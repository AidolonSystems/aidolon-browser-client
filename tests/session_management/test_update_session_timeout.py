import pytest
from uuid import UUID
import asyncio

from aidolon_browser_client.api.session_management import (
    update_session_timeout, create_browser_session, close_browser_session
)
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.update_session_timeout_body import UpdateSessionTimeoutBody
from aidolon_browser_client.client import Client


def test_update_session_timeout_sync(client: Client):
    """Test updating a browser session timeout using the synchronous API."""
    # First, create a session to update
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Update the session timeout
        timeout_body = UpdateSessionTimeoutBody(timeout=600)  # 10 minutes
        response = update_session_timeout.sync_detailed(
            session_id=session_id,
            client=client,
            body=timeout_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.session_id == session_id
        assert response.parsed.timeout == 600
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )


@pytest.mark.asyncio
async def test_update_session_timeout_async(client: Client):
    """Test updating a browser session timeout using the asynchronous API."""
    # First, create a session to update
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Update the session timeout
        timeout_body = UpdateSessionTimeoutBody(timeout=900)  # 15 minutes
        response = await update_session_timeout.asyncio_detailed(
            session_id=session_id,
            client=client,
            body=timeout_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.session_id == session_id
        assert response.parsed.timeout == 900
    finally:
        # Clean up by closing the session
        await close_browser_session.asyncio(
            session_id=session_id,
            client=client
        )


def test_update_session_timeout_not_found(client: Client):
    """Test updating timeout for a non-existent session."""
    # Use a random UUID that shouldn't exist
    random_uuid = UUID('00000000-0000-0000-0000-000000000000')
    
    # Attempt to update the session timeout
    timeout_body = UpdateSessionTimeoutBody(timeout=600)
    response = update_session_timeout.sync_detailed(
        session_id=random_uuid,
        client=client,
        body=timeout_body
    )
    
    # Should return a 404
    assert response.status_code == 404
    assert response.parsed is not None
    assert hasattr(response.parsed, 'error')
