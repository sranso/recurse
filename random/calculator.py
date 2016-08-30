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
            print(parsed)
            answer = self.calculate()
            print(answer)
            self.listen()
        elif calculation.lower() == 'help':
            print(self.instructions)
        elif calculation.lower() == 'exit':
            print('Good work team')
        else:
            print('kernel failure')

    def parse(self, calculation):
        i = 0
        operands = []
        operator = ''
        while i < len(calculation): 
            c = calculation[i]
            if self.is_number(c):
                operands.append(int(c))
                if len(operands) >= 2 and len(operator) == 1:
                    self.ast = [operator, operands]
                    operands = []
                    operator = ''
            elif c in self.operators:
                operator = c
            elif c.isspace():
                continue
            else:
                return False
            i += 1
        return self.ast

    def calculate(self):
        answer = 0
        for index, step in enumerate(self.ast):
            #pdb.set_trace()
            if type(step) is list:
                print('hi')
            elif step in self.operators:
                answer = self.operators[step](self.ast[index+1])
            elif type(step) is int:
                print('hi')
        return answer

if __name__ == '__main__':
    calculator = Calculator()
    calculator.listen()
