# pylint: disable=import-error
from expression_tokenizer import Token


def do_eval(first, second, operator):
    if operator == '+':
        return first + second
    elif operator == '-':
        return first - second
    elif operator == '*':
        return first * second
    elif operator == '/':
        return first // second


def eval_postfix(postfix_tokens):
    operand_stack = []

    for token in postfix_tokens:
        if isinstance(token, Token.Operand):
            operand_stack.append(token)
        elif isinstance(token, Token.Operator):
            operator = token.value
            second = operand_stack.pop().value
            first = operand_stack.pop().value

            res_int = do_eval(first, second, operator)
            res_token = Token.Operand(res_int)

            operand_stack.append(res_token)

    return operand_stack.pop()
