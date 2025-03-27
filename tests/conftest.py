import os
import pytest
from uuid import UUID
from aidolon_browser_client.client import AuthenticatedClient

# Set default base URL if environment variable is not set
BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:3005")

@pytest.fixture
def mock_session_id():
    """Return a consistent mock session ID for testing"""
    return UUID("11111111-1111-1111-1111-111111111111")

@pytest.fixture
def client():
    """Return an authenticated client with the mock API key"""
    return AuthenticatedClient(
        base_url=BASE_URL,
        token="give-me-mock-data",
        headers={"Content-Type": "application/json"}
    )
