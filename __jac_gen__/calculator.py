from __future__ import annotations
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__

@_Jac.make_walker(on_entry=[], on_exit=[])
@__jac_dataclass__(eq=False)
class init:

    def run(self) -> None:
        print('ð\x9f§® Welcome to the Jac Calculator!')
        print('You can perform +, -, *, or / operations.')
        num1 = 10
        num2 = 5
        op = '+'
        if op == '+':
            print('Result: ' + str(num1 + num2))
        elif op == '-':
            print('Result: ' + str(num1 - num2))
        elif op == '*':
            print('Result: ' + str(num1 * num2))
        elif op == '/':
            print('Result: ' + str(num1 / num2))
        else:
            print('Invalid operation!')

@_Jac.create_test
def test_t1(check) -> None:
    __init__.run()