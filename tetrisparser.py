from sly import Parser
from tetrisscanner import TetrisLexer
from tetris import tetrisgame

class TetrisParser(Parser):
    
    tokens = TetrisLexer.tokens

    def __init__(self):
        self.names = { }
        # self.game = tetrisgame()

    @_('KEYWORD ASSIGNOP NUMBER DELIMITER')
    def statement(self,p):
        self.names[p.KEYWORD]=p.NUMBER
        # self.game.a=p.NUMBER

    @_('KEYWORD ASSIGNOP BOOLEAN DELIMITER')
    def statement(self,p):
        self.names[p.KEYWORD]=p.BOOLEAN

    @_('CONFIG MOVE ID DELIMITER')
    def statement(self,p):
        self.names[p.MOVE]=p.ID

    @_('DELIMITER')
    def statement(self,p):
        pass

    @_('NUMBER')
    def expr(self, p):
        print('number is ' + p.NUMBER)
        self.names[p.NUMBER] = p.NUMBER
        print(self.names)