from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		# Start a selenium webdriver to pop up a real Firefox browser window
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3) # Waits up to 3 sec if needed for the page to complete loading

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrive_it_later(self):
		# Use the webdriver to open a local webpage
		self.browser.get('http://localhost:8000')

		# Test assertion that 'To-Do' is in the title
		self.assertIn('To-Do', self.browser.title) #
		#self.fail('Finish the test!') # Fails no matter what. Used as a reminder to finish the test.

		# Enter a todo item

		# Typing "Buy peacock feathers" into a text box

		# Hitting enter, the page updates and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list

		# There is still a text box inviting to add another item.
		# Entering "Use peacock feathers to make a fly"

		# The page updates again and now shows both items on the list

if __name__ == '__main__':
	unittest.main()

