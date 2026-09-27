import unittest

from chatbot import respond


class ChatbotTests(unittest.TestCase):
    def test_empty_message(self):
        self.assertIn("Escreva", respond("  "))

    def test_programming_topic(self):
        self.assertIn("programação", respond("Estou aprendendo PYTHON"))

    def test_fallback(self):
        self.assertIn("reformular", respond("assunto desconhecido"))


if __name__ == "__main__":
    unittest.main()
