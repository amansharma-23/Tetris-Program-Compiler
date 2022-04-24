from sly import Parser
from tetrisscanner import TetrisLexer

class TetrisParser(Parser):
    
    tokens = TetrisLexer.tokens

    def __init__(self):
        self.names = {}
        self.blocktable = [True, True, True, True, True, True, True]

    @_('KEYWORD ASSIGNOP NUMBER DELIMITER')
    def statement(self,p):
        self.names[p.KEYWORD]=int(p.NUMBER)

    @_('KEYWORD ASSIGNOP BOOLEAN DELIMITER')
    def statement(self,p):
        self.names[p.KEYWORD]=p.BOOLEAN
        if(p.KEYWORD=="BLOCKTYPE1"):
            if(p.BOOLEAN=="FALSE"):
                self.blocktable[0]=False
        if(p.KEYWORD=="BLOCKTYPE2"):
            if(p.BOOLEAN=="FALSE"):
                self.blocktable[1]=False
        if(p.KEYWORD=="BLOCKTYPE3"):
            if(p.BOOLEAN=="FALSE"):
                self.blocktable[2]=False
        if(p.KEYWORD=="BLOCKTYPE4"):
            if(p.BOOLEAN=="FALSE"):
                self.blocktable[3]=False
        if(p.KEYWORD=="BLOCKTYPE5"):
            if(p.BOOLEAN=="FALSE"):
                self.blocktable[4]=False
        if(p.KEYWORD=="BLOCKTYPE6"):
            if(p.BOOLEAN=="FALSE"):
                self.blocktable[5]=False
        if(p.KEYWORD=="BLOCKTYPE7"):
            if(p.BOOLEAN=="FALSE"):
                self.blocktable[6]=False

    @_('CONFIG MOVE ID DELIMITER')
    def statement(self,p):
        self.names[p.MOVE]=p.ID

    @_('DELIMITER')
    def statement(self,p):
        pass
        

    # @_('NUMBER')
    # def expr(self, p):
    #     print('number is ' + p.NUMBER)
    #     self.names[p.NUMBER] = p.NUMBER
    #     print(self.names)