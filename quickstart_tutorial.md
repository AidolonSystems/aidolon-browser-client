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
# browser = BrowserSession(api_key="your_api_key_here")

# You can also use the context manager to ensure proper cleanup
with BrowserSession() as browser:
    # Your browser automation code here
    pass
```

## 3. Navigating to a Website

Navigate to Google using the `navigate` method:

```python
# Navigate to Google using a full URL
browser.navigate("https://www.google.com")

# Or use smart URLs with plain language (AI-powered)
browser.navigate("google")
```

Aidolon browser features smart URLs that understand plain language. You can simply specify the name of the website you want to visit, and the AI will interpret your intent. Standard URLs will always work precisely as expected, while smart URLs provide convenience at the cost of a small amount of AI credits.

## 4. Interacting with Page Elements

Search for "donuts" on Google:

```python
# Type "donuts" in the search box using a CSS selector
browser.type("input[name='q']", "donuts")

# Or use smart selectors with plain language (AI-powered)
browser.type("the search box", "donuts")

# Press Enter to submit the search
browser.press("input[name='q']", "Enter")

# Or use natural language for keys
browser.press("the search box", "return")  # "enter", "return", etc. all work
```

Aidolon browser supports smart selectors that understand plain language descriptions of elements. Instead of writing complex CSS selectors, you can describe what you're looking for, such as "the search box" or "the submit button," and the AI will find the appropriate element.

Traditional CSS and XPath selectors still work perfectly when you need precision or have existing selectors. Smart selectors use AI credits, though the calls are efficient and the cost per selector is minimal.

The `press` function also accepts natural language key names like "delete", "del", "ctrl", "control", "enter", or "return" - the AI understands what you mean.

## 5. Smart Arguments - AI-Powered Interactions

Aidolon Browser Client leverages AI to understand natural language across all its functions:

- **Smart URLs**: Navigate to websites using plain language
  ```python
  browser.navigate("amazon")  # AI understands you want to go to Amazon
  browser.navigate("news about technology")  # Finds relevant news site
  ```

- **Smart Selectors**: Describe elements instead of providing technical selectors
  ```python
  browser.click("login button")  # Finds and clicks the login button
  browser.type("username field", "myusername")  # Finds the username input
  ```

- **Smart Key Commands**: Use intuitive key names
  ```python
  browser.press("search box", "enter")  # Press Enter key
  browser.press("text field", "shift+tab")  # Press key combinations
  ```

- **Smart Content Extraction**: Describe what information you need
  ```python
  browser.scrape_information("product prices and ratings")  # Extract specific data
  ```

This natural language capability makes browser automation accessible without needing to know complex CSS selectors or exact DOM structures.

## 6. Taking a Screenshot

Capture a screenshot of the search results:

```python
# Take a screenshot of the entire page
browser.take_screenshot(full_page=True)
```

## 7. Closing the Browser Session

Close the session to release resources:

```python
# Close the browser session when done
browser.close_session()
```

## Complete Example

Here's a complete script that performs all the steps above using smart arguments:

```python
import os
from dotenv import load_dotenv
from aidolon_browser_client.browser.browser_session import BrowserSession

# Load environment variables
load_dotenv()

# Using the context manager (recommended)
with BrowserSession() as browser:
    # Navigate to Google using smart URL
    browser.navigate("google")
    
    # Search for donuts using smart selectors
    browser.type("the search box", "donuts")
    browser.press("the search box", "enter")
    
    # Take a screenshot
    screenshot_result = browser.take_screenshot(full_page=True)
    print(f"Screenshot taken. URL: {screenshot_result.get('data', {}).get('screenshot_url')}")
    
    # The browser session is automatically closed when exiting the with block
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
3. Ensure your selectors or descriptions are clear
4. Try using more specific language if smart selectors aren't finding the right elements
