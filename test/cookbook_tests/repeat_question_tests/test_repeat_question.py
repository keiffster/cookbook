import unittest
import os

from programytest.client import TestClient


class RepeatQuestionTestClient(TestClient):

    def __init__(self):
        TestClient.__init__(self)

    def load_storage(self):
        super(RepeatQuestionTestClient, self).load_storage()
        self.add_default_stores()
        self.add_categories_store([os.path.dirname(__file__)])


class RepeatQuestionAIMLTests(unittest.TestCase):

    def setUp(self):
        client = RepeatQuestionTestClient()
        self._client_context = client.create_client_context("testid")

    def test_repeat_question(self):
        response = self._client_context.bot.ask_question(self._client_context, "SHOULD I TAKE AN UMBRELLA TODAY")
        self.assertIsNotNone(response)
        self.assertIn(response, ["YES.", "NO."])
