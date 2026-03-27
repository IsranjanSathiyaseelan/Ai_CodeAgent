class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": self.safe_divide
        }
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    def safe_divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def evaluate(self, expression):
        if not expression or expression.isspace():
            raise ValueError("Empty expression")
        tokens = self.tokenize(expression)
        return self._evaluate_infix(tokens)

    def tokenize(self, expr):
        """Convert string expression into list of numbers, operators, parentheses"""
        tokens = []
        number = ""
        for char in expr:
            if char.isdigit() or char == ".":
                number += char
            elif char in self.operators or char in "()":
                if number:
                    tokens.append(number)
                    number = ""
                tokens.append(char)
            elif char.isspace():
                if number:
                    tokens.append(number)
                    number = ""
            else:
                raise SyntaxError(f"Invalid character '{char}'")
        if number:
            tokens.append(number)
        return tokens

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        def apply_operator():
            op = operators.pop()
            if len(values) < 2:
                raise ValueError(f"Not enough operands for operator {op}")
            b = values.pop()
            a = values.pop()
            values.append(self.operators[op](a, b))

        def precedence(op):
            return self.precedence[op]

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.replace('.', '', 1).isdigit():
                values.append(float(token) if '.' in token else int(token))
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    apply_operator()
                if not operators:
                    raise SyntaxError("Mismatched parentheses")
                operators.pop()  # remove '('
            elif token in self.operators:
                while (operators and operators[-1] in self.operators and
                       precedence(token) <= precedence(operators[-1])):
                    apply_operator()
                operators.append(token)
            else:
                raise SyntaxError(f"Invalid token '{token}'")
            i += 1

        while operators:
            if operators[-1] in "()":
                raise SyntaxError("Mismatched parentheses")
            apply_operator()

        if len(values) != 1:
            raise ValueError("Not enough operands")
        return values[0]