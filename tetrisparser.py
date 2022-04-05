from sly import Parser
from tetrisscanner import TetrisLexer

class TetrisParser(Parser):
    
    tokens = TetrisLexer.tokens

    def __init__(self):
        self.names = { }

    @_('KEYWORD ASSIGNOP NUMBER')
    def statement(self, p):
        self.names[p.KEYWORD] = p.NUMBER
        print(self.names)