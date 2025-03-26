import pytest
from uuid import UUID
import asyncio
import base64

from aidolon_browser_client.api.session_management import (
    create_browser_session, close_browser_session
)
from aidolon_browser_client.api.browser_actions import navigate_browser
from aidolon_browser_client.api.content_extraction import generate_pdf
from aidolon_browser_client.models.create_browser_session_body import CreateBrowserSessionBody
from aidolon_browser_client.models.navigate_browser_body import NavigateBrowserBody
from aidolon_browser_client.models.generate_pdf_body import GeneratePdfBody
from aidolon_browser_client.client import Client


def test_generate_pdf_sync(client: Client):
    """Test generating a PDF using the synchronous API."""
    # Create a session and navigate to a page
    body = CreateBrowserSessionBody()
    create_response = create_browser_session.sync(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page to generate PDF from
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        navigate_browser.sync(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Generate PDF
        pdf_body = GeneratePdfBody(delay=0)  # No delay before generating
        response = generate_pdf.sync_detailed(
            session_id=session_id,
            client=client,
            body=pdf_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "pdf"
        assert response.parsed.data is not None
        
        # Verify data is valid base64-encoded PDF
        pdf_data = base64.b64decode(response.parsed.data)
        assert pdf_data.startswith(b'%PDF-')  # PDF magic number
    finally:
        # Clean up by closing the session
        close_browser_session.sync(
            session_id=session_id,
            client=client
        )


@pytest.mark.asyncio
async def test_generate_pdf_async(client: Client):
    """Test generating a PDF using the asynchronous API."""
    # Create a session and navigate to a page
    body = CreateBrowserSessionBody()
    create_response = await create_browser_session.asyncio(client=client, body=body)
    
    assert create_response is not None
    session_id = create_response.session_id
    
    try:
        # Navigate to a page to generate PDF from
        navigate_body = NavigateBrowserBody(url="https://www.example.com")
        await navigate_browser.asyncio(
            session_id=session_id,
            client=client,
            body=navigate_body
        )
        
        # Generate PDF with a delay
        pdf_body = GeneratePdfBody(delay=0.5)  # Wait half a second before generating
        response = await generate_pdf.asyncio_detailed(
            session_id=session_id,
            client=client,
            body=pdf_body
        )
        
        # Validate the response
        assert response.status_code == 200
        assert response.parsed is not None
        assert response.parsed.success is True
        assert response.parsed.action == "pdf"
        assert response.parsed.data is not None
        
        # Verify data is valid base64-encoded PDF
        pdf_data = base64.b64decode(response.parsed.data)
        assert pdf_data.startswith(b'%PDF-')  # PDF magic number
    finally:
        # Clean up by closing the session
        await close_browser_session.asyncio(
            session_id=session_id,
            client=client
        )


def test_generate_pdf_session_not_found(client: Client):
    """Test generating a PDF for a non-existent session."""
    # Use a random UUID that shouldn't exist
    random_uuid = UUID('00000000-0000-0000-0000-000000000000')
    
    # Try to generate a PDF
    pdf_body = GeneratePdfBody()
    response = generate_pdf.sync_detailed(
        session_id=random_uuid,
        client=client,
        body=pdf_body
    )
    
    # Should return a 404
    assert response.status_code == 404
    assert response.parsed is not None
    assert hasattr(response.parsed, 'error')
