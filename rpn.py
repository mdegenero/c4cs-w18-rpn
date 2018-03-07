#!/usr/bin/env python3

import operator
import readline
from colorama import Fore

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
}
        

def calculate(myarg):
    if myarg in ['quit', 'q', 'exit']:
        exit()
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            print(Fore.BLUE + str(arg1), Fore.GREEN + str(token), Fore.BLUE + str(arg2), Fore.WHITE)
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()
def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
            print(Fore.MAGENTA + "Result :", Fore.RED + str(result), Fore.WHITE)
        else:
            print(Fore.MAGENTA + "Result: ", Fore.BLUE + str(result), Fore.WHITE)

if __name__ == '__main__':
    main()
