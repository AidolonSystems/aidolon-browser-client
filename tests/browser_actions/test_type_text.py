import pytest
from uuid import UUID
import asyncio

from aidolon_browser_client.api.session_management import (
    create_browser_session, close_browser_session
)
from aidolon_browser_client.api.browser_actions import (
    navigate_browser, type_text
)
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.navigate_browser_body import NavigateBrowserBody
from aidolon_browser_client.models.type_text_body import TypeTextBody
from aidolon_browser_client.client import Client


def test_type_text_sync(client: Client):
    """Test typing text using the synchronous API."""
    # Create a session and navigate to a page with input fields
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page with a search input
        navigate_body = NavigateBrowserBody(url="https://www.google.com")
        navigate_browser.sync(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Type text into search input
        text_body = TypeTextBody(
            selector="input[name='q']",  # Google search input
            text="pytest automation",
            delay=0  # Type with no delay between characters
        )
        response = type_text.sync_detailed(
            session_id=session_id,
            client=client,
            body=text_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "type_text"
        assert response.parsed.selector == "input[name='q']"
        assert response.parsed.text == "pytest automation"
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )


@pytest.mark.asyncio
async def test_type_text_async(client: Client):
    """Test typing text using the asynchronous API."""
    # Create a session and navigate to a page with input fields
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page with a search input
        navigate_body = NavigateBrowserBody(url="https://www.google.com")
        await navigate_browser.asyncio(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Type text into search input
        text_body = TypeTextBody(
            selector="input[name='q']",  # Google search input
            text="async python testing",
            delay=50  # Type with 50ms delay between characters
        )
        response = await type_text.asyncio_detailed(
            session_id=session_id,
            client=client,
            body=text_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "type_text"
        assert response.parsed.selector == "input[name='q']"
        assert response.parsed.text == "async python testing"
    finally:
        # Clean up by closing the session
        await close_browser_session.asyncio(
            session_id=session_id,
            client=client
        )


def test_type_text_invalid_selector(client: Client):
    """Test typing text into an invalid selector."""
    # Create a session and navigate to a page
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
        
        # Try to type text into a non-existent element
        text_body = TypeTextBody(
            selector="#does-not-exist-123456",
            text="test text",
            delay=0
        )
        response = type_text.sync_detailed(
            session_id=session_id,
            client=client,
            body=text_body
        )
        
        # Should return a 400 or contain an error message
        assert response.status_code != 200 or (response.parsed and hasattr(response.parsed, 'error'))
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )
