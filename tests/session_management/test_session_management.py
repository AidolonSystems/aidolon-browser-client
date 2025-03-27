import pytest
from aidolon_browser_client.api.session_management import (
    create_browser_session,
    list_browser_sessions,
    close_browser_session,
    close_all_browser_sessions,
    get_browser_context,
    update_session_timeout
)
from aidolon_browser_client.models import (
    CreateBrowserSessionBody,
    UpdateSessionTimeoutBody
)

def test_create_browser_session(client):
    """Test creating a new browser session"""
    # Create request body
    body = CreateBrowserSessionBody(
        timeout=300,
        visible=True
    )
    
    # Call the API
    response = create_browser_session.sync(client=client, body=body)
    
    # Assert response structure and values
    assert response.success is True
    assert response.session_id is not None
    assert response.embed_url is not None
    assert response.status == "active"
    assert response.created_at is not None

def test_list_browser_sessions(client):
    """Test listing all browser sessions"""
    # Call the API
    response = list_browser_sessions.sync(client=client)
    
    # Assert response structure
    assert response.success is True
    assert response.sessions is not None
    assert response.count is not None
    assert response.filtered_by is not None

def test_close_browser_session(client, mock_session_id):
    """Test closing a specific browser session"""
    # Call the API
    response = close_browser_session.sync(client=client, session_id=mock_session_id)
    
    # Assert response structure and values
    assert response.success is True
    assert response.session_id == mock_session_id
    assert response.status == "closed"

def test_close_all_browser_sessions(client):
    """Test closing all browser sessions"""
    # Call the API
    response = close_all_browser_sessions.sync(client=client)
    
    # Assert response structure
    assert response.success is True
    assert response.closed_count is not None
    assert response.message is not None

def test_get_browser_context(client, mock_session_id):
    """Test getting the browser context"""
    # Call the API
    response = get_browser_context.sync(client=client, session_id=mock_session_id)
    
    # Assert response structure
    assert response.success is True
    assert response.context is not None

def test_update_session_timeout(client, mock_session_id):
    """Test updating session timeout"""
    # Create request body
    body = UpdateSessionTimeoutBody(timeout=600)
    
    # Call the API
    response = update_session_timeout.sync(
        client=client,
        session_id=mock_session_id,
        body=body
    )
    
    # Assert response structure and values
    assert response.success is True
    assert response.session_id == mock_session_id
    assert response.timeout == 600
