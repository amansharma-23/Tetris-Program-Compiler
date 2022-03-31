from sly import Lexer

class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { KEYWORD, NUMBER, MOVE, ASSIGNOP,BOOLEAN, DELIMITER, ID}

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['TRUE'] = 'BOOLEAN'
    ID['FALSE'] = 'BOOLEAN'
    ID['CONFIG'] = 'KEYWORD'
    ID['ROWS'] = 'KEYWORD'
    ID['COLUMNS'] = 'KEYWORD'
    ID['MUSIC'] = 'KEYWORD'
    ID['SPEED'] = 'KEYWORD'
    ID['NEXTQ'] = 'KEYWORD'
    ID['BLOCKTYPE1'] = 'KEYWORD'
    ID['BLOCKTYPE2'] = 'KEYWORD'
    ID['BLOCKTYPE3'] = 'KEYWORD'
    ID['BLOCKTYPE4'] = 'KEYWORD'
    ID['BLOCKTYPE5'] = 'KEYWORD'
    ID['BLOCKTYPE6'] = 'KEYWORD'
    ID['BLOCKTYPE7'] = 'KEYWORD'
    ID['TIMER'] = 'KEYWORD'
    ID['TIMEDGAME'] = 'KEYWORD'
    ID['RIGHT'] = 'MOVE'
    ID['LEFT'] = 'MOVE'
    ID['SOFTDROP'] = 'MOVE'
    ID['HARDDROP'] = 'MOVE'
    ID['ROTATERIGHT'] = 'MOVE'
    ID['ROTATELEFT'] = 'MOVE'
    NUMBER  = r'\d+'
    ASSIGNOP  = r'='
    DELIMITER = r'\n'

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1
    
if __name__ == '__main__':
    program = open('program.txt','r')
    data = program.read()
    program.close()
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))