import tokenn
from vocabulary import scan
from parser import signal_program
from generator import *


def main():
    scan('test1.sig')

    # print(' line  col   code  value')
    print('-----------------------------')
    # for lexeme in token.lexemes:
    #     print('   {:<4}{:<6}{:<6}{}'.format(lexeme.line, lexeme.col, lexeme.code, lexeme.value))

    for err in tokenn.err_stack:
        print(err)

    # print('\nConstants: {}'.format(token.consts))
    # print('Identifires: {}'.format(token.identifires))
    tree, lex_list = signal_program()
    kompile(tree, lex_list)


if __name__ == '__main__':
    main()
