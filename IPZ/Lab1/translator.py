import token
from vocabulary import scan
from parser import signal_program

def main():
    scan('test1.sig')

    # print(' line  col   code  value')
    print('-----------------------------')
    # for lexeme in token.lexemes:
    #     print('   {:<4}{:<6}{:<6}{}'.format(lexeme.line, lexeme.col, lexeme.code, lexeme.value))

    for err in token.err_stack:
        print(err)

    # print('\nConstants: {}'.format(token.consts))
    # print('Identifires: {}'.format(token.identifires))
    signal_program()

if __name__ == '__main__':
    main()
