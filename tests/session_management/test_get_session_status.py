import asyncio
import time
from http import HTTPStatus

import pytest
from uuid import UUID

from aidolon_browser_client.api.session_management.get_session_status import (
    asyncio as gs_asyncio,
    asyncio_detailed as gs_asyncio_detailed,
    sync as gs_sync,
    sync_detailed as gs_sync_detailed,
)
from aidolon_browser_client.api.session_management.create_browser_session import sync as create_session
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.api.browser_actions.navigate_browser import sync as navigate_browser
from aidolon_browser_client.models.navigate_browser_body import NavigateBrowserBody
from aidolon_browser_client.api.session_management.close_browser_session import sync as close_session
from aidolon_browser_client.client import Client
from aidolon_browser_client.models.error import Error
from aidolon_browser_client.models.get_session_status_response_200 import GetSessionStatusResponse200
from aidolon_browser_client.models.get_session_status_response_200_status import GetSessionStatusResponse200Status


# Helper functions for validation
def validate_success_response(response):
    """Validate a successful response from get_session_status."""
    assert isinstance(response, GetSessionStatusResponse200)
    assert response.success is True
    assert isinstance(response.session_id, UUID)
    assert isinstance(response.status, GetSessionStatusResponse200Status)
    assert response.status in (GetSessionStatusResponse200Status.ACTIVE, GetSessionStatusResponse200Status.CLOSED)
    
    # Validate timestamps
    assert response.created_at is not None
    assert response.updated_at is not None
    
    # If session is active, validate last_active_at and live_session
    if response.status == GetSessionStatusResponse200Status.ACTIVE:
        assert response.last_active_at is not None
        assert response.live_session is not None
    # If session is closed, validate closed_at
    elif response.status == GetSessionStatusResponse200Status.CLOSED:
        assert response.closed_at is not None


def validate_error_response(response):
    """Validate an error response."""
    assert isinstance(response, Error)
    assert response.success is False
    assert response.error is not None
    assert response.error_code is not None


# Test fixture for client initialization
@pytest.fixture
def client():
    """Create a client instance for testing."""
    return Client(base_url="http://localhost:8000")  # Adjust URL as needed


# This fixture creates a browser session for testing and returns its ID
@pytest.fixture
def browser_session_id(client):
    """Create a new browser session and return its ID."""
    # Create a new browser session
    session_body = CreateBrowserSessionBody()
    response = create_session(client=client, body=session_body)
    
    # Extract the session ID from the response
    session_id = response.session_id
    
    # Navigate to initialize the browser context
    navigate_body = NavigateBrowserBody(url="https://www.example.com")
    navigate_browser(session_id=session_id, client=client, body=navigate_body)
    
    # Wait for the browser context to be fully initialized
    time.sleep(2)
    
    return session_id


# Fixture for an active session ID (uses the browser_session_id fixture)
@pytest.fixture
def active_session_id(browser_session_id):
    """Return the ID of an active session for testing."""
    return browser_session_id


# Fixture for a closed session ID
@pytest.fixture
def closed_session_id(client):
    """Return the ID of a closed session for testing."""
    # Create a new session
    session_body = CreateBrowserSessionBody()
    response = create_session(client=client, body=session_body)
    session_id = response.session_id
    
    # Close the session
    close_session(session_id=session_id, client=client)
    
    return session_id


# Fixture for a nonexistent session ID
@pytest.fixture
def nonexistent_session_id():
    """Return a UUID that doesn't correspond to any session."""
    return UUID("00000000-0000-0000-0000-000000000000")


# Synchronous tests

def test_sync_detailed_active_session(client, active_session_id):
    """Test sync_detailed with an active session."""
    response = gs_sync_detailed(session_id=active_session_id, client=client)
    
    assert response.status_code == HTTPStatus.OK
    assert response.parsed is not None
    validate_success_response(response.parsed)
    assert response.parsed.status == GetSessionStatusResponse200Status.ACTIVE


def test_sync_detailed_closed_session(client, closed_session_id):
    """Test sync_detailed with a closed session."""
    response = gs_sync_detailed(session_id=closed_session_id, client=client)
    
    assert response.status_code == HTTPStatus.OK
    assert response.parsed is not None
    validate_success_response(response.parsed)
    assert response.parsed.status == GetSessionStatusResponse200Status.CLOSED


def test_sync_detailed_nonexistent_session(client, nonexistent_session_id):
    """Test sync_detailed with a nonexistent session ID."""
    response = gs_sync_detailed(session_id=nonexistent_session_id, client=client)
    
    assert response.status_code == HTTPStatus.NOT_FOUND
    validate_error_response(response.parsed)


def test_sync_active_session(client, active_session_id):
    """Test sync with an active session."""
    response = gs_sync(session_id=active_session_id, client=client)
    
    assert response is not None
    validate_success_response(response)
    assert response.status == GetSessionStatusResponse200Status.ACTIVE


def test_sync_closed_session(client, closed_session_id):
    """Test sync with a closed session."""
    response = gs_sync(session_id=closed_session_id, client=client)
    
    assert response is not None
    validate_success_response(response)
    assert response.status == GetSessionStatusResponse200Status.CLOSED


def test_sync_nonexistent_session(client, nonexistent_session_id):
    """Test sync with a nonexistent session ID."""
    response = gs_sync(session_id=nonexistent_session_id, client=client)
    
    assert response is not None
    validate_error_response(response)


# Asynchronous tests

@pytest.mark.asyncio
async def test_asyncio_detailed_active_session(client, active_session_id):
    """Test asyncio_detailed with an active session."""
    response = await gs_asyncio_detailed(session_id=active_session_id, client=client)
    
    assert response.status_code == HTTPStatus.OK
    assert response.parsed is not None
    validate_success_response(response.parsed)
    assert response.parsed.status == GetSessionStatusResponse200Status.ACTIVE


@pytest.mark.asyncio
async def test_asyncio_detailed_closed_session(client, closed_session_id):
    """Test asyncio_detailed with a closed session."""
    response = await gs_asyncio_detailed(session_id=closed_session_id, client=client)
    
    assert response.status_code == HTTPStatus.OK
    assert response.parsed is not None
    validate_success_response(response.parsed)
    assert response.parsed.status == GetSessionStatusResponse200Status.CLOSED


@pytest.mark.asyncio
async def test_asyncio_detailed_nonexistent_session(client, nonexistent_session_id):
    """Test asyncio_detailed with a nonexistent session ID."""
    response = await gs_asyncio_detailed(session_id=nonexistent_session_id, client=client)
    
    assert response.status_code == HTTPStatus.NOT_FOUND
    validate_error_response(response.parsed)


@pytest.mark.asyncio
async def test_asyncio_active_session(client, active_session_id):
    """Test asyncio with an active session."""
    response = await gs_asyncio(session_id=active_session_id, client=client)
    
    assert response is not None
    validate_success_response(response)
    assert response.status == GetSessionStatusResponse200Status.ACTIVE


@pytest.mark.asyncio
async def test_asyncio_closed_session(client, closed_session_id):
    """Test asyncio with a closed session."""
    response = await gs_asyncio(session_id=closed_session_id, client=client)
    
    assert response is not None
    validate_success_response(response)
    assert response.status == GetSessionStatusResponse200Status.CLOSED


@pytest.mark.asyncio
async def test_asyncio_nonexistent_session(client, nonexistent_session_id):
    """Test asyncio with a nonexistent session ID."""
    response = await gs_asyncio(session_id=nonexistent_session_id, client=client)
    
    assert response is not None
    validate_error_response(response)
