from uuid import UUID
from typing import Optional, Union

from aidolon_browser_client import AuthenticatedClient
from aidolon_browser_client.api.session_management import (
    create_browser_session,
    close_browser_session
)
from aidolon_browser_client.api.browser_actions import (
    click_element,
    type_text,
    navigate_browser,
    press_key
)
from aidolon_browser_client.models import (
    CreateBrowserSessionBody,
    ClickElementBody,
    ClickElementBodyWait,
    TypeTextBody,
    NavigateBrowserBody,
    PressKeyBody
)
from aidolon_browser_client.models.error import Error

class BrowserSession:
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://api.aidolon.com"):
        """Initialize a browser session with Aidolon.
        
        Args:
            api_key: API key for Aidolon. If None, will try to get from environment variable.
            base_url: Base URL for Aidolon API.
        """
        self.client = AuthenticatedClient(base_url=base_url, token=api_key) if api_key else AuthenticatedClient(base_url=base_url)
        self.session_id = None
        
        # Create a browser session
        session_body = CreateBrowserSessionBody(
            visible=True,
            timeout=300
        )
        
        response = create_browser_session.sync(
            client=self.client,
            body=session_body
        )
        
        if hasattr(response, 'session_id'):
            self.session_id = response.session_id
            print("Browser session started.")
        else:
            raise Exception("Failed to create browser session.")
    
    def click(self, selector: str, wait: str = "auto"):
        """Click on an element in the browser.
        
        Args:
            selector: CSS selector, XPath, or natural language description.
            wait: Wait strategy ("auto", "navigation", "load", "domcontentloaded", "networkidle").
        """
        if not self.session_id:
            raise Exception("No active browser session.")
            
        wait_enum = getattr(ClickElementBodyWait, wait.upper(), ClickElementBodyWait.AUTO)
        
        click_body = ClickElementBody(
            selector=selector,
            wait=wait_enum
        )
        
        response = click_element.sync(
            client=self.client,
            session_id=self.session_id,
            body=click_body
        )
        
        print("Browser clicked.")
        return response
    
    def navigate(self, url: str):
        """Navigate to a specific URL.
        
        Args:
            url: URL to navigate to.
        """
        if not self.session_id:
            raise Exception("No active browser session.")
            
        navigate_body = NavigateBrowserBody(url=url)
        
        response = navigate_browser.sync(
            client=self.client,
            session_id=self.session_id,
            body=navigate_body
        )
        
        print(f"Navigated to {url}")
        return response
    
    def type(self, selector: str, text: str):
        """Type text into an element.
        
        Args:
            selector: CSS selector, XPath, or natural language description.
            text: Text to type.
        """
        if not self.session_id:
            raise Exception("No active browser session.")
            
        type_body = TypeTextBody(
            selector=selector,
            text=text
        )
        
        response = type_text.sync(
            client=self.client,
            session_id=self.session_id,
            body=type_body
        )
        
        print(f"Typed text: {text}")
        return response
    
    def press(self, selector: str, key: str):
        """Press a key on an element.
        
        Args:
            selector: CSS selector, XPath, or natural language description.
            key: Key to press (e.g., "Enter", "Tab").
        """
        if not self.session_id:
            raise Exception("No active browser session.")
            
        press_body = PressKeyBody(
            selector=selector,
            key=key
        )
        
        response = press_key.sync(
            client=self.client,
            session_id=self.session_id,
            body=press_body
        )
        
        print(f"Pressed key: {key}")
        return response
    
    def close_session(self):
        """Close the browser session and release resources."""
        if not self.session_id:
            print("No active browser session to close.")
            return
            
        response = close_browser_session.sync(
            client=self.client,
            session_id=self.session_id
        )
        
        self.session_id = None
        print("Browser session closed.")
        return response
    
    def __enter__(self):
        """Return self to allow access to instance methods inside the with block."""
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Ensure that the session is closed when exiting the with block."""
        self.close_session()


def create_session(api_key: Optional[str] = None, base_url: str = "https://api.aidolon.com"):
    """Create a new browser session.
    
    Args:
        api_key: API key for Aidolon. If None, will try to get from environment variable.
        base_url: Base URL for Aidolon API.
    
    Returns:
        BrowserSession object.
    """
    return BrowserSession(api_key=api_key, base_url=base_url)