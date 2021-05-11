from lexer import Lexer
from parserTB import Parser
from tabulate import tabulate

#scanner_text_input = "/-This is main function \nIre@decrease(){\nIre@3num=5;\nRingWhen (counter<num){\nreg3=reg3-1;} }"
#parser_text_input = "Beginning;Division@x{Ire@xy;};End."

with open('scanner_text_input.txt', 'r') as file:
    scanner_text_input = file.read()
print('\n')
print(scanner_text_input)

with open('parser_text_input.txt', 'r') as file:
    parser_text_input = file.read()
print('\n')
print(parser_text_input)

lexer = Lexer().get_lexer()
tokens = lexer.lex(scanner_text_input)
Parsertokens = lexer.lex(parser_text_input)

print('\n')
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(Parsertokens)

token_names = []
token_values = []
token_lineno = []
token_match = []
lex_no = []
error_num = 0
counter = 1
oldlineno = 1
iscommented = 0
commentedlineno = 0
commentedblock = 0

for token in tokens:
    lexpos = str(token.source_pos)
    strpos = lexpos.split("lineno=", 1)[1]
    lineno = strpos.split(", ")[0]  
    if (token.name == "Comment_Line"):
        iscommented = 1
        commentedlineno = lineno
    if (token.name == "Comment_Block_Start"):
        iscommented = 1
        commentedblock = 1
    if (lineno != commentedlineno and commentedblock == 0):
        iscommented = 0
    if (iscommented == 0):
        #print(token)
        #print(token.name)
        token_names.append(token.name)
        #print(token.value)
        token_values.append(token.value)
        if (token.name == "ERROR"):
            error_num += 1
            token_match.append("Not matched")
        else:
            token_match.append("Matched")
        token_lineno.append(lineno)
        #print('Line #', lineno)
        if (oldlineno == lineno):
            counter += 1
        else:
            counter = 1
        lex_no.append(counter)
        #print('')
        oldlineno = lineno
    if (token.name == "Comment_Block_End"):
        iscommented = 0
        commentedblock = 0

table_headers = ["Line #", "Lexeme", "Return Token", "Lexeme # in Line", "Matchability"]
table_data = zip(token_lineno, token_values, token_names, lex_no, token_match)

print('\n')
print(tabulate(table_data, table_headers, tablefmt="pretty"))
print('Total # of Errors: ', error_num)
print('\n')