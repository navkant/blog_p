from django.test.testcases import TestCase, SimpleTestCase
import  time

class FirstDjangoTest(TestCase):
    def setUp(self):
        pass

    def test_assertion(self):
        time.sleep(60)
        self.assertEquals(1, 1)