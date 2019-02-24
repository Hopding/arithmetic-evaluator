import unittest

# pylint: disable=import-error
from expression_tokenizer import tokenize_expression, stringify_tokens, Token
from notation_conversion import infix_to_postfix, is_lower_precedence


def parse_infix_to_postfix(infix_expression):
    tokens = tokenize_expression(infix_expression)
    return stringify_tokens(infix_to_postfix(tokens), delim=' ')


class TestIsLowerPrecedence(unittest.TestCase):

    def test_one(self):
        first = Token.Operator('+')
        second = Token.Operator('-')

        actual = is_lower_precedence(first, second)
        expected = False

        self.assertEqual(actual, expected)

    def test_two(self):
        first = Token.Operator('+')
        second = Token.Operator('*')

        actual = is_lower_precedence(first, second)
        expected = True

        self.assertEqual(actual, expected)

    def test_three(self):
        first = Token.Operator('*')
        second = Token.Operator('+')

        actual = is_lower_precedence(first, second)
        expected = False

        self.assertEqual(actual, expected)


class TestInfixToPostfix(unittest.TestCase):

    def test_one(self):
        expression = '21+91372-4'

        actual = parse_infix_to_postfix(expression)
        expected = '21 91372 + 4 - '

        self.assertEqual(actual, expected)

    def test_two(self):
        expression = '21*91372/4'

        actual = parse_infix_to_postfix(expression)
        expected = '21 91372 * 4 / '

        self.assertEqual(actual, expected)

    def test_three(self):
        expression = '21+91372*4'

        actual = parse_infix_to_postfix(expression)
        expected = '21 91372 4 * + '

        self.assertEqual(actual, expected)

    def test_four(self):
        expression = '21*91372+4'

        actual = parse_infix_to_postfix(expression)
        expected = '21 91372 * 4 + '

        self.assertEqual(actual, expected)

    def test_five(self):
        expression = '21*(91372+4)'

        actual = parse_infix_to_postfix(expression)
        expected = '21 91372 4 + * '

        self.assertEqual(actual, expected)

    def test_six(self):
        expression = '(21+91372)*(4-56)'

        actual = parse_infix_to_postfix(expression)
        expected = '21 91372 + 4 56 - * '

        self.assertEqual(actual, expected)

    def test_seven(self):
        expression = '(21+91372)*4-56'

        actual = parse_infix_to_postfix(expression)
        expected = '21 91372 + 4 * 56 - '

        self.assertEqual(actual, expected)

    def test_eight(self):
        expression = '21+91372*(4-56/(1+99))'

        actual = parse_infix_to_postfix(expression)
        expected = '21 91372 4 56 1 99 + / - * + '

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
