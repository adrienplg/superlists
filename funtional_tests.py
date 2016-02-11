from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

		# Test assertion that 'To-Do' is in the title and the main header
		self.assertIn('To-Do', self.browser.title) #
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# Invited to enter a new element right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# Typing "Buy peacock feathers" into a text box
		inputbox.send_keys('Buy peacock feathers')

		# Hitting enter, the page updates and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)

		# There is still a text box inviting to add another item.
		# Entering "Use peacock feathers to make a fly"

		# The page updates again and now shows both items on the list

		self.fail('Finish the test!') # Fails no matter what. Used as a reminder to finish the test.

if __name__ == '__main__':
	unittest.main()

