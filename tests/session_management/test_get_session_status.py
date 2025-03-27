import asyncio
from http import HTTPStatus

import pytest
from uuid import UUID

from aidolon_browser_client.api.session_management.get_session_status import (
    asyncio as gs_asyncio,
    asyncio_detailed as gs_asyncio_detailed,
    sync as gs_sync,
    sync_detailed as gs_sync_detailed,
)
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
    # For testing, we'll just mock an active session ID
    # In a real scenario, you would create a real session and return its ID
    return UUID("00000000-0000-0000-0000-000000000001")


# Fixture for existing session IDs
@pytest.fixture
def active_session_id():
    """Return the ID of an active session for testing."""
    return UUID("00000000-0000-0000-0000-000000000001")


@pytest.fixture
def closed_session_id():
    """Return the ID of a closed session for testing."""
    return UUID("00000000-0000-0000-0000-000000000002")


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
