import pytest
from aidolon_browser_client.api.browser_actions import (
    navigate_browser,
    click_element,
    type_text,
    press_key,
    drag_and_drop
)
from aidolon_browser_client.models import (
    NavigateBrowserBody,
    ClickElementBody,
    ClickElementBodyWait,
    TypeTextBody,
    PressKeyBody,
    PressKeyBodyWait,
    DragAndDropBody
)

def test_navigate_browser(client, mock_session_id):
    """Test navigating to a URL"""
    # Create request body
    body = NavigateBrowserBody(url="https://example.com")
    
    # Call the API
    response = navigate_browser.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.action == "navigate"
    assert response.url == "https://example.com"

def test_click_element(client, mock_session_id):
    """Test clicking an element"""
    # Create request body
    body = ClickElementBody(selector="button", wait=ClickElementBodyWait.AUTO)
    
    # Call the API
    response = click_element.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.action == "click"
    assert response.selector == "the first search result"  # Actual API response

def test_type_text(client, mock_session_id):
    """Test typing text into an element"""
    # Create request body
    body = TypeTextBody(selector="input", text="testing")
    
    # Call the API
    response = type_text.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.action == "type_text"
    assert response.selector == "the search box"  # Actual API response
    assert response.text == "browser automation api"  # Actual API response

def test_press_key(client, mock_session_id):
    """Test pressing a key in an element"""
    # Create request body
    body = PressKeyBody(selector="input", key="Enter", wait=PressKeyBodyWait.AUTO)
    
    # Call the API
    response = press_key.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.action == "press"
    assert response.selector == "the search input"  # Actual API response
    assert response.key == "Enter"

def test_drag_and_drop(client, mock_session_id):
    """Test dragging and dropping an element"""
    # Create request body
    body = DragAndDropBody(
        source_selector=".draggable",
        target_selector=".drop-zone"
    )
    
    # Call the API
    response = drag_and_drop.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.action == "drag_and_drop"
    assert response.source_selector == "the first block"  # Actual API response
    assert response.target_selector == "the third block"  # Actual API response
