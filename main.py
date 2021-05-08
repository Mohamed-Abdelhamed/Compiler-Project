from lexer import Lexer
from parserTB import Parser

text_input = """
Beginning;
Division@x{
Ire@decrease() {
Ire@reg3=5;
RingWhen (counter<num){
reg3=reg3-1; } }}End
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()