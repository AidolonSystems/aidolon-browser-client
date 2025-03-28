# Quickstart Guide for Aidolon Browser Client

This guide will help you get started with the Aidolon Browser Client, a powerful tool for automating browser interactions. By the end of this tutorial, you'll learn how to set up your environment, create a browser session, navigate to websites, interact with page elements, and capture screenshots.

## Prerequisites

- Python 3.7 or later
- Aidolon API key (obtain from your Aidolon account)

## Installation

Install the Aidolon Browser Client using pip:

```bash
pip install aidolon-browser-client
```

## 1. Setting Up the Environment

Create a `.env` file in your project's root directory with your Aidolon API credentials:

```bash
# .env file
AIDOLONS_API_KEY=your_api_key_here
AIDOLONS_API_BASE_URL=https://api.aidolon.com
```

Load these environment variables in your Python script:

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
```

## 2. Creating a Browser Session

Import the `BrowserSession` class and create a new browser session:

```python
from aidolon_browser_client.browser.browser_session import BrowserSession

# Create a new browser session
# If API key is not provided, it will be read from environment variables
browser = BrowserSession()

# Alternatively, provide API key and base URL explicitly
# browser = BrowserSession(api_key="your_api_key_here", base_url="https://api.aidolon.com")

# You can also use the context manager to ensure proper cleanup
with BrowserSession() as browser:
    # Your browser automation code here
    pass
```

## 3. Navigating to a Website

Navigate to Google using the `navigate` method:

```python
# Navigate to Google
browser.navigate("https://www.google.com")
```

## 4. Interacting with Page Elements

Search for "donuts" on Google:

```python
# Type "donuts" in the search box
# The CSS selector targets Google's search input field
browser.type("input[name='q']", "donuts")

# Press Enter to submit the search
browser.press("input[name='q']", "Enter")
```

## 5. Taking a Screenshot

Capture a screenshot of the search results:

```python
# Take a screenshot of the entire page
browser.take_screenshot(full_page=True)
```

## 6. Closing the Browser Session

Close the session to release resources:

```python
# Close the browser session when done
browser.close_session()
```

## Complete Example

Here's a complete script that performs all the steps above:

```python
import os
from dotenv import load_dotenv
from aidolon_browser_client.browser.browser_session import BrowserSession

# Load environment variables
load_dotenv()

# Method 1: Using the context manager (recommended)
with BrowserSession() as browser:
    # Navigate to Google
    browser.navigate("https://www.google.com")
    
    # Search for donuts
    browser.type("input[name='q']", "donuts")
    browser.press("input[name='q']", "Enter")
    
    # Take a screenshot
    screenshot_result = browser.take_screenshot(full_page=True)
    print(f"Screenshot taken. URL: {screenshot_result.get('data', {}).get('screenshot_url')}")

# Method 2: Manual session management
browser = BrowserSession()
try:
    # Navigate to Google
    browser.navigate("https://www.google.com")
    
    # Search for donuts
    browser.type("input[name='q']", "donuts")
    browser.press("input[name='q']", "Enter")
    
    # Take a screenshot
    screenshot_result = browser.take_screenshot(full_page=True)
    print(f"Screenshot taken. URL: {screenshot_result.get('data', {}).get('screenshot_url')}")
finally:
    # Always close the session when done
    browser.close_session()
```

## Additional Features

The Aidolon Browser Client offers many more features beyond this basic example:

- Clicking on elements: `browser.click("selector")`
- Dragging and dropping elements: `browser.drag_and_drop("source_selector", "target_selector")`
- Generating PDFs: `browser.generate_pdf()`
- Scraping page content: `browser.scrape_page()`
- Extracting specific information: `browser.scrape_information("description of what to extract")`

## Best Practices

1. Always close browser sessions when you're done with them
2. Use the context manager pattern (`with` statement) when possible
3. Handle exceptions appropriately to ensure resources are cleaned up
4. Store sensitive information like API keys in environment variables
5. Implement appropriate waiting strategies when interacting with dynamic web content

## Troubleshooting

If you encounter issues:

1. Verify your API key is correct
2. Check your network connection
3. Ensure you're using the correct selectors for page elements
4. Review the Aidolon documentation for any API changes

For more detailed information, refer to the official Aidolon documentation.
