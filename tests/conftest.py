import pytest
from aidolon_browser_client.client import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_BASE_URL = os.environ.get('API_BASE_URL', 'http://localhost:3005/api/v1')

@pytest.fixture
def client():
    """Fixture providing a configured Client instance for tests."""
    return Client(
        base_url=API_BASE_URL, 
        raise_on_unexpected_status=True  # Helpful for tests to raise on unexpected responses
    )
import pytest
import os
from aidolon_browser_client.client import AuthenticatedClient

@pytest.fixture
def client():
    """Fixture providing a configured AuthenticatedClient instance for tests."""
    # You can set API_KEY in your environment or provide it directly here
    return AuthenticatedClient(
        base_url=API_BASE_URL,  # Use an appropriate URL for testing
        token=os.getenv("API_KEY"),  # Will read from environment or can be passed directly
        raise_on_unexpected_status=True  # Helpful for tests to raise on unexpected responses
    )
