from token import *
from vocabulary import *
from tree import *

error_table = {"Wrong delimiter": -1, "Wrong keyword": -2, "No such identifier": -3, "Wrong integer": -4}

lex_list = lexemes
tree = Tree()


def scan(dictionary, value):
    for key, v in dictionary.items():
        if v == value:
            return key


def err(err_number, line, col):
    tree.add(err_number)
    tree.current_element = tree.current_element.parent_element
    print('\n\nSYNTAX ANALYZER\n')
    tree.print_tree()
    print('ERROR traceback:')
    print(scan(error_table, err_number) + ' on line - ' + str(line) + ' and column - ' + str(col))
    print(tree.listing())
    quit()


def functionIdentifier(i):
    tree.add('function-identifier')
    identifier(lex_list[i])
    # tree.current_element = tree.current_element.parent_element
    return i + 1


def unsignedInteger(i):
    tree.add('unsigned-integer')
    lexem = lex_list[i]
    if lexem.code < 1000 and lexem.code >= 500:
        tree.add(scan(consts, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-3, lexem.line, lexem.col)
    tree.current_element = tree.current_element.parent_element


def constant(i):
    tree.add('constant')
    unsignedInteger(i)
    tree.current_element = tree.current_element.parent_element
    # tree.current_element = tree.current_element.parent_element
    return i + 1


def functionCharasteristic(i):
    tree.add('function-charasteristic')
    lexem = lex_list[i]

    if lexem.code == 92:
        tree.add(scan(delims, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-1, lexem.line, lexem.col)
    # print(lexem.code)
    unsignedInteger(i + 1)

    i += 2
    lexem = lex_list[i]

    if lexem.code == 44:
        tree.add(scan(delims, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-1, lexem.line, lexem.col)

    unsignedInteger(i + 1)
    tree.current_element = tree.current_element.parent_element
    return i + 2


def function(i):
    tree.add('function')

    i = functionIdentifier(i)

    lexem = lex_list[i]
    if lexem.code == 61:
        tree.add(scan(delims, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-1, lexem.line, lexem.col)

    i = constant(i + 1)
    i = functionCharasteristic(i)

    lexem = lex_list[i]

    if lexem.code == 59:
        tree.add(scan(delims, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-1, lexem.line, lexem.col)

    i += 1
    tree.current_element = tree.current_element.parent_element

    return i


def functionList(i):
    tree.add('function-list')
    lexem = lex_list[i]
    if lexem.code == 403:
        tree.add('empty')
        tree.current_element = tree.current_element.parent_element
    else:
        if lex_list[i].code != 402:
            i = function(i)
            i = functionList(i)
            tree.current_element = tree.current_element.parent_element


    return i


def mathFunctionDeclarations(i):
    tree.add('math-function-declarations')
    lexem = lex_list[i]
    if lexem.code == 402:
        tree.add(scan(keywords, lexem.code))
        tree.current_element = tree.current_element.parent_element
        i = functionList(i + 1)
        tree.current_element = tree.current_element.parent_element
    else:
        if lexem.code == 403:
            tree.add('empty')
            tree.current_element = tree.current_element.parent_element
        else:
            err(-2, lexem.line, lexem.col)

            
        tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element

    return i


def declarations(i):
    tree.add('declarations')

    i = mathFunctionDeclarations(i)
    tree.current_element = tree.current_element.parent_element
    return i


def statement_list(i):
    tree.add('statement-list')

    lexem = lex_list[i]
    if lexem.code == 404:
        tree.add('empty')
        tree.current_element = tree.current_element.parent_element
    else:
        err(-2, lexem.line, lexem.col)
    tree.current_element = tree.current_element.parent_element
    # i+=1
    return i


def block(i):
    tree.add('block')

    i = declarations(i)

    lexem = lex_list[i]

    if lexem.code == 403:
        tree.add(scan(keywords, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        
        err(-2, lexem.line, lexem.col)
    i += 1
    i = statement_list(i)
    lexem = lex_list[i]
    if lexem.code == 404:
        tree.add(scan(keywords, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        
        err(-2, lexem.line, lexem.col)
    tree.current_element = tree.current_element.parent_element
    return i;


def identifier(lexem):
    tree.add('identifier')

    if lexem.code >= 1000:
        tree.add(scan(identifires, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-3, lexem.line, lexem.col)
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element


def procedureIdentifier(lexem):
    tree.add('procedure-identifier')
    identifier(lexem)


def program():
    tree.add('PROCEDURE')
    i = 0
    lexem = lex_list[i]
    if lexem.code == 401:
        tree.add(scan(keywords, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-1, lexem.line, lexem.col)

    i += 1
    lexem = lex_list[i]
    procedureIdentifier(lexem);

    i += 1
    lexem = lex_list[i]

    if lexem.code == 59:
        tree.add(scan(delims, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-1, lexem.line, lexem.col)

    i += 1
    i = block(i)
    i += 1
    lexem = lex_list[i]

    if lexem.code == 46:
        tree.add(scan(delims, lexem.code))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-1, lexem.line, lexem.col)


def signal_program():
    if lex_list:
        program()

        for lex in lex_list:
            print(lex.value)
        print('-----------------------------------------')
        print('-----------------------------------------')
        print('-----------------------------------------')
        tree.print_tree()
        print()
        print(error_table)
        print()
        tree.listing()
    return tree

# if __name__ == '__main__':
#     print(lex_list)
#     signal_program_proc()
