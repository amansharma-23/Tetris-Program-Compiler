from sly import Parser

class TetrisParser(Parser):

    @_('NUMBER')
    def expr(self, p):
    return Number(p.NUMBER)
