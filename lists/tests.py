from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page # View function that return the HTML we want.
from lists.models import Item

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		# Django uses resolve() to resolve URLs and find what view function they should map to.
		found = resolve('/')
		# Checking tht resolve(), when called with the root of the site, finds a function called home_page
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_hmtl(self):
		request = HttpRequest() # Create an HttpRequest object, which is what Django will see when a browser asks for a page.
		response = home_page(request) # Pass is to our home_page view, giving back an HttpResponse
		# Supply the request object so that the context processors run, therefore resolving elements like {% csrf_token %}
		expected_html = render_to_string('home.html', request=request)
		self.assertEqual(response.content.decode(), expected_html)

	def test_home_page_can_save_a_POST_request(self):
		# Setup the test
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		# Exercise
		response = home_page(request)

		# Assert
		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'home.html', 
			{'new_item_text': 'A new list item'},
			request=request
		)
		self.assertEqual(response.content.decode(), expected_html)

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()

		saved_items = Item.objects.all() # Return a list like object called a QuerySet
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(second_saved_item.text, 'Item the second')
		