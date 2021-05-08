from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        self.lexer.add('AND', r'and')
        self.lexer.add('OR', r'or')
        self.lexer.add('RingWhen',r'RingWhen')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\{')
        self.lexer.add('CLOSE_PAREN', r'\}')
        #Brackets
        self.lexer.add('OPEN_BRC', r'\(')
        self.lexer.add('CLOSE_BRC', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        #Dot
        self.lexer.add('Dot', r'\.')
        #Comma
        self.lexer.add('Comma', r'\,')
        self.lexer.add('Equals', r'\=')
        #@
        self.lexer.add('At', r'\@')
        # # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('DIFF',r'\-')
        self.lexer.add('DIV',r'\/')
        self.lexer.add('MULTI',r'\*')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()