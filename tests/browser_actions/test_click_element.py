import pytest
from uuid import UUID
import asyncio

from aidolon_browser_client.api.session_management import (
    create_browser_session, close_browser_session
)
from aidolon_browser_client.api.browser_actions import (
    navigate_browser, click_element
)
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.navigate_browser_body import NavigateBrowserBody
from aidolon_browser_client.models.click_element_body import ClickElementBody
from aidolon_browser_client.models.click_element_body_wait import ClickElementBodyWait
from aidolon_browser_client.client import Client


def test_click_element_sync(client: Client):
    """Test clicking an element using the synchronous API."""
    # First, create a session and navigate to a test page
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page with clickable elements
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        navigate_browser.sync(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Click on a link or button
        click_body = ClickElementBody(
            selector="a",  # Example selects the first link
            wait=ClickElementBodyWait.NAVIGATION
        )
        response = click_element.sync_detailed(
            session_id=session_id,
            client=client,
            body=click_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "click"
        assert response.parsed.selector == "a"
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )


@pytest.mark.asyncio
async def test_click_element_async(client: Client):
    """Test clicking an element using the asynchronous API."""
    # First, create a session and navigate to a test page
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page with clickable elements
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        await navigate_browser.asyncio(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Click on a link or button
        click_body = ClickElementBody(
            selector="a",  # Example selects the first link
            wait=ClickElementBodyWait.NAVIGATION
        )
        response = await click_element.asyncio_detailed(
            session_id=session_id,
            client=client,
            body=click_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "click"
        assert response.parsed.selector == "a"
    finally:
        # Clean up by closing the session
        await close_browser_session.asyncio(
            session_id=session_id,
            client=client
        )


def test_click_element_invalid_selector(client: Client):
    """Test clicking with an invalid selector."""
    # First, create a session and navigate to a test page
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a simple page
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        navigate_browser.sync(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Try to click on a non-existent element
        click_body = ClickElementBody(
            selector="#does-not-exist-123456",
            wait=ClickElementBodyWait.NONE
        )
        response = click_element.sync_detailed(
            session_id=session_id,
            client=client,
            body=click_body
        )
        
        # Should return a 400 or contain an error message
        assert response.status_code != 200 or (response.parsed and hasattr(response.parsed, 'error'))
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )
