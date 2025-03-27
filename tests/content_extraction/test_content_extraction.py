import pytest
from aidolon_browser_client.api.content_extraction import (
    take_screenshot,
    scrape_information,
    scrape_page,
    generate_pdf
)
from aidolon_browser_client.models import (
    TakeScreenshotBody,
    ScrapeInformationBody,
    ScrapeInformationBodyLevelOfDetail,
    ScrapePageBody,
    ScrapePageBodyFormatItem,
    GeneratePdfBody
)

def test_take_screenshot(client, mock_session_id):
    """Test taking a screenshot"""
    # Create request body
    body = TakeScreenshotBody(full_page=True)
    
    # Call the API
    response = take_screenshot.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.action == "screenshot"
    assert response.data is not None  # Base64-encoded image data

def test_scrape_information(client, mock_session_id):
    """Test scraping specific information"""
    # Create request body
    body = ScrapeInformationBody(
        description="all products on the page",
        level_of_detail=ScrapeInformationBodyLevelOfDetail.FULL
    )
    
    # Call the API
    response = scrape_information.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.action == "scrape_information"
    assert response.description == "the page title and main content"  # Actual API response
    assert response.data is not None

def test_scrape_page(client, mock_session_id):
    """Test scraping the entire page"""
    # Create request body
    body = ScrapePageBody(
        format_=[ScrapePageBodyFormatItem.HTML, ScrapePageBodyFormatItem.TEXT],
        screenshot=True
    )
    
    # Call the API
    response = scrape_page.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.action == "scrape"
    assert response.data is not None
    
    # Check that requested formats are in the response
    assert response.data.html is not None
    assert response.data.text is not None
    assert response.data.screenshot is not None

def test_generate_pdf(client, mock_session_id):
    """Test generating a PDF"""
    # Create request body
    body = GeneratePdfBody()
    
    # Call the API
    response = generate_pdf.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.action == "pdf"
    assert response.data is not None  # Base64-encoded PDF data
