import pytest
import asyncio
import time
from uuid import UUID

from aidolon_browser_client.api.session_management.get_browser_context import (
    sync_detailed,
    sync,
    asyncio_detailed,
    asyncio as asyncio_get_browser_context,
)
from aidolon_browser_client.api.session_management.create_browser_session import sync as create_session
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.api.browser_actions.navigate_browser import sync as navigate_browser
from aidolon_browser_client.models.navigate_browser_body import NavigateBrowserBody
from aidolon_browser_client.models.get_browser_context_response_200 import GetBrowserContextResponse200
from aidolon_browser_client.models.browser_context import BrowserContext

# This fixture creates a browser session for testing and returns its ID
@pytest.fixture
def browser_session_id(client):
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

def test_sync_detailed_get_browser_context(client, browser_session_id):
    """Test the sync_detailed function for getting browser context."""
    # Act
    response = sync_detailed(session_id=browser_session_id, client=client)
    
    # Assert
    assert response.status_code == 200
    assert isinstance(response.parsed, GetBrowserContextResponse200)
    assert response.parsed.success is True
    assert isinstance(response.parsed.context, BrowserContext)

def test_sync_get_browser_context(client, browser_session_id):
    """Test the sync function for getting browser context."""
    # Act
    result = sync(session_id=browser_session_id, client=client)
    
    # Assert
    assert isinstance(result, GetBrowserContextResponse200)
    assert result.success is True
    assert isinstance(result.context, BrowserContext)

@pytest.mark.asyncio
async def test_asyncio_detailed_get_browser_context(client, browser_session_id):
    """Test the asyncio_detailed function for getting browser context."""
    # Act
    response = await asyncio_detailed(session_id=browser_session_id, client=client)
    
    # Assert
    assert response.status_code == 200
    assert isinstance(response.parsed, GetBrowserContextResponse200)
    assert response.parsed.success is True
    assert isinstance(response.parsed.context, BrowserContext)

@pytest.mark.asyncio
async def test_asyncio_get_browser_context(client, browser_session_id):
    """Test the asyncio function for getting browser context."""
    # Act
    result = await asyncio_get_browser_context(session_id=browser_session_id, client=client)
    
    # Assert
    assert isinstance(result, GetBrowserContextResponse200)
    assert result.success is True
    assert isinstance(result.context, BrowserContext)
