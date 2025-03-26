import pytest
from uuid import UUID
import asyncio
import base64

from aidolon_browser_client.api.session_management import (
    create_browser_session, close_browser_session
)
from aidolon_browser_client.api.browser_actions import navigate_browser
from aidolon_browser_client.api.content_extraction import take_screenshot
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.navigate_browser_body import NavigateBrowserBody
from aidolon_browser_client.models.take_screenshot_body import TakeScreenshotBody
from aidolon_browser_client.client import Client


def test_take_screenshot_sync(client: Client):
    """Test taking a screenshot using the synchronous API."""
    # Create a session and navigate to a page
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page to screenshot
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        navigate_browser.sync(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Take a screenshot of the viewport
        screenshot_body = TakeScreenshotBody(full_page=False, delay=0)
        response = take_screenshot.sync_detailed(
            session_id=session_id,
            client=client,
            body=screenshot_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "screenshot"
        assert response.parsed.data is not None
        
        # Verify data is valid base64-encoded image
        screenshot_data = base64.b64decode(response.parsed.data)
        assert screenshot_data.startswith((b'\xff\xd8\xff', b'\x89PNG', b'GIF8'))  # Common image format signatures
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )


@pytest.mark.asyncio
async def test_take_screenshot_async(client: Client):
    """Test taking a screenshot using the asynchronous API."""
    # Create a session and navigate to a page
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page to screenshot
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        await navigate_browser.asyncio(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Take a full-page screenshot
        screenshot_body = TakeScreenshotBody(full_page=True, delay=0.5)
        response = await take_screenshot.asyncio_detailed(
            session_id=session_id,
            client=client,
            body=screenshot_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "screenshot"
        assert response.parsed.data is not None
        
        # Verify data is valid base64-encoded image
        screenshot_data = base64.b64decode(response.parsed.data)
        assert screenshot_data.startswith((b'\xff\xd8\xff', b'\x89PNG', b'GIF8'))  # Common image format signatures
    finally:
        # Clean up by closing the session
        await close_browser_session.asyncio(
            session_id=session_id,
            client=client
        )


def test_take_screenshot_with_delay(client: Client):
    """Test taking a screenshot with a delay."""
    # Create a session and navigate to a page
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page to screenshot
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        navigate_browser.sync(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Take a screenshot with a delay
        screenshot_body = TakeScreenshotBody(full_page=True, delay=1.0)  # 1 second delay
        response = take_screenshot.sync_detailed(
            session_id=session_id,
            client=client,
            body=screenshot_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.data is not None
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )
