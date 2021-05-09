from lexer import Lexer
#from parserTB import Parser
from tabulate import tabulate

#text_input = """print(10  - 9);"""
text_input = "/-This is main function \nIre@decrease(){\nIre@3num=5;\nRingWhen (counter<num){\nreg3=reg3-1;} }"

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

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
    if (token.name == "Comment Line"):
        iscommented = 1
        commentedlineno = lineno
    if (token.name == "Comment Block Start"):
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
    if (token.name == "Comment Block End"):
        iscommented = 0
        commentedblock = 0

table_headers = ["Line #", "Lexeme", "Return Token", "Lexeme # in Line", "Matchability"]
table_data = zip(token_lineno, token_values, token_names, lex_no, token_match)

print('\n')
print(tabulate(table_data, table_headers, tablefmt="pretty"))
print('Total # of Errors: ', error_num)
print('\n')

#pg = Parser()
#pg.parse()
#parser = pg.get_parser()
#parser.parse(tokens).eval()