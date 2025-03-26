import pytest
import os
from dotenv import load_dotenv
from aidolon_browser_client.client import AuthenticatedClient

load_dotenv()

API_BASE_URL = os.environ.get('API_BASE_URL', 'http://localhost:3005/api/v1')

@pytest.fixture
def client():
    """Fixture providing a configured AuthenticatedClient instance for tests."""
    return AuthenticatedClient(
        base_url=API_BASE_URL,
        token=os.getenv("API_KEY"),
        raise_on_unexpected_status=True  # Helpful for tests to raise on unexpected responses
    )
