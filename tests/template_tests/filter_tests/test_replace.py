from datetime import date, timedelta

from django.template.defaultfilters import replace
from django.test import SimpleTestCase

from ..utils import setup


class ReplaceTests(SimpleTestCase):

    @setup({'replace01': '{{ i|replace:arg }}'})
    def test_replace01(self):
        output = self.engine.render_to_string('replace01', {'i': 'Lorem ipsum dolor sit amet.', 'arg': (' ', '_', 2) })
        self.assertEqual(output, 'Lorem_ipsum_dolor sit amet.')

    @setup({'replace02': '{{ i|replace:arg }}'})
    def test_replace02(self):
        output = self.engine.render_to_string('replace02', {'i': 'Lorem ipsum dolor sit amet.', 'arg': (' ', '_')})
        self.assertEqual(output, 'Lorem_ipsum_dolor_sit_amet.')

    @setup({'replace03': '{{ i|replace:arg }}'})
    def test_replace03(self):
        output = self.engine.render_to_string('replace03', {'i': 'Lorem ipsum dolor sit amet.', 'arg': ('no_match', 'replace_this')})
        self.assertEqual(output, 'Lorem ipsum dolor sit amet.')

    @setup({'replace04': '{{ i|replace:arg }}'})
    def test_replace04(self):
        output = self.engine.render_to_string('replace04', {'i': 'Lorem ipsum dolor sit amet.', 'arg': ['i', '*']})
        self.assertEqual(output, 'Lorem *psum dolor s*t amet.')


class FunctionTests(SimpleTestCase):

    def test_replace(self):
        self.assertEqual(replace('Lorem ipsum dolor sit amet.', (' ', '_')), 'Lorem_ipsum_dolor_sit_amet.')
