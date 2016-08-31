import sys
import pdb
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

    def add(self, args):
        return args[0] + args[1]

    def subtract(self, args):
        return args[0] - args[1]

    def multiply(self, args):
        return args[0] * args[1]

    def divide(self, args):
        return args[0] / args[1]

    def listen(self):
        self.calculation = input('What would you like to compute?\n')
        parsed = self.parse()
        if parsed:
            print('parsed ast', self.ast)
            answer = self.calculate()
            print('answer', answer)
            self.calculation = ''
            self.ast = ()
            self.listen()
        elif self.calculation.lower() == 'help':
            print(self.instructions)
            self.listen()
        elif self.calculation.lower() == 'exit':
            print('Good work team')
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

    def make_node_from_number(self, i):
        return self.get_next_full_number(i)

    def make_node(self, operator, num, current_node):
        # 1 + 2
        # +, 2, (1,)        --> (+, (1, 2))
        # 1 + 2 - 3
        # -, 3, (+, (1, 2)) --> (-, ((+, (1, 2)), 3))
        return (operator, (current_node, num))

    def parse(self):
        i = 0
        i, current_node = self.get_next_full_number(i)
        while i < len(self.calculation):
            i, operator = self.get_next_operator(i)
            i, num = self.get_next_full_number(i)
            current_node = self.make_node(operator, num, current_node)
        self.ast = current_node
        return True

    def calculate(self):
        answer = 0
        for index, step in enumerate(self.ast):
            if type(step) is list:
                print('step: list', index)
            elif step in self.operators:
                print('step: operator', index)
                answer = self.operators[step](self.ast[index+1])
            elif type(step) is int:
                print('step: int', index)
        return answer

if __name__ == '__main__':
    calculator = Calculator()
    calculator.listen()
