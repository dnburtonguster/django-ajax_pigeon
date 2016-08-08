from django.test import TestCase
from django.core.urlresolvers import resolve
from .forms import PostForm


class HomeViewTest(TestCase):

    def test_index(self):
        """Ensure main url is connected to the talk.views.home view"""
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'talk.views.home')

class FormTest(TestCase):
    def test_valid_form(self):
        """test form with valid data isvalid"""
        form_data = {'3938282828':['3938282828 undefined']}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_form(self):
        form_data = {}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'text': ['This field is required.'],
    })
