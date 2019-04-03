# Table of delimiters
# delims = {
#     # ';': 59,
#     # '=': 61,
#     # '\\': 92,
#     # ',': 44,
#     # '.': 46
#
# }

# Table of identifires
identifires = {}

# Table of consts
consts = {
}

# Table of lexemes
lexemes = []

# Table of keywords
keywords = {
    'PROCEDURE': 401,
    'DEFFUNC': 402,
    'BEGIN': 403,
    'END': 404
}

errors = {
    'lexical': {
        'invalid_ident': "Lexer: Error (line: {}, column: {}): invalid identifier '{}'",
        'invalid_char': "Lexer: Error (line: {}, column: {}): invalid character '{}'",
        'unclosed_comment': "Lexer: Warning (line: {}, column: {}): *) expected, but end of file found",
    },
}

err_stack = []
