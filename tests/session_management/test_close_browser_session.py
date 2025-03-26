import pytest
from uuid import UUID
import asyncio

from aidolon_browser_client.api.session_management import close_browser_session, create_browser_session, list_browser_sessions
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.create_browser_session_response_200 import CreateBrowserSessionResponse200
from aidolon_browser_client.models.close_browser_session_response_200 import CloseBrowserSessionResponse200
from aidolon_browser_client.models.list_browser_sessions_status import ListBrowserSessionsStatus
from aidolon_browser_client.client import Client


def test_close_browser_session_sync_detailed(client: Client):
    """Test closing a browser session using the synchronous detailed API."""
    # First create a browser session
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync_detailed(client=client, body=body)
    
    # Ensure session was created successfully
    assert create_response.status_code == 200
    assert create_response.parsed is not None
    assert isinstance(create_response.parsed, CreateBrowserSessionResponse200)
    
    # Get the session ID
    session_id = create_response.parsed.session_id
    
    # Close the session using detailed sync API
    close_response = close_browser_session.sync_detailed(
        session_id=session_id,
        client=client
    )
    
    # Validate the response
    assert close_response.status_code == 200
    assert close_response.parsed is not None
    assert isinstance(close_response.parsed, CloseBrowserSessionResponse200)
    assert close_response.parsed.success is True
    assert close_response.parsed.session_id == session_id
    
    # Verify session no longer appears in the list of active sessions
    list_response = list_browser_sessions.sync_detailed(
        client=client,
        status=ListBrowserSessionsStatus.ACTIVE
    )
    assert list_response.status_code == 200
    assert list_response.parsed is not None
    
    # Check that our closed session is not in the active list
    session_ids = [session.session_id for session in list_response.parsed.sessions]
    assert session_id not in session_ids


def test_close_browser_session_sync(client: Client):
    """Test closing a browser session using the synchronous convenience API."""
    # First create a browser session
    body = CreateBrowserSessionBody()
    create_result = create_browser_session.sync(client=client, body=body)
    
    # Ensure session was created successfully
    assert create_result is not None
    assert isinstance(create_result, CreateBrowserSessionResponse200)
    
    # Get the session ID
    session_id = create_result.session_id
    
    # Close the session using sync convenience API
    close_result = close_browser_session.sync(
        session_id=session_id,
        client=client
    )
    
    # Validate the response
    assert close_result is not None
    assert isinstance(close_result, CloseBrowserSessionResponse200)
    assert close_result.success is True
    assert close_result.session_id == session_id
    
    # Verify session no longer appears in the list of active sessions
    list_result = list_browser_sessions.sync(
        client=client,
        status=ListBrowserSessionsStatus.ACTIVE
    )
    assert list_result is not None
    
    # Check that our closed session is not in the active list
    session_ids = [session.session_id for session in list_result.sessions]
    assert session_id not in session_ids


@pytest.mark.asyncio
async def test_close_browser_session_asyncio_detailed(client: Client):
    """Test closing a browser session using the asynchronous detailed API."""
    # First create a browser session
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio_detailed(client=client, body=body)
    
    # Ensure session was created successfully
    assert create_response.status_code == 200
    assert create_response.parsed is not None
    assert isinstance(create_response.parsed, CreateBrowserSessionResponse200)
    
    # Get the session ID
    session_id = create_response.parsed.session_id
    
    # Close the session using detailed async API
    close_response = await close_browser_session.asyncio_detailed(
        session_id=session_id,
        client=client
    )
    
    # Validate the response
    assert close_response.status_code == 200
    assert close_response.parsed is not None
    assert isinstance(close_response.parsed, CloseBrowserSessionResponse200)
    assert close_response.parsed.success is True
    assert close_response.parsed.session_id == session_id
    
    # Verify session no longer appears in the list of active sessions
    list_response = await list_browser_sessions.asyncio_detailed(
        client=client,
        status=ListBrowserSessionsStatus.ACTIVE
    )
    assert list_response.status_code == 200
    assert list_response.parsed is not None
    
    # Check that our closed session is not in the active list
    session_ids = [session.session_id for session in list_response.parsed.sessions]
    assert session_id not in session_ids


@pytest.mark.asyncio
async def test_close_browser_session_asyncio(client: Client):
    """Test closing a browser session using the asynchronous convenience API."""
    # First create a browser session
    body = CreateBrowserSessionBody()
    create_result = await create_browser_session.asyncio(client=client, body=body)
    
    # Ensure session was created successfully
    assert create_result is not None
    assert isinstance(create_result, CreateBrowserSessionResponse200)
    
    # Get the session ID
    session_id = create_result.session_id
    
    # Close the session using async convenience API
    close_result = await close_browser_session.asyncio(
        session_id=session_id,
        client=client
    )
    
    # Validate the response
    assert close_result is not None
    assert isinstance(close_result, CloseBrowserSessionResponse200)
    assert close_result.success is True
    assert close_result.session_id == session_id
    
    # Verify session no longer appears in the list of active sessions
    list_result = await list_browser_sessions.asyncio(
        client=client,
        status=ListBrowserSessionsStatus.ACTIVE
    )
    assert list_result is not None
    
    # Check that our closed session is not in the active list
    session_ids = [session.session_id for session in list_result.sessions]
    assert session_id not in session_ids
