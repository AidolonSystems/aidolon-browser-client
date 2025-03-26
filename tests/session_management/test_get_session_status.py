import pytest
from uuid import UUID
import asyncio

from aidolon_browser_client.api.session_management import (
    get_session_status, create_browser_session, close_browser_session
)
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.client import Client


def test_get_session_status_sync(client: Client):
    """Test getting a browser session status using the synchronous API."""
    # First, create a session to get status for
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Get the session status
        response = get_session_status.sync_detailed(
            session_id=session_id,
            client=client
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.session_id == session_id
        assert response.parsed.status == "active"
        assert response.parsed.created_at is not None
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )


@pytest.mark.asyncio
async def test_get_session_status_async(client: Client):
    """Test getting a browser session status using the asynchronous API."""
    # First, create a session to get status for
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Get the session status
        response = await get_session_status.asyncio_detailed(
            session_id=session_id,
            client=client
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.session_id == session_id
        assert response.parsed.status == "active"
        assert response.parsed.created_at is not None
    finally:
        # Clean up by closing the session
        await close_browser_session.asyncio(
            session_id=session_id,
            client=client
        )


def test_get_session_status_not_found(client: Client):
    """Test getting a non-existent session status."""
    # Use a random UUID that shouldn't exist
    random_uuid = UUID('00000000-0000-0000-0000-000000000000')
    
    # Get the session status
    response = get_session_status.sync_detailed(
        session_id=random_uuid,
        client=client
    )
    
    # Should return a 404
    assert response.status_code == 404
    assert response.parsed is not None
    assert hasattr(response.parsed, 'error')
