# pylint: disable=import-error
from expression_tokenizer import tokenize_expression, stringify_tokens, Token
from notation_conversion import infix_to_postfix
from postfix_evaluation import eval_postfix


expression = input('Enter an arithmetic expression: ')

infix_tokens = tokenize_expression(expression)
postfix_tokens = infix_to_postfix(infix_tokens)
result = eval_postfix(postfix_tokens).value

print(result)
