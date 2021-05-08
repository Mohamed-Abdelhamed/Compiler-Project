from rply import ParserGenerator
from ast import Number, Sum, Print , Minus ,Multiply,Divide


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM','DIFF','DIV','MULTI']
        )

    def parse(self):
        @self.pg.production('program : BEGINNING SEMI_COLON ClassDeclaration SEMI_COLON End Dot')
        def program(p):
            return p[2]

        @self.pg.production('ClassDeclaration : Division At ID OPEN_PAREN Class_Implementation CLOSE_PAREN')
        def ClassDeclaration(p):
            return p[4]

        @self.pg.production('ClassDeclaration : Division At ID AT InferedForm OPEN_PAREN Class_Implementation CLOSE_PAREN')
        def ClassDeclaration(p):
            return p[6]

        @self.pg.production('Class_Implementation : VarDeclaration Class_Implementation')
        def Class_Implementation(p):
            return p[0]
            return p[1]

        @self.pg.production('Class_Implementation : MethodDeclaration Class_Implementation')
        def Class_Implementation(p):
            return p[0]
            return p[1]
        
        @self.pg.production('Class_Implementation : Comment Class_Implementation')
        def Class_Implementation(p):
            return p[1]


        @self.pg.production('Class_Implementation : Func_Call Class_Implementation')
        def Class_Implementation(p):
            return p[0]
            return p[1]


        @self.pg.production('Class_Implementation : empty')
        # def Class_Implementation(p):


        @self.pg.production('MethodDeclaration : FuncDecl SEMI_COLON')
        def MethodDeclaration(p):
            return p[0]
            
           
        
        @self.pg.production('MethodDeclaration : FuncDecl OPEN_PAREN VarDeclaration Statments CLOSE_PAREN')
        def MethodDeclaration(p):
            return p[0]
            return p[2]
            return p[3]
            

        @self.pg.production('Func Decl : Type AT  OPEN_BRC ParametersList CLOSE_BRC')
        def FuncDecl(p):
            return p[0]
            return p[3]


        @self.pg.production('Type : Ire')
        def Type(p):
            return Number(p[0].value)
        @self.pg.production('Type : Sire')
        def Type(p):
            return Number(p[0].value)
        @self.pg.production('Type : Clo')
        def Type(p):
            return Number(p[0].value)
        
        @self.pg.production('ParameterList : empty')
        def ParameterList(p):
            return Number(p[0].value)
        
        @self.pg.production('ParameterList : NoneValue')
        def ParameterList(p):
            return Number(p[0].value)
        
        @self.pg.production('ParameterList : NonEmptyList')
        def ParameterList(p):
            return p[0]
        
        @self.pg.production('Non-Empty List : Type AT ID SEMI_COLON')
        def NonEmptyList(p):
            return p[0]
        
        @self.pg.production('Non-Empty List : NonEmptyList Comma Type AT ID')
        def NonEmptyList(p):
            return p[0]
            return p[2]
        
        @self.pg.production('VarDeclaration : Type AT ID_List SEMI_COLON VarDeclaration')
        def VarDeclaration(p):
            return p[0]
            return p[2]
            return p[4]
        
        @self.pg.production('VarDeclaration : empty')
        def VarDeclaration(p):
            return Number(p[0].value)
        
        @self.pg.production('ID_List : ID')
        # def ID_List(p):
        #     return Number(p[0].value)
        
        @self.pg.production('ID_List : ID_List Comma ID')
        def ID_List(p):
            return p[0]
        
        @self.pg.production('Statements : empty')

        @self.pg.production('Statements : Statement Statments')
        def Statments(p):
            return p[0]
            return p[1]

        @self.pg.production('Statement : Assignment')
        def Statment(p):
            return p[0]
        @self.pg.production('Statement : WhetherDo_Statement')
        def Statment(p):
            return p[0]
        @self.pg.production('Statement : RingWhen_Statement')
        def Statment(p):
            return p[0]
        @self.pg.production('Statement : BackedValue_Statement')
        def Statment(p):
            return p[0]
        @self.pg.production('Statement : terminatethis_Statement')
        def Statment(p):
            return p[0]
        @self.pg.production('Statement : read OPEN_BRC ID CLOSE_BRC SEMI_COLON')
        @self.pg.production('Statement : write OPEN_BRC Expression CLOSE_BRC SEMI_COLON')

        @self.pg.production('Assignment : VarDeclaration Equals Expression SEMI_COLON')
        def Assignment(p):
            return p[0]
            return p[2]
        @self.pg.production('Func_Call : ID OPEN_BRC Argument_List CLOSE_BRC SEMI_COLON')
        def Func_Call(p):
            return p[2]
        @self.pg.production('Argument_List : empty')
        
        @self.pg.production('Argument_List : NonEmpty_Argument_List')
        def Argument_List(p):
            return p[0]
        @self.pg.production('NonEmpty_Argument_List : Expression')
        def NonEmpty_Argument_List(p):
            return p[0]
        @self.pg.production('NonEmpty_Argument_List : NonEmpty_Argument_List Comma Expression')
        def NonEmpty_Argument_List(p):
            return p[0]
            return p[2]
        
        @self.pg.production('Block Statements : OPEN_PAREN Statements CLOSE_PAREN')
        def Block_Statements(p):
            return p[1]

        @self.pg.production('WhetherDo_Statement : WhetherDo OPEN_BRC Condition_Expression CLOSE_BRC Block Statements Else Statement')
        def WhetherDo_Statement(p):
            return p[2]
            return p[5]
            return p[7]

        @self.pg.production('Condition_Expression : Condition')
        def Condition_Expression(p):
            return p[0]

        @self.pg.production('Condition_Expression : Condition Condition_Op Condition')
        def Condition_Expression(p):
            return p[0]
            return p[1]
            return p[2]
        
        @self.pg.production('Condition_Op : And')
        @self.pg.production('Condition_Op : OR')

        @self.pg.production('Condition : Expression Comparison_Op Condition')
        def Condition(p):
            return p[1]
            return p[1]
            return p[2]
        @self.pg.production('Comparison_Op : ')
        # def Comparison_Op(p):

        @self.pg.production('RingWhen_Statement : RingWhen OPEN_BRC Condition_Expression CLOSE_BRC Block_Statements')
        def RingWhen_Statement(p):
            return p[2]
            return p[4]
        
        @self.pg.production('BackedValue_Statement : BackedValue At Expression SEMI_COLON')
        def BackedValue_Statement(p):
            return p[2]
        @self.pg.production('BackedValue_Statement : BackedValue At ID SEMI_COLON')
        def BackedValue_Statement(p):
            return p[2]
        @self.pg.production('terminatethis_Statement : TerminateThisNow SEMI_COLON')
        # def terminatethis_Statement(p):
        #     return p[2]
        @self.pg.production('Expression : Term')
        def Expression(p):
            return p[0]
        @self.pg.production('Expression : Expression AT Add_Op AT Factor')
        def Expression(p):
            return p[0]
            return p[2]
            return p[4]
        @self.pg.production('Add_Op : SUM')
        def Add_Op(p):
            return p[0]
        @self.pg.production('Add_Op : DIFF')
        def Add_Op(p):
            return p[0]
        @self.pg.production('Term : Factor')
        def Term(p):
            return p[0]
        @self.pg.production('Term : Expression AT Mul_Op AT Factor')
        def Term(p):
            return p[0]
            return p[2]
            return p[4]
        @self.pg.production('Mul_Op : MULTI')
        def Mul_Op(p):
            return p[0]
        @self.pg.production('Mul_Op : DIV')
        def Mul_Op(p):
            return p[0]
        @self.pg.production('Factor : ID')
        def Factor(p):
            return p[0]
        @self.pg.production('Factor : Number')
        def Factor(p):
            return p[0]
        
        @self.pg.production('Comment : ')
        # def Factor(p):
        #     return p[0]
        
        @self.pg.production('using_command : using OPEN_BRC F_name Dot txt')
        def using_command(p):
            return p[2]
        
        @self.pg.production('F_name : STR')
        def F_name(p):
            return p[0]


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
