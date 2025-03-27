import pytest
import asyncio
from uuid import UUID

from aidolon_browser_client.api.session_management.get_browser_context import (
    sync_detailed,
    sync,
    asyncio_detailed,
    asyncio as asyncio_get_browser_context,
)
from aidolon_browser_client.models.get_browser_context_response_200 import GetBrowserContextResponse200
from aidolon_browser_client.models.browser_context import BrowserContext

# This fixture creates a browser session for testing and returns its ID
# In a real implementation, you would use your API to create a browser session
@pytest.fixture
def browser_session_id(client):
    # TODO: Replace with actual code to create a browser session
    # For example:
    # response = create_browser_session_sync(client=client, url="https://example.com")
    # return response.session_id
    
    # For now, using a placeholder UUID - will fail tests until replaced
    return UUID("12345678-1234-5678-1234-567812345678")

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
