from selenium import webdriver

# Start a selenium webdriver to pop up a real Firefox browser window
browser = webdriver.Firefox()
# Use the webdriver to open a local webpage
browser.get('http://localhost:8000')

# Test assertion that 'Django' is in the title
assert 'Django' in browser.title