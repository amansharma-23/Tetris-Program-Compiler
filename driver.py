
from tetrisscanner import TetrisLexer
from tetrisparser import TetrisParser

def main():
    lexer = TetrisLexer()
    parser = TetrisParser()
    program = open('program.rpj','r')
    text = program.readlines()
    # print(len(text))
    for string in text:
        tokens = lexer.tokenize(string) # Creates a generator of tokens
        # for tok in tokens:
        #     print(tok)
            # print('type=%r, value=%r' % (tok.type, tok.value))
        # print(tokens)
        parser.parse(tokens) 
    print(parser.names)   
    
    # parser.parse(tokens) # The entry point to the parser
    # print(parser.last_item_on_stack)

if __name__ == '__main__':
    main()