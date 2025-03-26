import pytest
import asyncio
from uuid import UUID

from aidolon_browser_client.api.session_management import (
    list_browser_sessions, create_browser_session, close_browser_session
)
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.list_browser_sessions_status import ListBrowserSessionsStatus
from aidolon_browser_client.client import Client


def test_list_browser_sessions_sync(client: Client):
    """Test listing browser sessions using the synchronous API."""
    # Create a session to ensure we have at least one in the list
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # List all sessions
        response = list_browser_sessions.sync_detailed(
            client=client
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.sessions is not None
        assert len(response.parsed.sessions) > 0
        assert response.parsed.count > 0
        
        # Ensure our created session is in the list
        session_ids = [session.session_id for session in response.parsed.sessions]
        assert session_id in session_ids
        
        # Test filtering by status
        active_response = list_browser_sessions.sync_detailed(
            client=client,
            status=ListBrowserSessionsStatus.ACTIVE
        )
        
        assert active_response.status_code == 200
        assert active_response.parsed is not None
        assert active_response.parsed.sessions is not None
        
        # Our session should be in the active list
        active_session_ids = [session.session_id for session in active_response.parsed.sessions]
        assert session_id in active_session_ids
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )


@pytest.mark.asyncio
async def test_list_browser_sessions_async(client: Client):
    """Test listing browser sessions using the asynchronous API."""
    # Create a session to ensure we have at least one in the list
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # List all sessions
        response = await list_browser_sessions.asyncio_detailed(
            client=client
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.sessions is not None
        assert len(response.parsed.sessions) > 0
        assert response.parsed.count > 0
        
        # Ensure our created session is in the list
        session_ids = [session.session_id for session in response.parsed.sessions]
        assert session_id in session_ids
        
        # Test filtering by status
        active_response = await list_browser_sessions.asyncio_detailed(
            client=client,
            status=ListBrowserSessionsStatus.ACTIVE
        )
        
        assert active_response.status_code == 200
        assert active_response.parsed is not None
        assert active_response.parsed.sessions is not None
        
        # Our session should be in the active list
        active_session_ids = [session.session_id for session in active_response.parsed.sessions]
        assert session_id in active_session_ids
    finally:
        # Clean up by closing the session
        await close_browser_session.asyncio(
            session_id=session_id,
            client=client
        )
