class Symbol:
    def __init__(self, attributes: list, val: str = '', attr: int = 0):
        """
        :param attributes: our attributes
        :param val: the value of lexeme
        :param attr: attribute
        """
        self.val = val
        self.attr = attr
        self.line = 1
        self.col = 0
        self.attributes = attributes

    def read(self, file: "file"):
        """
        :param file: file for reading
        :return: next value for reading
        """
        self.val = file.read(1).upper()
        if self.val:
            self.attr = self.attributes[ord(self.val)]
            self.col += 1
            if self.val == '\n':
                self.col = 0
                self.line += 1
        return self.val
