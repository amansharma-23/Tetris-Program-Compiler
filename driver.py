
from tetrisscanner import TetrisLexer
from tetrisparser import TetrisParser

def main():
    lexer = TetrisLexer()
    while True:
        program = open('program.rpj','r')
        text = input(">>> ")
        tokens = lexer.tokenize(text) # Creates a generator of tokens
        for t in tokens:
            print(t.type)
            print(t.value)
        # parser = TetrisParser()
        # parser.parse(tokens) # The entry point to the parser
        # print(parser.last_item_on_stack)

if __name__ == '__main__':
    main()