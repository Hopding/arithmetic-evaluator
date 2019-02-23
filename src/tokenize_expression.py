from tokenize import tokenize, NUMBER, OP
from io import BytesIO


class _Operand:
    def __init__(self, number):
        self.value = int(number)


class _Operator:
    def __init__(self, operator):
        self.value = operator


class _OpeningParen:
    pass


class _ClosingParen:
    pass


class Token():
    Operand = _Operand
    Operator = _Operator
    OpeningParen = _OpeningParen
    ClosingParen = _ClosingParen


def tokenize_expression(expression_string):
    raw_tokens = tokenize(BytesIO(expression_string.encode('utf-8')).readline)

    tokens = []
    for raw_token in raw_tokens:
        if raw_token.type == NUMBER:
            tokens.append(Token.Operand(raw_token.string))
        elif raw_token.type == OP and raw_token.string == '(':
            tokens.append(Token.OpeningParen())
        elif raw_token.type == OP and raw_token.string == ')':
            tokens.append(Token.ClosingParen())
        elif raw_token.type == OP:
            tokens.append(Token.Operator(raw_token.string))

    return list(tokens)


def stringify_tokens(tokens):
    string = ''

    for token in tokens:
        if isinstance(token, Token.OpeningParen):
            string += '('
        if isinstance(token, Token.ClosingParen):
            string += ')'
        if isinstance(token, Token.Operand):
            string += str(token.value)
        if isinstance(token, Token.Operator):
            string += token.value

    return string
