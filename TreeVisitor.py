if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor


class Visitor(ExprVisitor):

    def __init__(self):
        self.nivell = 0
        self.variables = [{}] # Stack of dictionaries
        self.func_dict = {}
        # self.contextStack = []
    
    def visitRoot(self, ctx:ExprParser.RootContext):
        print("## visitRoot")
        l = list(ctx.getChildren())
        return self.visit(l[0])

    # Visit a parse tree produced by ExprParser#DeclareFunction.
    def visitDeclareFunction(self, ctx:ExprParser.DeclareFunctionContext):
        print("## visitDeclareFunction")

        l = list(ctx.getChildren())
        functionName = l[0].getText()
        parametersList = []
        i = 1
        while l[i].getText() != "{":
            parametersList.append(l[i].getText())
            i += 1
        
        instrucBloc = l[i]

        if functionName in self.func_dict:
            errorMsg = "Procedure with name '{}' already defined"
            raise Exception(errorMsg.format(functionName))
        
        parametersSet = set(parametersList)
        if not(len(parametersList) == len(parametersSet)):
            errorMsg = "Some parameters in function '{}' have the same name"
            raise Exception(errorMsg.format(functionName))

        self.func_dict[functionName] = (parametersList, instrucBloc)

    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        """Visit a block of instructions. Stop when a value is returned."""
        print("## visitBlock")
        l = list(ctx.getChildren())
        for instruc in l:
            value = self.visit(instruc)
            if value is not None:
                return value


    # Visit a parse tree produced by ExprParser#write.
    def visitWrite(self, ctx:ExprParser.WriteContext):
        print("## visitWrite")
        l = list(ctx.getChildren())
        return self.visit(l[0])
    
    # Visit a parse tree produced by ExprParser#assignation.
    def visitAssignation(self, ctx:ExprParser.AssignationContext):
        print("## visitAssignation")
        l = list(ctx.getChildren())
        varName = l[0].getText()
        varValue = self.visit(l[2])
        self.variables[-1][varName] = varValue
    
    # Visit a parse tree produced by ExprParser#if.
    def visitIf(self, ctx:ExprParser.IfContext):
        print("## visitIf")
        l = list(ctx.getChildren())
        condition = self.visit(l[1])
        if condition:
            self.visit(l[3])

    # Visit a parse tree produced by ExprParser#ifElse.
    def visitIfElse(self, ctx:ExprParser.IfElseContext):
        print("## visitIfElse")
        l = list(ctx.getChildren())
        condition = self.visit(l[1])
        if condition:
            self.visit(l[3])
        else:
            self.visit(l[5])
    
    # Visit a parse tree produced by ExprParser#while.
    def visitWhile(self, ctx:ExprParser.WhileContext):
        print("## visitWhile")
        l = list(ctx.getChildren())
        condition = self.visit(l[1])
        while condition:
            self.visit(l[3])
            condition = self.visit(l[1])

    # Visit a parse tree produced by ExprParser#lessExpr.
    def visitLessExpr(self, ctx:ExprParser.LessExprContext):
        print("## visitLessExpr")
        l = list(ctx.getChildren())
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            return a < b
        else:
            print("Error evaluating less expression!")
            return False
    
    # Visit a parse tree produced by ExprParser#greaterEqualExpr.
    def visitGreaterEqualExpr(self, ctx:ExprParser.GreaterEqualExprContext):
        print("## visitGreaterEqualExpr")
        l = list(ctx.getChildren())
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            return a >= b
        else:
            print("Error evaluating greaterEqual expression!")
            return False
    
    # Visit a parse tree produced by ExprParser#differentExpr.
    def visitDifferentExpr(self, ctx:ExprParser.DifferentExprContext):
        print("## visitDifferentExpr")
        l = list(ctx.getChildren())
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            return a != b
        else:
            print("Error evaluating different expression!")
            return False

    # Visit a parse tree produced by ExprParser#lessEqualExpr.
    def visitLessEqualExpr(self, ctx:ExprParser.LessEqualExprContext):
        print("## visitLessEqualExpr")
        l = list(ctx.getChildren())
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            return a <= b
        else:
            print("Error evaluating lessEqual expression!")
            return False

    # Visit a parse tree produced by ExprParser#varExpr.
    def visitVarExpr(self, ctx:ExprParser.VarExprContext):
        print("## visitVarExpr")
        varName = ctx.getText()
        if varName in self.variables:
            return self.variables[-1][varName]
        else:
            errorMsg = "Error, variable {} not defined!"
            raise Exception(errorMsg.format(varName))
    
    # Visit a parse tree produced by ExprParser#greaterExpr.
    def visitGreaterExpr(self, ctx:ExprParser.GreaterExprContext):
        print("## visitGreaterExpr")
        l = list(ctx.getChildren())
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            return a > b
        else:
            print("Error evaluating greater expression!")
            return False

    # Visit a parse tree produced by ExprParser#addExpr.
    def visitAddExpr(self, ctx:ExprParser.AddExprContext):
        print("## visitAddExpr")
        l = list(ctx.getChildren())
        sumVar = 0
        #print("expr length",len(l))
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            sumVar = a+b
        else:
            print("Error evaluating sum expression!")
        # print("sum",sumVar)
        return sumVar
    
    # Visit a parse tree produced by ExprParser#functionCall.
    def visitFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        print("## visitFunctionCall")

        l = list(ctx.getChildren())
        functionName = l[0].getText()

        # Visit the parameters according to the function definition
        parametersList = []
        param_count = len(self.func_dict[functionName][0])
        for i in range(1, 1+param_count):
            parametersList.append(self.visit(l[i]))

        if functionName not in self.func_dict:
            errorMsg = "Procedure with name '{}' not defined"
            raise Exception(errorMsg.format(functionName))
        
        parametersSet = set(parametersList)

        if not(len(parametersList) == len(parametersSet)):
            errorMsg = "Some parameters in function '{}' have the same name"
            raise Exception(errorMsg.format(functionName))
        
        parametersList, instrucBloc = self.func_dict[functionName]
        if not(len(parametersList) == len(parametersSet)):
            errorMsg = "Some parameters in function '{}' have the same name"
            raise Exception(errorMsg.format(functionName))
        
        d ={}
        values = list(parametersSet)
        for i in range(param_count):
            d[parametersList[i]] = values[i]
        
        self.variables.append(d)

        ret = self.visit(instrucBloc)

        self.variables.pop()

        return ret
    
    # Visit a parse tree produced by ExprParser#mulExpr.
    def visitMulExpr(self, ctx:ExprParser.MulExprContext):
        print("## visitMulExpr")
        l = list(ctx.getChildren())
        mulVar = 0
        #print("expr length",len(l))
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            mulVar = a*b
        else:
            print("Error evaluating multiplication expression!")
        return mulVar

    # Visit a parse tree produced by ExprParser#divExpr.
    def visitDivExpr(self, ctx:ExprParser.DivExprContext):
        print("## visitDivExpr")
        l = list(ctx.getChildren())
        divVar = 0
        #print("expr length",len(l))
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            if b == 0:
                errorMsg = "Error, division by zero! in expression: {}"
                expression = "{}/{}".format(l[0].getText(), l[2].getText())
                raise Exception(errorMsg.format(expression))
            else:
                divVar = a/b
        else:
            print("Error evaluating division expression!")
        return divVar

    # Visit a parse tree produced by ExprParser#powExpr.
    def visitPowExpr(self, ctx:ExprParser.PowExprContext):
        print("## visitPowExpr")
        l = list(ctx.getChildren())
        powVar = 0
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            powVar = a**b
        else:
            print("Error evaluating power expression!")
        return powVar

    # Visit a parse tree produced by ExprParser#subExpr.
    def visitSubExpr(self, ctx:ExprParser.SubExprContext):
        print("## visitSubExpr")
        l = list(ctx.getChildren())
        difVar = 0
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            difVar = a-b
        else:
            print("Error evaluating difference expression!")
        return difVar
    
    # Visit a parse tree produced by ExprParser#numExpr.
    def visitNumExpr(self, ctx:ExprParser.NumExprContext):
        print("## visitNumExpr")
        l = list(ctx.getChildren())
        return int(l[0].getText())
    
    # Visit a parse tree produced by ExprParser#equalExpr.
    def visitEqualExpr(self, ctx:ExprParser.EqualExprContext):
        print("## visitEqualExpr")
        l = list(ctx.getChildren())
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            return a == b
        else:
            print("Error evaluating equal expression!")
            return False
    
    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        print("## visitAssign")
        return self.visitChildren(ctx)
