import unittest
import os
import time

from programytest.client import TestClient


class ReturnTimeTestClient(TestClient):

    def __init__(self):
        TestClient.__init__(self)

    def load_storage(self):
        super(ReturnTimeTestClient, self).load_storage()
        self.add_default_stores()
        self.add_categories_store([os.path.dirname(__file__)])


class ReturnTimeAIMLTests(unittest.TestCase):

    def setUp(self):
        client = ReturnTimeTestClient()
        self._client_context = client.create_client_context("testid")

    def test_return_timeom(self):

        response = self._client_context.bot.ask_question(self._client_context, "RETURN TIME")
        self.assertIsNotNone(response)
        self.assertEqual(response, "First time you asked this question.")

        time.sleep(2)

        response = self._client_context.bot.ask_question(self._client_context, "RETURN TIME")
        self.assertIsNotNone(response)
        self.assertEqual(response, "You asked this question 2 seconds before.")

        time.sleep(3)

        response = self._client_context.bot.ask_question(self._client_context, "RETURN TIME")
        self.assertIsNotNone(response)
        self.assertEqual(response, "You asked this question 5 seconds before.")
