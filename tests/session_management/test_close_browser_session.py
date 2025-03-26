import pytest
from uuid import UUID
import asyncio

from aidolon_browser_client.api.session_management import (
    close_browser_session, create_browser_session, get_session_status
)
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.client import Client


def test_close_browser_session_sync(client: Client):
    """Test closing a browser session using the synchronous API."""
    # First, create a session to close
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    # Close the session
    response = close_browser_session.sync_detailed(
        session_id=session_id,
        client=client
    )
    
    # Validate the response
    assert response.status_code == 200
    assert response.parsed is not None
    assert response.parsed.success is True
    assert response.parsed.session_id == session_id
    assert response.parsed.status == "closed"
    
    # Verify the session is actually closed
    status_response = get_session_status.sync(
        session_id=session_id,
        client=client
    )
    
    assert status_response is not None
    assert status_response.status == "closed"
    assert status_response.closed_at is not None


@pytest.mark.asyncio
async def test_close_browser_session_async(client: Client):
    """Test closing a browser session using the asynchronous API."""
    # First, create a session to close
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    # Close the session
    response = await close_browser_session.asyncio_detailed(
        session_id=session_id,
        client=client
    )
    
    # Validate the response
    assert response.status_code == 200
    assert response.parsed is not None
    assert response.parsed.success is True
    assert response.parsed.session_id == session_id
    assert response.parsed.status == "closed"
    
    # Verify the session is actually closed
    status_response = await get_session_status.asyncio(
        session_id=session_id,
        client=client
    )
    
    assert status_response is not None
    assert status_response.status == "closed"
    assert status_response.closed_at is not None


def test_close_browser_session_not_found(client: Client):
    """Test closing a non-existent session."""
    # Use a random UUID that shouldn't exist
    random_uuid = UUID('00000000-0000-0000-0000-000000000000')
    
    # Attempt to close the session
    response = close_browser_session.sync_detailed(
        session_id=random_uuid,
        client=client
    )
    
    # Should return a 404
    assert response.status_code == 404
    assert response.parsed is not None
    assert hasattr(response.parsed, 'error')
