from tokenize_expression import tokenize_expression, stringify_tokens, Token  # pylint: disable=import-error

s = '( 1+213 - (325 +2))'

tokens = tokenize_expression(s)

print(stringify_tokens(tokens))
