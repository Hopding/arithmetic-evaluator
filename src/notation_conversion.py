from tokenize_expression import Token


def is_low_precedence(op): op.value == '+' or op.value == '-'


def is_high_precedence(op): op.value == '*' or op.value == '/'


def is_lower_precedence(first_op, second_op):
    return is_low_precedence(first_op) and is_high_precedence(second_op)


def infix_to_postfix(infix_tokens):
    postfix_tokens = []
    token_stack = []

    for token in infix_tokens:
        if isinstance(token, Token.Operand):
            postfix_tokens.append(token)
        elif isinstance(token, Token.OpeningParen):
            token_stack.append(token)
        elif isinstance(token, Token.ClosingParen):
            while True:
                item = token_stack.pop()
                if isinstance(item, Token.OpeningParen):
                    break
                else:
                    postfix_tokens.append(item)
        elif isinstance(token, Token.Operator):
            curr_op = token
            if len(token_stack) == 0:
                token_stack.append(token)
            else:
                while len(token_stack) != 0:
                    item = token_stack.pop()
                    if isinstance(item, Token.OpeningParen):
                        token_stack.append(item)
                        break
                    elif isinstance(item, Token.Operator):
                        op_top = item
                        if is_lower_precedence(op_top, curr_op):
                            token_stack.append(op_top)
                            break
                        else:
                            postfix_tokens.append(op_top)
                token_stack.append(curr_op)

    for token in token_stack:
        postfix_tokens.append(token)

    return postfix_tokens
