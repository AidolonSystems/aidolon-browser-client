import pytest
from aidolon_browser_client.api.session_management import get_session_status

def test_get_session_status(client, mock_session_id):
    """Test getting the status of a browser session"""
    # Call the API
    response = get_session_status.sync(client=client, session_id=mock_session_id)
    
    # Assert response structure and values
    assert response.success is True
    assert response.session_id == mock_session_id
    assert response.status is not None  # The status can vary but should exist
    assert response.created_at is not None
    
    # Check for live_session information if the session is active
    if response.status == "active":
        assert response.live_session is not None
