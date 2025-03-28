# Aidolon Browser Client Quickstart Tutorial

This guide will walk you through the basics of using the Aidolon Browser Client to automate browser tasks.

## Installation

Install the client library using pip:

```bash
pip install aidolon-browser-client
```

## Authentication

Initialize the client with your API key. You can provide it directly or set it in your environment:

```python
from aidolon_browser_client import AuthenticatedClient

# Option 1: Initialize with explicit API key
client = AuthenticatedClient(
    base_url="https://api.aidolon.com",  # Replace with your API endpoint
    token="your_api_key_here"
)

# Option 2: Initialize using API_KEY from environment
# The client will automatically use this environment variable if set
client = AuthenticatedClient(
    base_url="https://api.aidolon.com"  # Replace with your API endpoint
)
```

## Creating a Browser Session

First, create a new browser session:

```python
from aidolon_browser_client.api.session_management import create_browser_session
from aidolon_browser_client.models import CreateBrowserSessionBody

# Create session request body
session_body = CreateBrowserSessionBody(
    visible=True,  # Make browser visible
    timeout=300    # Session timeout in seconds
)

# Create a new browser session
response = create_browser_session.sync(
    client=client,
    body=session_body
)

# Get the session ID for subsequent operations
session_id = response.session_id
```

## Navigating to a Website

Navigate to Google:

```python
from aidolon_browser_client.api.browser_actions import navigate_browser
from aidolon_browser_client.models import NavigateBrowserBody

# Create navigation request body
navigate_body = NavigateBrowserBody(url="https://www.google.com")

# Navigate to Google
navigate_browser.sync(
    client=client,
    session_id=session_id,
    body=navigate_body
)
```

## Using Selectors

Aidolon Browser Client supports two types of selectors:

### Smart Selectors
Smart Selectors use natural language descriptions that AI can understand:

```python
from aidolon_browser_client.api.browser_actions import type_text, press_key
from aidolon_browser_client.models import TypeTextBody, PressKeyBody

# Type "donuts" into the search bar using a Smart Selector
type_text.sync(
    client=client,
    session_id=session_id,
    body=TypeTextBody(
        selector="the search input",  # Smart Selector - AI understands this!
        text="donuts"
    )
)

# Press Enter to search
press_key.sync(
    client=client,
    session_id=session_id,
    body=PressKeyBody(
        selector="the search input",
        key="Enter"
    )
)
```

### Traditional Selectors
You can also use standard CSS or XPath selectors when you need precise control:

```python
from aidolon_browser_client.api.browser_actions import type_text, click_element
from aidolon_browser_client.models import TypeTextBody, ClickElementBody, ClickElementBodyWait

# Using a CSS selector
type_text.sync(
    client=client,
    session_id=session_id,
    body=TypeTextBody(
        selector="input[name='q']",  # Standard CSS selector
        text="donuts"
    )
)

# Using an XPath selector
click_element.sync(
    client=client,
    session_id=session_id,
    body=ClickElementBody(
        selector="//button[@type='submit']",  # XPath selector
        wait=ClickElementBodyWait.AUTO
    )
)
```

## Waiting and Clicking

Wait for the search results to load, then click the first result:

```python
import time
from aidolon_browser_client.api.browser_actions import click_element
from aidolon_browser_client.models import ClickElementBody, ClickElementBodyWait

# Wait a moment for search results to load
time.sleep(2)

# Click the first search result using a Smart Selector
click_element.sync(
    client=client,
    session_id=session_id,
    body=ClickElementBody(
        selector="the first search result",  # Smart Selector
        wait=ClickElementBodyWait.AUTO  # Wait for navigation to complete
    )
)
```

## Taking Screenshots

Capture what you're seeing:

```python
from aidolon_browser_client.api.content_extraction import take_screenshot
from aidolon_browser_client.models import TakeScreenshotBody

# Take a screenshot
screenshot_response = take_screenshot.sync(
    client=client,
    session_id=session_id,
    body=TakeScreenshotBody(full_page=True)  # Capture the entire page
)

# Save the screenshot
import base64
with open("donut_page.png", "wb") as f:
    f.write(base64.b64decode(screenshot_response.data.image))
    
print(f"Screenshot saved to donut_page.png")
```

## Cleaning Up

Always close your session when finished:

```python
from aidolon_browser_client.api.session_management import close_browser_session

# Always remember to close the session when done
close_browser_session.sync(client=client, session_id=session_id)
```

## Selector Examples

### Smart Selector Examples
Smart Selectors use AI to interpret your intention. Here are some examples:

- `"the search input"` - Finds the main search field
- `"the login button"`- Finds the login button
- `"the first search result"` - Finds the first result in a list
- `"the shopping cart icon"` - Finds the cart icon
- `"the email field in the contact form"` - Finds a specific field in a form
- `"the Submit button at the bottom of the page"` - Finds a button with location context

### Traditional Selector Examples
You can also use precise CSS and XPath selectors:

- CSS: `"input[name='q']"` - Selects an input with name attribute 'q'
- CSS: `"button.primary"` - Selects buttons with class 'primary'
- CSS: `"#login-form"` - Selects element with ID 'login-form'
- XPath: `"//div[contains(@class, 'result')][1]"` - First div with 'result' in its class
- XPath: `"//button[text()='Submit']"` - Button with text 'Submit'

## Best Practices

1. Always close your sessions when done to avoid resource leaks
2. Choose the right selector for your needs:
   - Smart Selectors for convenience and readability
   - Traditional selectors for precision when needed
3. Consider using `wait` options after clicks that trigger navigation 
4. Handle potential errors with try/except blocks
5. Use descriptive Smart Selectors that uniquely identify elements

## Troubleshooting

If you encounter issues:
1. Check that your API key is valid or properly set in your environment
2. Verify your session hasn't timed out
3. Selector problems:
   - If Smart Selectors aren't working well, try more specific descriptions
   - Fall back to traditional CSS/XPath selectors for precise targeting
4. Review the documentation for correct parameter usage
5. Use the scrape_page API to help debug what the browser is seeing