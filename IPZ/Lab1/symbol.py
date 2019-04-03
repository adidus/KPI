

class Symbol:
    def __init__(self, attributes: list, val: list = '', attr: int = 0):
        self.val = val
        self.attr = attr
        self.line = 1
        self.col = 0
        self.attributes = attributes

    def read(self, file):
        self.val = file.read(1).upper()
        if self.val:
            self.attr = self.attributes[ord(self.val)]
            self.col += 1
            if self.val == '\n':
                self.col = 0
                self.line += 1
        return self.val