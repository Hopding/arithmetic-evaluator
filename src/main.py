# pylint: disable=import-error
from expression_tokenizer import tokenize_expression, stringify_tokens, Token
from notation_conversion import infix_to_postfix
from postfix_evaluation import eval_postfix

s = '( 1+213 - (325 +2))'

infix_tokens = tokenize_expression(s)
postfix_tokens = infix_to_postfix(infix_tokens)

print('Infix:')
print(stringify_tokens(infix_tokens))

print()
print('Postfix:')
print(stringify_tokens(postfix_tokens, delim=' '))

print()
print('Result:')
print(eval_postfix(postfix_tokens).value)
