from rply import ParserGenerator
from ast import  Program,ClassDeclaration,Class_Implementation,MethodDeclaration,FuncDecl,Type,ParameterList,NonEmptyList,ID_List,Statements,Statement,Assignment,Func_Call,Argument_List,NonEmpty_Argument_List,Block_Statements,WhetherDo_Statement,Condition_Expression,Condition_Op,Condition,Comparison_Op,RingWhen_Statement,BackedValue_Statement,terminatethis_Statement,Expression,Add_Op,Term,Mul_Op,Factor,Comment,using_command,F_name,Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            [ 'Class','Inheritance','Whether_Do','Else','Integer','SInteger','Character','String',
            'Float','SFloat','Void','Break','Loop','Return','Struct','Check','Case_Of','Start_Statement',
            'End_Statement','Comment_Line','Comment_Block_Start','Comment_Block_End','Plus','Minus','Mult',
            'Div','And','Or','Not','Identical','Less-than','Greater-than','NotEqual','Less-thanOrEqual','Greater-thanOrEqual',
            'Equal','Dot','Opened_Parenthesis','Closed_Parenthesis','Opened_Bracket','Closed_Bracket','ERROR','Number','Comma',
            'Inclusion','Delimiter','Identifier','ERROR'
            ]
        )

    def parse(self):
        @self.pg.production('Program : Start_Statement Delimiter ClassDeclaration Delimiter End_Statement Dot')
        def program(p):
            return p[2]

        @self.pg.production('Program : Comment Delimiter using_command')
        def program(p):
            return p[2]

        @self.pg.production('ClassDeclaration : Class Delimiter ID Opened_Parenthesis Class_Implementation Closed_Parenthesis')
        def ClassDeclaration(p):
            return p[4]

        @self.pg.production('ClassDeclaration : Class Delimiter ID Delimiter Inheritance Opened_Parenthesis Class_Implementation Closed_Parenthesis')
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


        @self.pg.production('MethodDeclaration : FuncDecl Delimiter')
        def MethodDeclaration(p):
            return p[0]
            
           
        
        @self.pg.production('MethodDeclaration : FuncDecl Opened_Parenthesis VarDeclaration Statments Closed_Parenthesis')
        def MethodDeclaration(p):
            return p[0]
            
            

        @self.pg.production('Func Decl : Type Delimiter  Opened_Bracket ParametersList Closed_Bracket')
        def FuncDecl(p):
            return p[0]
            return p[3]


        @self.pg.production('Type : Integer')
        def Type(p):
            return p[0]
        @self.pg.production('Type : SInteger')
        def Type(p):
            return p[0]
        @self.pg.production('Type : Character')
        def Type(p):
            return p[0]
        @self.pg.production('Type : String')
        def Type(p):
            return p[0]  
        @self.pg.production('Type : Float')
        def Type(p):
            return p[0]  
        @self.pg.production('Type : SFloat')
        def Type(p):
            return p[0] 
        @self.pg.production('Type : Void')
        def Type(p):
            return p[0]    
        @self.pg.production('ParameterList : empty')
        def ParameterList(p):
            return p[0]
        
        @self.pg.production('ParameterList : Void')
        def ParameterList(p):
            return p[0]
        
        @self.pg.production('ParameterList : NonEmptyList')
        def ParameterList(p):
            return p[0]
        
        @self.pg.production('Non-Empty List : Type Delimiter ID Delimiter')
        def NonEmptyList(p):
            return p[0]
        
        @self.pg.production('Non-Empty List : NonEmptyList Comma Type Delimiter ID')
        def NonEmptyList(p):
            return p[0]
            return p[2]
        
        @self.pg.production('VarDeclaration : Type Delimiter ID_List Delimiter VarDeclaration')
        def VarDeclaration(p):
            return p[0]
            return p[2]
            return p[4]
        
        @self.pg.production('VarDeclaration : empty')
        def VarDeclaration(p):
            return p[0]
        
        @self.pg.production('ID_List : ID')
        def ID_List(p):
            return p[0]
        
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
        @self.pg.production('Statement : read Opened_Bracket ID Closed_Bracket Delimiter')
        @self.pg.production('Statement : write Opened_Bracket Expression Closed_Bracket Delimiter')

        @self.pg.production('Assignment : VarDeclaration Equal Expression Delimiter')
        def Assignment(p):
            return p[0]
            return p[2]
        @self.pg.production('Func_Call : ID Opened_Bracket Argument_List Closed_Bracket Delimiter')
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
        
        @self.pg.production('Block Statements : Opened_Parenthesis Statements Closed_Parenthesis')
        def Block_Statements(p):
            return p[1]

        @self.pg.production('WhetherDo_Statement : Whether_Do Opened_Bracket Condition_Expression Closed_Bracket Block Statements Else Statement')
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
        def Condition_Op(p):
            return p[0]
        @self.pg.production('Condition_Op : Or')
        def Condition_Op(p):
            return p[0]

        @self.pg.production('Condition : Expression Comparison_Op Condition')
        def Condition(p):
            return p[0]
            return p[1]
            return p[2]
        @self.pg.production('Comparison_Op : Identical')
        @self.pg.production('Comparison_Op : Less-than')
        @self.pg.production('Comparison_Op : Greater-than')
        @self.pg.production('Comparison_Op : NotEqual')
        @self.pg.production('Comparison_Op : Less-thanOrEqual')
        @self.pg.production('Comparison_Op : Greater-thanOrEqual')
        def Comparison_Op(p):
            return p[0]

        @self.pg.production('RingWhen_Statement : Loop Opened_Bracket Condition_Expression Closed_Bracket Block_Statements')
        def RingWhen_Statement(p):
            return p[2]
            return p[4]
        
        @self.pg.production('BackedValue_Statement : Return Delimiter Expression Delimiter')
        def BackedValue_Statement(p):
            return p[2]
        @self.pg.production('BackedValue_Statement : Return Delimiter ID Delimiter')
        def BackedValue_Statement(p):
            return p[2]
        @self.pg.production('terminatethis_Statement : Break Delimiter')
        def terminatethis_Statement(p):
            return p[0]
        @self.pg.production('Expression : Term')
        def Expression(p):
            return p[0]
        @self.pg.production('Expression : Expression Delimiter Add_Op Delimiter Factor')
        def Expression(p):
            return p[0]
            return p[2]
            return p[4]
        @self.pg.production('Add_Op : Plus')
        def Add_Op(p):
            return p[0]
        @self.pg.production('Add_Op : Minus')
        def Add_Op(p):
            return p[0]
        @self.pg.production('Term : Factor')
        def Term(p):
            return p[0]
        @self.pg.production('Term : Expression Delimiter Mul_Op Delimiter Factor')
        def Term(p):
            return p[0]
            return p[2]
            return p[4]
        @self.pg.production('Mul_Op : Mult')
        def Mul_Op(p):
            return p[0]
        @self.pg.production('Mul_Op : Div')
        def Mul_Op(p):
            return p[0]
        @self.pg.production('Factor : ID')
        def Factor(p):
            return p[0]
        @self.pg.production('Factor : Number')
        def Factor(p):
            return p[0]
        
        @self.pg.production('Comment : Comment_Block_Start Identifier Comment_Block_End')
        def Comment(p):
            return 0
            # return p[0]
            # return p[2]
        @self.pg.production('Comment : Comment_Line Identifier')
        def Comment(p):
            return p[0]
        
        @self.pg.production('using_command : Inclusion Opened_Bracket F_name Dot txt Closed_Parenthesis Delimiter')
        def using_command(p):
            return p[2]
        
        @self.pg.production('F_name : Identifier')
        def F_name(p):
            return p[0]


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
