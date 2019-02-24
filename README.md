# UMSL CS5130 Project 1

This program fulfills the requirements for CS5130 Project 1. It implements an arithmetic expression evaluator in Python. When evaluating an expression, the following steps are performed:

1. **Input** - When the program starts, it prompts the user to enter an arithmetic expression as a string. After the program finishes processing one expression, it stops.
2. **Skip Data Validation** - The validation step would be rather complicated. We want to focus the program on the main technical problem. So we'll require the input string to have the following properties:

   - The operands must be non-negative integers.
   - The operators can only be: +, -, \*, /.
   - The delimiters can only be ( and ).
   - The whole input string is a valid arithmetic expression.

3. **Tokenization** - We iterate through the input string character by character, and convert it into a sequence of four token types (`Operand`, `Operator`, `OpeningParen`, `ClosingParen`). Whitespace separators are stripped out. Multi-digit integers are supported.

4. **Postfix Notation Converion** - We convert the sequence of tokens from prefix notation to postfix notation. This makes the evaluation step much easier.

5. **Evaluate Postfix Expression** - We evaluate the postfix expression.

6. **Output** - We output the answer on the screen.

## Requirements

To run this program, you must have python 3.6 installed on your machine. Older and newer versions may work, but only 3.6 has been tested.

## Running

- You can use the included `run` script:
  ```
  chmod +x run
  ./run
  ```
- Alternatively, you can run the `main.py` script directly:
  ```
  python3.6 src/main.py
  ```

## Division By Zero

If you try to evaluate an expression that includes division by zero, the program will exit with a `ZeroDivisionError`. For example:

```
$ ./run
Enter an arithmetic expression: 1 / 0
Traceback (most recent call last):
  File "src/main.py", line 11, in <module>
    result = eval_postfix(postfix_tokens).value
  File "/CS5130/project1/src/postfix_evaluation.py", line 27, in eval_postfix
    res_int = do_eval(first, second, operator)
  File "/CS5130/project1/src/postfix_evaluation.py", line 13, in do_eval
    return first // second
ZeroDivisionError: integer division or modulo by zero
```
