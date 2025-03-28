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
from aidolon_browser_client import Client

# Option 1: Initialize with explicit API key
client = Client(api_key="your_api_key_here")

# Option 2: Initialize using AIDOLONS_API_KEY from .env file
# The client will automatically use this environment variable if set
client = Client()
```

## Creating a Browser Session

First, create a new browser session:

```python
# Create a new browser session
session = client.create_browser_session(
    visible=True,  # Make browser visible
    timeout=300    # Session timeout in seconds
)

# Get the session ID for subsequent operations
session_id = session["session_id"]
```

## Navigating to a Website

Navigate to Google:

```python
# Navigate to Google
client.navigate(
    session_id=session_id,
    url="https://www.google.com"
)
```

## Using Selectors

Aidolon Browser Client supports two types of selectors:

### Smart Selectors
Smart Selectors use natural language descriptions that AI can understand:

```python
# Type "donuts" into the search bar using a Smart Selector
client.type_text(
    session_id=session_id,
    selector="the search input",  # Smart Selector - AI understands this!
    text="donuts"
)

# Press Enter to search
client.press_key(
    session_id=session_id,
    key="Enter"
)
```

### Traditional Selectors
You can also use standard CSS or XPath selectors when you need precise control:

```python
# Using a CSS selector
client.type_text(
    session_id=session_id,
    selector="input[name='q']",  # Standard CSS selector
    text="donuts"
)

# Using an XPath selector
client.click(
    session_id=session_id,
    selector="//button[@type='submit']",  # XPath selector
    wait=True
)
```

## Waiting and Clicking

Wait for the search results to load, then click the first result:

```python
# Wait a moment for search results to load
import time
time.sleep(2)

# Click the first search result using a Smart Selector
client.click(
    session_id=session_id,
    selector="the first search result",  # Smart Selector
    wait=True  # Wait for navigation to complete
)
```

## Taking Screenshots

Capture what you're seeing:

```python
# Take a screenshot
screenshot = client.take_screenshot(
    session_id=session_id,
    full_page=True  # Capture the entire page
)

# Save the screenshot
import base64
with open("donut_page.png", "wb") as f:
    f.write(base64.b64decode(screenshot["data"]["image"]))
    
print(f"Screenshot saved to donut_page.png")
```

## Cleaning Up

Always close your session when finished:

```python
# Always remember to close the session when done
client.close_session(session_id=session_id)
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
3. Consider using `wait=True` after clicks that trigger navigation 
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
5. Use `client.scrape_page()` to help debug what the browser is seeing