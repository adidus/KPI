import token

# Array of ASCII character attributes
attributes = []


class Lexeme:
    def __init__(self, code, line, col, value):
        self.value = value
        self.code = code
        self.line = line
        self.col = col


class Symbol:
    def __init__(self, val='', attr=0):
        self.val = val
        self.attr = attr
        self.line = 1
        self.col = 0

    def read(self, file):
        self.val = file.read(1).upper()
        if self.val:
            self.attr = attributes[ord(self.val)]
            self.col += 1
            if self.val == '\n':
                self.col = 0
                self.line += 1
        return self.val


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

    if buf in token.keywords:
        code = token.keywords[buf]
    elif buf in token.identifires:
        code = token.identifires[buf]
    elif token.identifires:
        code = max(token.identifires.values()) + 1
        token.identifires[buf] = code
    else:
        code = 1001
        token.identifires[buf] = code

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
        token.err_stack.append(token.errors['lexical']['invalid_ident'].format(line, col, buf))
        return {'skip': True}
    # const exist in code
    elif buf in token.consts:
        code = token.consts[buf]
    elif token.consts:
        code = max(token.consts.values()) + 1
        token.consts[buf] = code
    else:
        code = 501
        token.consts[buf] = code

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
            token.err_stack.append(token.errors['lexical']['unclosed_comment'].format(line, col))
        else:
            while True:
                while symbol.val and symbol.val != '*':
                    symbol.read(file)
                if symbol.val == '':
                    token.err_stack.append(token.errors['lexical']['unclosed_comment'].format(line, col))
                    break
                else:
                    symbol.read(file)
                if symbol.val == ')':
                    symbol.read(file)
                    break
    return {'skip': True}


def illegal(symbol, file):
    token.err_stack.append(token.errors['lexical']['invalid_char'].format(symbol.line, symbol.col, symbol.val))
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
    fill_attributes(attributes)

    try:
        f = open(fname, 'r')
    except OSError:
        print('Couldn`t open this file')
    else:
        symbol = Symbol()
        symbol.read(f)
        while symbol.val:
            lex = lexeme_type[symbol.attr](symbol, f)
            print(lex)
            if not lex['skip']:
                token.lexemes.append(Lexeme(lex['code'], lex['line'], lex['col'], lex['val']))
        f.close()
