from rply import ParserGenerator
# from ast import  Program,ClassDeclaration,Class_Implementation,MethodDeclaration,FuncDecl,Type,ParameterList,NonEmptyList,ID_List,Statements,Statement,Assignment,Func_Call,Argument_List,NonEmpty_Argument_List,Block_Statements,WhetherDo_Statement,Condition_Expression,Condition_Op,Condition,Comparison_Op,RingWhen_Statement,BackedValue_Statement,terminatethis_Statement,Expression,Add_Op,Term,Mul_Op,Factor,Comment,using_command,F_name,Print
# from ast import Print

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            [ 'Class','Inheritance','Whether_Do','Else','Integer','SInteger','Character','String',
            'Float','SFloat','Void','Break','Loop','Return','Start_Statement',
            'End_Statement','Comment_Line','Comment_Block_Start','Comment_Block_End','Plus','Minus','Mult',
            'Div','And','Or','Identical','Less-than','Greater-than','NotEqual','Less-thanOrEqual','Greater-thanOrEqual',
            'Equal','Dot','Opened_Parenthesis','Closed_Parenthesis','Opened_Bracket','Closed_Bracket','Number','Comma',
            'Inclusion','Delimiter','Identifier','Read','Write'
            ]
        )

    def parse(self):
        @self.pg.production('Program : Start_Statement Delimiter ClassDeclaration Delimiter End_Statement Dot')
        @self.pg.production('Program : Comment Delimiter using_command')
        def program(p):
            print("Program")


        @self.pg.production('ClassDeclaration : Class Delimiter Identifier Opened_Parenthesis Class_Implementation Closed_Parenthesis')
        @self.pg.production('ClassDeclaration : Class Delimiter Identifier Delimiter Inheritance Opened_Parenthesis Class_Implementation Closed_Parenthesis')
        def ClassDeclaration(p):
            print("Class Declaraion")

        @self.pg.production('Class_Implementation : VarDeclaration Class_Implementation')
        @self.pg.production('Class_Implementation : MethodDeclaration Class_Implementation') 
        @self.pg.production('Class_Implementation : Comment Class_Implementation')
        @self.pg.production('Class_Implementation : Func_Call Class_Implementation')
        
        def Class_Implementation(p):
            print("Class Implementation")

        @self.pg.production('Class_Implementation :')
        def Class_Implementation(p):
            return


        @self.pg.production('MethodDeclaration : FuncDecl Delimiter')
        @self.pg.production('MethodDeclaration : FuncDecl Opened_Parenthesis VarDeclaration Statements Closed_Parenthesis')
        def MethodDeclaration(p):
            print ("Method Declaration")
            

        @self.pg.production('FuncDecl : Type Delimiter  Opened_Bracket ParameterList Closed_Bracket')
        def FuncDecl(p):
            print("Fun Decl")
 
        
        @self.pg.production('ParameterList : Void')
        @self.pg.production('ParameterList : NonEmptyList')
        def ParameterList(p):
            print("Parameter List")
      
        @self.pg.production('ParameterList :')
        def ParameterList(p):
            return
        
        @self.pg.production('NonEmptyList : Type Delimiter Identifier Delimiter')
        @self.pg.production('NonEmptyList : NonEmptyList Comma Type Delimiter Identifier')
        def NonEmptyList(p):
            print("Non Empty")
        
        @self.pg.production('VarDeclaration : Type Delimiter ID_List Delimiter VarDeclaration')
        def VarDeclaration(p):
            print("Var Decl")
        @self.pg.production('VarDeclaration :')
        def VarDeclaration(p):
            return 
        
        @self.pg.production('ID_List : Identifier')
        @self.pg.production('ID_List : ID_List Comma Identifier')
        def ID_List(p):
            print("ID_List")
        
        
        @self.pg.production('Statements : Statement Statements')
        def Statements(p):
            print("Statements")
        
        @self.pg.production('Statements :')
        def Statements(p):
            return 

        @self.pg.production('Statement : Assignment')
        @self.pg.production('Statement : WhetherDo_Statement')
        @self.pg.production('Statement : RingWhen_Statement')
        @self.pg.production('Statement : BackedValue_Statement')
        @self.pg.production('Statement : terminatethis_Statement')
        @self.pg.production('Statement : Read Opened_Bracket Identifier Closed_Bracket Delimiter')
        @self.pg.production('Statement : Write Opened_Bracket Expression Closed_Bracket Delimiter')
        def Statment(p):
            print("Statement")

        @self.pg.production('Assignment : VarDeclaration Equal Expression Delimiter')
        def Assignment(p):
            print("Assignment")

        @self.pg.production('Func_Call : Identifier Opened_Bracket Argument_List Closed_Bracket Delimiter')
        def Func_Call(p):
            print("Func_Call")

       
        
        @self.pg.production('Argument_List : NonEmpty_Argument_List')
        def Argument_List(p):
            print ("Argument List")
        
        @self.pg.production('Argument_List :')
        def Argument_List(p):
            return 

        @self.pg.production('NonEmpty_Argument_List : Expression')
        @self.pg.production('NonEmpty_Argument_List : NonEmpty_Argument_List Comma Expression')
        def NonEmpty_Argument_List(p):
            print("Non Empty Argument List")
        
        @self.pg.production('Block_Statements : Opened_Parenthesis Statements Closed_Parenthesis')
        def Block_Statements(p):
            print("Block Statement")

        @self.pg.production('WhetherDo_Statement : Whether_Do Opened_Bracket Condition_Expression Closed_Bracket Block_Statements Else Statement')
        def WhetherDo_Statement(p):
            print("Whether Do")

        @self.pg.production('Condition_Expression : Condition')
        @self.pg.production('Condition_Expression : Condition Condition_Op Condition')
        def Condition_Expression(p):
            print("Condition Expression")

        
        @self.pg.production('Condition_Op : And')
        @self.pg.production('Condition_Op : Or')
        def Condition_Op(p):
            print("Condition OP")
        
        @self.pg.production('Condition : Expression Comparison_Op Condition')
        def Condition(p):
            print("Condition")

        @self.pg.production('Comparison_Op : Identical')
        @self.pg.production('Comparison_Op : Less-than')
        @self.pg.production('Comparison_Op : Greater-than')
        @self.pg.production('Comparison_Op : NotEqual')
        @self.pg.production('Comparison_Op : Less-thanOrEqual')
        @self.pg.production('Comparison_Op : Greater-thanOrEqual')
        def Comparison_Op(p):
            print("Comparison OP")

        @self.pg.production('RingWhen_Statement : Loop Opened_Bracket Condition_Expression Closed_Bracket Block_Statements')
        def RingWhen_Statement(p):
            print("Ring When Statement")
        
        @self.pg.production('BackedValue_Statement : Return Delimiter Expression Delimiter')
        @self.pg.production('BackedValue_Statement : Return Delimiter Identifier Delimiter')
        def BackedValue_Statement(p):
            print("Backed Value")
        
        @self.pg.production('terminatethis_Statement : Break Delimiter')
        def terminatethis_Statement(p):
            print("TerminateThis Statement")

        @self.pg.production('Expression : Term')
        @self.pg.production('Expression : Expression Delimiter Add_Op Delimiter Factor')
        def Expression(p):
            print("Expression")

        @self.pg.production('Add_Op : Plus')
        @self.pg.production('Add_Op : Minus')
        def Add_Op(p):
            print("Add OP")

        @self.pg.production('Term : Factor')
        @self.pg.production('Term : Expression Delimiter Mul_Op Delimiter Factor')
        def Term(p):
            print("Term")

        @self.pg.production('Mul_Op : Mult')
        @self.pg.production('Mul_Op : Div')
        def Mul_Op(p):
            print("Mul OP")

        @self.pg.production('Factor : Identifier')
        @self.pg.production('Factor : Number')
        def Factor(p):
            print("Factor")
        
        @self.pg.production('Comment : Comment_Block_Start Identifier Comment_Block_End')
        @self.pg.production('Comment : Comment_Line Identifier')
        def Comment(p):
            print("Comment")
        
        @self.pg.production('using_command : Inclusion Opened_Bracket F_name Dot Identifier Closed_Parenthesis Delimiter')
        def using_command(p):
            print("Using Commad")
        
        @self.pg.production('F_name : Identifier')
        def F_name(p):
            print("F name")
        
        @self.pg.production('Type : Integer')
        @self.pg.production('Type : SInteger')
        @self.pg.production('Type : Character')
        @self.pg.production('Type : String')  
        @self.pg.production('Type : Float')  
        @self.pg.production('Type : SFloat') 
        @self.pg.production('Type : Void')
        def Type(p):
            print ("Type")   


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
