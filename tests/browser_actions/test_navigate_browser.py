import pytest
from uuid import UUID
import asyncio

from aidolon_browser_client.api.session_management import (
    create_browser_session, close_browser_session
)
from aidolon_browser_client.api.browser_actions import navigate_browser
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.navigate_browser_body import NavigateBrowserBody
from aidolon_browser_client.client import Client


def test_navigate_browser_sync(client: Client):
    """Test navigating a browser to a URL using the synchronous API."""
    # First, create a session
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a URL
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        response = navigate_browser.sync_detailed(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "navigate"
        assert response.parsed.url == "https://www.example.com"
        
        # Navigate to another URL
        navigate_body = NavigateBrowserBody(url="https://www.google.com")
        response = navigate_browser.sync_detailed(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "navigate"
        assert response.parsed.url == "https://www.google.com"
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )


@pytest.mark.asyncio
async def test_navigate_browser_async(client: Client):
    """Test navigating a browser to a URL using the asynchronous API."""
    # First, create a session
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a URL
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        response = await navigate_browser.asyncio_detailed(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "navigate"
        assert response.parsed.url == "https://www.example.com"
        
        # Navigate to another URL
        navigate_body = NavigateBrowserBody(url="https://www.google.com")
        response = await navigate_browser.asyncio_detailed(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "navigate"
        assert response.parsed.url == "https://www.google.com"
    finally:
        # Clean up by closing the session
        await close_browser_session.asyncio(
            session_id=session_id,
            client=client
        )


def test_navigate_browser_invalid_url(client: Client):
    """Test navigating to an invalid URL."""
    # First, create a session
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Try to navigate to an invalid URL
        navigate_body = NavigateBrowserBody(url="invalid-url")
        response = navigate_browser.sync_detailed(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Should either return a 400 or a successful navigation that might show an error page
        # The exact behavior depends on the browser implementation
        if response.status_code == 400:
            assert response.parsed is not None
            assert hasattr(response.parsed, 'error')
        else:
            assert response.status_code == 200
            assert response.parsed is not None
            assert response.parsed.success is True
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )
