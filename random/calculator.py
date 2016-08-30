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
        self.ast = []

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
        calculation = input('What would you like to compute?\n')
        parsed = self.parse(calculation)
        if parsed:
            print('parsed ast', self.ast)
            answer = self.calculate()
            print('answer', answer)
            self.ast = []
            self.listen()
        elif calculation.lower() == 'help':
            print(self.instructions)
            self.listen()
        elif calculation.lower() == 'exit':
            print('Good work team')
        else:
            print('kernel failure')

    def parse(self, calculation):
        i = 0
        operands = []
        operator = ''
        number = ''
        while i < len(calculation): 
            c = calculation[i]
            if self.is_number(c):
                number += c
                if i == len(calculation) - 1:
                    operands.append(int(number))
                if len(operands) >= 2 and len(operator) == 1:
                    self.ast = [operator, operands]
                    operands = []
                    operator = ''
            elif c in self.operators:
                operator = c
                if len(number) >= 1:
                    operands.append(int(number))
                    number = ''
            elif c.isspace():
                continue
            else:
                return False
            i += 1
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
