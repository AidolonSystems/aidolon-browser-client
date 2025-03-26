import pytest
from uuid import UUID
import asyncio

from aidolon_browser_client.api.session_management import create_browser_session
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.create_browser_session_response_200 import CreateBrowserSessionResponse200
from aidolon_browser_client.client import Client


def test_create_browser_session_sync(client: Client):
    """Test creating a browser session using the synchronous API."""
    # Create a browser session with default parameters
    body = CreateBrowserSessionBody()
    
    # Call the create_browser_session endpoint
    response = create_browser_session.sync_detailed(client=client, body=body)
    
    # Validate the response
    assert response.status_code == 200
    assert response.parsed is not None
    
    # Check that the response is a valid CreateBrowserSessionResponse200
    assert isinstance(response.parsed, CreateBrowserSessionResponse200)
    assert response.parsed.success is True
    
    # Validate session details
    assert isinstance(response.parsed.session_id, UUID)
    assert response.parsed.status == "active"
    assert response.parsed.embed_url is not None
    assert response.parsed.created_at is not None
    
    # Verify that live_session information is present
    assert response.parsed.live_session is not None
    
    # Further checks could verify that the session appears in database
    # This would depend on how the test environment is set up


@pytest.mark.asyncio
async def test_create_browser_session_async(client: Client):
    """Test creating a browser session using the asynchronous API."""
    # Create a browser session with default parameters
    body = CreateBrowserSessionBody()
    
    # Call the create_browser_session endpoint asynchronously
    response = await create_browser_session.asyncio_detailed(client=client, body=body)
    
    # Validate the response
    assert response.status_code == 200
    assert response.parsed is not None
    
    # Check that the response is a valid CreateBrowserSessionResponse200
    assert isinstance(response.parsed, CreateBrowserSessionResponse200)
    assert response.parsed.success is True
    
    # Validate session details
    assert isinstance(response.parsed.session_id, UUID)
    assert response.parsed.status == "active"
    assert response.parsed.embed_url is not None
    assert response.parsed.created_at is not None
    
    # Verify that live_session information is present
    assert response.parsed.live_session is not None
    
    # Further checks could verify that the session appears in database
    # This would depend on how the test environment is set up
