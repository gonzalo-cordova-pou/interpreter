if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

class Visitor(ExprVisitor):

    def __init__(self):
        self.nivell = 0
        self.variables = [] # Stack of dictionaries
        self.func_dict = {}
        self.global_i = 0
        # self.contextStack = []

        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a // b,
            "^": lambda a, b: a ** b,
            "=": lambda a, b: a == b,
            "!=": lambda a, b: a != b,
            ">": lambda a, b: a > b,
            "<": lambda a, b: a < b,
            ">=": lambda a, b: a >= b,
            "<=": lambda a, b: a <= b,
            "&&": lambda a, b: a and b,
            "and": lambda a, b: a and b,
            "||": lambda a, b: a or b,
            "or": lambda a, b: a or b,
        }

    def visitRoot(self, ctx:ExprParser.RootContext):
        #print("## visitRoot")
        l = list(ctx.getChildren())
        return self.visit(l[0])

    def visitDeclareFunction(self, ctx:ExprParser.DeclareFunctionContext):
        #print("## visitDeclareFunction")
        l = list(ctx.getChildren())
        functionName = l[0].getText()
        parametersList = []
        i = 1
        while l[i].getText() != "{":
            parametersList.append(l[i].getText())
            i += 1
        
        instrucBlock = l[i+1]

        #print("instrucBlock: {}".format(instrucBlock.getText()))

        if functionName in self.func_dict:
            errorMsg = "Procedure with name '{}' already defined"
            raise Exception(errorMsg.format(functionName))
        
        parametersSet = set(parametersList)
        if not(len(parametersList) == len(parametersSet)):
            errorMsg = "Some parameters in function '{}' have the same name"
            raise Exception(errorMsg.format(functionName))

        self.func_dict[functionName] = (parametersList, instrucBlock)

    def visitBlock(self, ctx:ExprParser.BlockContext):
        """Visit a block of instructions. Stop when a value is returned."""
        #print("## visitBlock")

        self.global_i += 1
        #print("Block {}: {}".format(self.global_i, ctx.getText()))
        l = list(ctx.getChildren())
        ret = None
        i = 0
        n = len(l)
        while i < n and ret is None:
            #print("Block {}: instruction {}, code: {}".format(self.global_i, i, l[i].getText()))
            ret = self.visit(l[i])
            i += 1
        #print("FINISHED Block {}: returning {}".format(self.global_i, ret))
        self.global_i -= 1
        return ret

    def visitBinaryExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 3:
            a = self.visit(l[0])
            b = self.visit(l[2])
            symbol = l[1].getText()
            return int(self.operations[symbol](a, b))
        raise Exception("Error evaluating binary expression!")
    
    def visitParenthesizedInstruc(self, ctx:ExprParser.ParenthesizedInstrucContext):
        #print("## visitParenthesizedInstruc")
        l = list(ctx.getChildren())
        if len(l) == 3:
            return self.visit(l[1])
        else:
            error = "Parenthesized instruction with wrong number of children"
            raise Exception(error)

    def visitWrite(self, ctx:ExprParser.WriteContext):
        #print("## visitWrite")
        l = list(ctx.getChildren())
        ret = self.visit(l[0])
        #print("Write: {}".format(ret))
        if ret is not None:
            return ret

    def visitAssignation(self, ctx:ExprParser.AssignationContext):
        #print("## visitAssignation")
        l = list(ctx.getChildren())
        varName = l[0].getText()
        varValue = self.visit(l[2])
        self.variables[-1][varName] = varValue

    def visitIf(self, ctx:ExprParser.IfContext):
        #print("## visitIf")
        l = list(ctx.getChildren())
        condition = self.visit(l[1])
        if condition:
            return self.visit(l[3])

    def visitIfElse(self, ctx:ExprParser.IfElseContext):
        #print("## visitIfElse")
        l = list(ctx.getChildren())
        #print("Checking if {} is true".format(l[1].getText()))
        condition = self.visit(l[1])
        if condition:
            #print("Condition is true, visiting {}".format(l[3].getText()))
            ret = self.visit(l[3])
        else:
            #print("Condition is false, visiting {}".format(l[7].getText()))
            ret = self.visit(l[7])
        
        if ret is not None:
            return ret

    def visitWhile(self, ctx:ExprParser.WhileContext):
        #print("## visitWhile")
        l = list(ctx.getChildren())
        condition = self.visit(l[1])
        while condition:
            ret = self.visit(l[3])
            if ret is not None:
                return ret
            condition = self.visit(l[1])
        return

    def visitVarExpr(self, ctx:ExprParser.VarExprContext):
        #print("## visitVarExpr")
        varName = ctx.getText()
        if varName in self.variables[-1]:
            #print("Returning value of variable {}".format(varName))
            return self.variables[-1][varName]
        else:
            #print("All current variables: {}".format(self.variables))
            #print("Current variables: {}".format(self.variables[-1]))
            errorMsg = "Error, variable {} not defined!"
            raise Exception(errorMsg.format(varName))

    def visitNotExpr(self, ctx:ExprParser.NotExprContext):
        #print("## visitNot")
        l = list(ctx.getChildren())
        if len(l) == 2:
            a = self.visit(l[1])
            #print("Checking if not {}".format(a))
            return not a
        else:
            error_mg =  "Error evaluating not expression!"
            raise Exception(error_mg)

    def visitSumExpr(self, ctx:ExprParser.SumExprContext):
        return self.visitBinaryExpr(ctx)

    def visitParenthesizedExpr(self, ctx:ExprParser.ParenthesizedExprContext):
        #print("visitParenthesizedExpr")
        l = list(ctx.getChildren())
        #print("length Parent expr:",len(l))
        if len(l) == 3:
            return self.visit(l[1])
        else:
            print("Error in parenthesized expression")

    def visitFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        l = list(ctx.getChildren())
        functionName = l[0].getText()

        # assign the given values to the function variables
        values = []
        try:
            param_count = len(self.func_dict[functionName][0])
        except:
            raise Exception("Function '{}' not defined".format(functionName))
        for i in range(1, 1+param_count):
            values.append(self.visit(l[i]))
        parametersList, instrucBlock = self.func_dict[functionName]
        d ={}
        for i in range(param_count):
            d[parametersList[i]] = values[i]

        # add the new variables to the stack
        self.variables.append(d)
        # visit the instructions block
        ret = self.visit(instrucBlock)
        # remove the variables from the stack
        self.variables.pop()
        
        return ret

    def visitLogicExpr(self, ctx:ExprParser.LogicExprContext):
        return self.visitBinaryExpr(ctx)

    def visitMulExpr(self, ctx:ExprParser.MulExprContext):
        return self.visitBinaryExpr(ctx)

    def visitBoolExpr(self, ctx:ExprParser.BoolExprContext):
        l = list(ctx.getChildren())
        return l[0].getText() == "true"

    def visitPowExpr(self, ctx:ExprParser.PowExprContext):
        return self.visitBinaryExpr(ctx)

    def visitRelationalExpr(self, ctx:ExprParser.RelationalExprContext):
        return self.visitBinaryExpr(ctx)

    def visitNumExpr(self, ctx:ExprParser.NumExprContext):
        #print("## visitNumExpr")
        l = list(ctx.getChildren())
        return int(l[0].getText())
