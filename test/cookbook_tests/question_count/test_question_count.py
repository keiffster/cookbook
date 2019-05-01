import unittest
import os

from programytest.client import TestClient


class QuestionCountTestClient(TestClient):

    def __init__(self):
        TestClient.__init__(self)

    def load_storage(self):
        super(QuestionCountTestClient, self).load_storage()
        self.add_default_stores()
        self.add_categories_store([os.path.dirname(__file__)])


class QuestionCountAIMLTests(unittest.TestCase):

    def setUp(self):
        client = QuestionCountTestClient()
        self._client_context = client.create_client_context("testid")

    def test_question_count(self):
        response = self._client_context.bot.ask_question(self._client_context, "ASK QUESTION")
        self.assertIsNotNone(response)
        self.assertEqual(response, "First time.")

        response = self._client_context.bot.ask_question(self._client_context, "ASK QUESTION")
        self.assertIsNotNone(response)
        self.assertEqual(response, "You have asked this question 2 times.")

        response = self._client_context.bot.ask_question(self._client_context, "ASK QUESTION")
        self.assertIsNotNone(response)
        self.assertEqual(response, "You have asked this question 3 times.")

        response = self._client_context.bot.ask_question(self._client_context, "RESET ASK QUESTION")
        self.assertIsNotNone(response)
        self.assertEqual(response, "Count reset.")

        response = self._client_context.bot.ask_question(self._client_context, "ASK QUESTION")
        self.assertIsNotNone(response)
        self.assertEqual(response, "First time.")

