import unittest

from expression_tokenizer import tokenize_expression, stringify_tokens, Token
from notation_conversion import infix_to_postfix
from postfix_evaluation import eval_postfix


def parse_and_eval(infix_expression):
    return eval_postfix(infix_to_postfix(tokenize_expression(infix_expression)))


class TestInfixToPostfix(unittest.TestCase):

    def test_one(self):
        expression = '21+91372-4'

        actual = parse_and_eval(expression).value
        expected = 91389

        self.assertEqual(actual, expected)

    def test_two(self):
        expression = '21*91372/4'

        actual = parse_and_eval(expression).value
        expected = 479703

        self.assertEqual(actual, expected)

    def test_three(self):
        expression = '21+91372*4'

        actual = parse_and_eval(expression).value
        expected = 365509

        self.assertEqual(actual, expected)

    def test_four(self):
        expression = '21*91372+4'

        actual = parse_and_eval(expression).value
        expected = 1918816

        self.assertEqual(actual, expected)

    def test_five(self):
        expression = '21*(91372+4)'

        actual = parse_and_eval(expression).value
        expected = 1918896

        self.assertEqual(actual, expected)

    def test_six(self):
        expression = '(21+91372)*(4-56)'

        actual = parse_and_eval(expression).value
        expected = -4752436

        self.assertEqual(actual, expected)

    def test_seven(self):
        expression = '(21+91372)*4-56'

        actual = parse_and_eval(expression).value
        expected = 365516

        self.assertEqual(actual, expected)

    def test_eight(self):
        expression = '21+91372*(4-56/(1+99))'

        actual = parse_and_eval(expression).value
        expected = 365509

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
