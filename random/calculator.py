import sys
import readline
import unittest

class Calculator:
    def __init__(self):
        self.operators = {
                '+': self.add,
                '-': self.subtract,
                '*': self.multiply,
                '/': self.divide
        }
        self.instructions = 'You can add (+), subtract (-), multiply (*), or divide (/). To exit, type "exit".\n'
        self.calculation = ''
        self.ast = ()

    def is_number(self, c):
        try:
            int(c)
            return True
        except:
            return False

    def add(self, op1, op2):
        return op1 + op2

    def subtract(self, op1, op2):
        return op1 - op2

    def multiply(self, op1, op2):
        return op1 * op2

    def divide(self, op1, op2):
        return op1 / op2

    def listen(self):
        self.calculation = input('What would you like to compute?\n')
        parsed = self.parse()
        if parsed:
            print('parsed ast', self.ast)
            answer = self.calculate()
            print('The answer is', answer)
            self.ast = ()
            self.listen()
        elif self.calculation.lower() == 'help':
            print(self.instructions)
            self.listen()
        elif self.calculation.lower() == 'exit':
            print('Cya later')
        else:
            print('kernel failure')

    def get_next_full_number(self, i):
        number = ''
        while i < len(self.calculation):
            c = self.calculation[i]
            if self.is_number(c):
                number += c
                i += 1
            else:
                break
        if self.is_number(number):
            return i, int(number)
        else:
            return i, False

    def skip_whitespaces(self, i):
        while i < len(self.calculation):
            c = self.calculation[i]
            if c.isspace():
                i += 1
            else:
                return i

    def get_next_operator(self, i):
        while i < len(self.calculation):
            c = self.calculation[i]
            if c in self.operators:
                i += 1
                return i, c
            else:
                return i, False

    def is_invalid_char(self, i):
        c = self.calculation[i]
        if (not c in self.operators) and (not self.is_number(c)):
            return True

    def operator_has_precedence(self, operator):
        return operator == '/' or operator == '*'

    def make_node(self, operator, num, current_node):
        if not self.operator_has_precedence(operator) or type(current_node) == int:
            return (operator, (current_node, num))
        else:
            return (current_node[0], (current_node[1][0], (operator, (current_node[1][1], num))))

    def parse(self):
        i = 0
        i, current_node = self.get_next_full_number(i)
        while i < len(self.calculation):
            i, operator = self.get_next_operator(i)
            i, num = self.get_next_full_number(i)
            current_node = self.make_node(operator, num, current_node)
        self.ast = current_node
        return True

    def calculate(self, node=None):
        if not node:
            node = self.ast
        if type(node) is tuple:
            operator = node[0]
            op1 = node[1][0]
            op2 = node[1][1]
            return self.operators[operator](self.calculate(op1), self.calculate(op2))
        elif type(node) is int:
            return node

if __name__ == '__main__':
    calculator = Calculator()
    calculator.listen()
