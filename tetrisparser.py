from sly import Parser
from tetrisscanner import TetrisLexer

class TetrisParser(Parser):
    
    tokens = TetrisLexer.tokens

    @_('KEYWORD ASSIGNOP NUMBER')
    def statement(self, p):
        self.names[p.KEYWORD] = p.NUMBER
