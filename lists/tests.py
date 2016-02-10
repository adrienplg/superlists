from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page # View function that return the HTML we want.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		# Django uses resolve() to resolve URLs and find what view function they should map to.
		found = resolve('/')
		# Checking tht resolve(), when called with the root of the site, finds a function called home_page
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_hmtl(self):
		request = HttpRequest() # Create an HttpRequest object, which is what Django will see when a browser asks for a page.
		response = home_page(request) # Pass is to our home_page view, giving back an HttpResponse
		self.assertTrue(response.content.startswith(b'<html>')) # Using 'b' because response.content is raw bytes, not a Python string
		self.assertIn(b'<title>To-Do lists</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))