import pytest
from uuid import UUID
import asyncio

from aidolon_browser_client.api.session_management import (
    create_browser_session, close_browser_session
)
from aidolon_browser_client.api.browser_actions import navigate_browser
from aidolon_browser_client.api.content_extraction import scrape_page
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.navigate_browser_body import NavigateBrowserBody
from aidolon_browser_client.models.scrape_page_body import ScrapePageBody
from aidolon_browser_client.models.scrape_page_body_format_item import ScrapePageBodyFormatItem
from aidolon_browser_client.client import Client


def test_scrape_page_sync(client: Client):
    """Test scraping a page using the synchronous API."""
    # Create a session and navigate to a page
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page to scrape
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        navigate_browser.sync(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Scrape the page
        scrape_body = ScrapePageBody(
            selector="body",  # Scrape the entire page
            include_html=True,
            format=[ScrapePageBodyFormatItem.TEXT, ScrapePageBodyFormatItem.JSON]
        )
        response = scrape_page.sync_detailed(
            session_id=session_id,
            client=client,
            body=scrape_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "scrape"
        assert response.parsed.data is not None
        
        # Check that the requested formats are present
        assert response.parsed.data.text is not None
        assert response.parsed.data.json is not None
        assert response.parsed.data.html is not None
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )


@pytest.mark.asyncio
async def test_scrape_page_async(client: Client):
    """Test scraping a page using the asynchronous API."""
    # Create a session and navigate to a page
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page to scrape
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        await navigate_browser.asyncio(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Scrape the page, just getting text
        scrape_body = ScrapePageBody(
            selector="body",  # Scrape the entire page
            include_html=False,
            format=[ScrapePageBodyFormatItem.TEXT]
        )
        response = await scrape_page.asyncio_detailed(
            session_id=session_id,
            client=client,
            body=scrape_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "scrape"
        assert response.parsed.data is not None
        
        # Check that text is present but HTML is not
        assert response.parsed.data.text is not None
        assert response.parsed.data.html is None
    finally:
        # Clean up by closing the session
        await close_browser_session.asyncio(
            session_id=session_id,
            client=client
        )


def test_scrape_page_with_specific_selector(client: Client):
    """Test scraping a specific element on a page."""
    # Create a session and navigate to a page
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page to scrape
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        navigate_browser.sync(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Scrape just the first paragraph
        scrape_body = ScrapePageBody(
            selector="p",  # Scrape the first paragraph
            include_html=True,
            format=[ScrapePageBodyFormatItem.TEXT, ScrapePageBodyFormatItem.HTML]
        )
        response = scrape_page.sync_detailed(
            session_id=session_id,
            client=client,
            body=scrape_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.data is not None
        
        # Check that text and HTML are present but should be shorter than scraping the whole page
        assert response.parsed.data.text is not None
        assert response.parsed.data.html is not None
        assert "<p" in response.parsed.data.html  # Should contain paragraph tag
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )
