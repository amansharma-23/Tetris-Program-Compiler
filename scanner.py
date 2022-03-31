from sly import Lexer

class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { KEYWORD, NUMBER, MOVE, ASSIGNOP,BOOLEAN, DELIMITER}

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    KEYWORD = r'[CONFIG][ROWS][COLUMNS][MUSIC][SPEED][NEXTQ][BLOCKTYPE1][BLOCKTYPE2][BLOCKTYPE3][BLOCKTYPE4][BLOCKTYPE5][BLOCKTYPE6][BLOCKTYPE7][TIMER][TIMEDGAME]'
    NUMBER  = r'\d+'
    ASSIGNOP  = r'='
    BOOLEAN = r'[TRUE] | [FALSE]'
    MOVE = r'[RIGHT][LEFT][SOFTDROP][HARDDROP][ROTATERIGHT][ROTATELEFT]'
    DELIMITER = r'\n'

if __name__ == '__main__':
    data = 'TRUE'
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))