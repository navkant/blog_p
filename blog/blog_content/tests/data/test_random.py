from django.test.testcases import TestCase, SimpleTestCase


class FirstDjangoTest(TestCase):
    def setUp(self):
        pass

    def test_assertion(self):
        self.assertEquals(1, 1)