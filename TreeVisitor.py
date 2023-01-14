if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

class VisitorError():
    def __init__(self, msg):
        self.msg = msg

class Visitor(ExprVisitor):

    def __init__(self):
        self.variables = [] # Stack of dictionaries
        self.func_dict = {}
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
    
    def reset(self):
        self.variables = []
        self.func_dict = {}

    def visitRoot(self, ctx:ExprParser.RootContext):
        l = list(ctx.getChildren())
        return self.visit(l[0])

    def visitDeclareFunction(self, ctx:ExprParser.DeclareFunctionContext):
        l = list(ctx.getChildren())
        functionName = l[0].getText()
        parametersList = []
        i = 1
        while l[i].getText() != "{":
            parametersList.append(l[i].getText())
            i += 1
        
        instrucBlock = l[i+1]

        if functionName in self.func_dict:
            errorMsg = "Function with name '{}' already defined"
            return VisitorError(errorMsg.format(functionName))

        parametersSet = set(parametersList)
        if not(len(parametersList) == len(parametersSet)):
            errorMsg = "Some parameters in function '{}' have the same name"
            return VisitorError(errorMsg.format(functionName))

        self.func_dict[functionName] = (parametersList, instrucBlock)

    def visitBlock(self, ctx:ExprParser.BlockContext):
        """Visit a block of instructions. Stop when a value is returned."""
        l = list(ctx.getChildren())
        ret = None
        i = 0
        n = len(l)
        while i < n and ret is None:
            ret = self.visit(l[i])
            i += 1
        return ret

    def visitBinaryExpr(self, ctx):
        try:
            l = list(ctx.getChildren())
            if len(l) == 3:
                a = self.visit(l[0])
                b = self.visit(l[2])
                symbol = l[1].getText()
                return int(self.operations[symbol](a, b))
        except Exception as e:
            return VisitorError("Error evaluating binary expression: " + str(e))

    def visitParenthesizedInstruc(self, ctx:ExprParser.ParenthesizedInstrucContext):
        try:
            l = list(ctx.getChildren())
            if len(l) == 3:
                return self.visit(l[1])
        except Exception as e:
            error = "Error in parenthesized instruction: " + str(e)
            return VisitorError(error)
        return VisitorError("Error in parenthesized instruction")

    def visitWrite(self, ctx:ExprParser.WriteContext):
        l = list(ctx.getChildren())
        ret = self.visit(l[0])
        if ret is not None:
            return ret

    def visitAssignation(self, ctx:ExprParser.AssignationContext):
        l = list(ctx.getChildren())
        varName = l[0].getText()
        varValue = self.visit(l[2])
        self.variables[-1][varName] = varValue

    def visitIf(self, ctx:ExprParser.IfContext):
        l = list(ctx.getChildren())
        condition = self.visit(l[1])
        if condition:
            return self.visit(l[3])

    def visitIfElse(self, ctx:ExprParser.IfElseContext):
        l = list(ctx.getChildren())
        condition = self.visit(l[1])
        if condition:
            ret = self.visit(l[3])
        else:
            ret = self.visit(l[7])
        if ret is not None:
            return ret

    def visitWhile(self, ctx:ExprParser.WhileContext):
        l = list(ctx.getChildren())
        condition = self.visit(l[1])
        while condition:
            ret = self.visit(l[3])
            if ret is not None:
                return ret
            condition = self.visit(l[1])
        return

    def visitVarExpr(self, ctx:ExprParser.VarExprContext):
        varName = ctx.getText()
        if varName in self.variables[-1]:
            return self.variables[-1][varName]
        else:
            errorMsg = "Error, variable {} not defined!"
            return VisitorError(errorMsg.format(varName))

    def visitNotExpr(self, ctx:ExprParser.NotExprContext):
        l = list(ctx.getChildren())
        if len(l) == 2:
            a = self.visit(l[1])
            return not a
        error_mg =  "Error evaluating not expression!"
        return VisitorError(error_mg)

    def visitSumExpr(self, ctx:ExprParser.SumExprContext):
        return self.visitBinaryExpr(ctx)

    def visitParenthesizedExpr(self, ctx:ExprParser.ParenthesizedExprContext):
        l = list(ctx.getChildren())
        if len(l) == 3:
            return self.visit(l[1])
        else:
            return VisitorError("Parenthesized expression with wrong number of children")

    def visitFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        l = list(ctx.getChildren())
        functionName = l[0].getText()
        values = []
        try:
            param_count = len(self.func_dict[functionName][0])
        except:
            return VisitorError("Function '{}' not defined".format(functionName))
        for i in range(1, 1+param_count):
            values.append(self.visit(l[i]))
        parametersList, instrucBlock = self.func_dict[functionName]
        if len(values) != param_count:
            errorMsg = "Wrong number of parameters in function '{}', expected {}, but {} were given"
            return VisitorError(errorMsg.format(functionName, param_count, len(values)))
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
        l = list(ctx.getChildren())
        return int(l[0].getText())
