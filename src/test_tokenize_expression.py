import unittest

from expression_tokenizer import tokenize_expression, stringify_tokens, Token


class TestStringifyTokens(unittest.TestCase):

    def test_one(self):
        tokens = [
            Token.OpeningParen(),
            Token.Operand(21),
            Token.Operator('*'),
            Token.Operand(2139),
            Token.ClosingParen(),
            Token.Operator('-'),
            Token.Operand(416),
        ]

        actual = stringify_tokens(tokens)
        expected = '(21*2139)-416'

        self.assertEqual(actual, expected)


class TestTokenizeExpression(unittest.TestCase):

    def test_one(self):
        expression = '1 + 2'

        actual = stringify_tokens(tokenize_expression(expression))
        expected = '1+2'

        self.assertEqual(actual, expected)

    def test_two(self):
        expression = '((42) + 21 - (96 * 32) / 4998673)'

        actual = stringify_tokens(tokenize_expression(expression))
        expected = '((42)+21-(96*32)/4998673)'

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
