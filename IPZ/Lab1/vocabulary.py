import tokenn
from symbol import Symbol

# Array of ASCII character attributes
attributes = []


class Lexeme:
    def __init__(self, code: int, line: int, col: int, value: str):
        """
        :param code: code after analysing
        :param line: coordinate of line
        :param col: coordinate of column
        :param value: the value of lexeme
        """
        self.value = value
        self.code = code
        self.line = line
        self.col = col


def fill_attributes(attr: list):
    # 5 - illegals characters
    attr += [5 for x in range(128)]

    # 0 - whitespace
    for i in range(9, 14):
        attr[i] = 0
    attr[32] = 0

    # 1 - letters
    for i in range(65, 91):
        attr[i] = 1

    # 2 - numbers
    for i in range(48, 58):
        attr[i] = 2

    # 3 - delimiters
    attr[59] = 3
    attr[92] = 3
    attr[44] = 3
    attr[46] = 3
    attr[61] = 3

    # 4 - character '(',')'
    attr[40] = 4
    # attr[41] = 4


def whitespace(symbol, file):
    while symbol.val and symbol.attr == 0:
        symbol.read(file)
    return {'skip': True}


def ident(symbol, file):
    line = symbol.line
    col = symbol.col
    buf = ''
    while symbol.val and (symbol.attr == 1 or symbol.attr == 2):
        buf += symbol.val
        symbol.read(file)

    if buf in tokenn.keywords:
        code = tokenn.keywords[buf]
    elif buf in tokenn.identifires:
        code = tokenn.identifires[buf]
    elif tokenn.identifires:
        code = max(tokenn.identifires.values()) + 1
        tokenn.identifires[buf] = code
    else:
        code = 1001
        tokenn.identifires[buf] = code

    return {'code': code, 'line': line, 'col': col, 'val': buf, 'skip': False}


def number(symbol, file):
    err_idn = False
    line = symbol.line
    col = symbol.col
    buf = ''
    skiping = False
    while symbol.val and (symbol.attr == 1 or symbol.attr == 2):
        if symbol.attr != 2:
            err_idn = True
        buf += symbol.val
        symbol.read(file)
    if err_idn:
        tokenn.err_stack.append(tokenn.errors['lexical']['invalid_ident'].format(line, col, buf))
        return {'skip': True}
    # const exist in code
    elif buf in tokenn.consts:
        code = tokenn.consts[buf]
    elif tokenn.consts:
        code = max(tokenn.consts.values()) + 1
        tokenn.consts[buf] = code
    else:
        code = 501
        tokenn.consts[buf] = code

    return {'code': code, 'line': line, 'col': col, 'val': buf, 'skip': skiping}


def delim(symbol, file):
    line = symbol.line
    col = symbol.col
    buf = symbol.val
    code = ord(buf)
    symbol.read(file)
    return {'code': code, 'line': line, 'col': col, 'val': buf, 'skip': False}


def comment(symbol, file):
    line = symbol.line
    col = symbol.col
    buf = symbol.val
    code = ord(buf)
    symbol.read(file)
    skiping = True
    if symbol.val == '' or symbol.val != '*':
        return {'code': code, 'line': line, 'col': col, 'val': buf, 'skip': False}
    else:
        symbol.read(file)
        if symbol.val == '':
            tokenn.err_stack.append(tokenn.errors['lexical']['unclosed_comment'].format(line, col))
        else:
            while True:
                while symbol.val and symbol.val != '*':
                    symbol.read(file)
                if symbol.val == '':
                    tokenn.err_stack.append(tokenn.errors['lexical']['unclosed_comment'].format(line, col))
                    break
                else:
                    symbol.read(file)
                if symbol.val == ')':
                    symbol.read(file)
                    break
    return {'skip': True}


def illegal(symbol, file):
    tokenn.err_stack.append(tokenn.errors['lexical']['invalid_char'].format(symbol.line, symbol.col, symbol.val))
    symbol.read(file)
    return {'skip': True}


lexeme_type = {
    0: whitespace,
    1: ident,
    2: number,
    3: delim,
    4: comment,
    5: illegal,
}


def scan(fname: str):
    """
    :param fname: name of file for analysing
    """
    fill_attributes(attributes)

    try:
        f = open(fname, 'r')
    except OSError:
        print('Couldn`t open this file')
    else:
        symbol = Symbol(attributes)
        symbol.read(f)
        while symbol.val:
            lex = lexeme_type[symbol.attr](symbol, f)
            print(lex)
            if not lex['skip']:
                tokenn.lexemes.append(Lexeme(lex['code'], lex['line'], lex['col'], lex['val']))
        f.close()
