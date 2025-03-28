from aidolons.browser import create_session

# Example 1: Using the session without a with block
browser = create_session()
browser.navigate("https://www.google.com")
browser.type("the search input", "donuts")
browser.press("the search input", "Enter")
browser.click("the first search result")
browser.close_session()

print("-----")

# Example 2: Using the session with a with block
with create_session() as browser:
    browser.navigate("https://www.google.com")
    browser.type("the search input", "donuts")
    browser.press("the search input", "Enter")
    browser.click("the first search result")