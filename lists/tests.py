from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page # View function that return the HTML we want.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		# Django uses resolve() to resolve URLs and find what view function they should map to.
		found = resolve('/')
		# Checking tht resolve(), when called with the root of the site, finds a function called home_page
		self.assertEqual(found.func, home_page)

#class SmokeTest(TestCase):
#
#	def test_bad_maths(self):
#		self.assertEqual(1 + 1, 3)
