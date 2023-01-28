if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

class VisitorError():
    def __init__(self, msg):
        self.msg = msg

class Visitor(ParseTreeVisitor):
    """
    A visitor for the parse tree produced by funxParser.
    Attributes
    ----------
    variables : list
        Stack of dictionaries. Each dictionary represents a scope.
    func_dict : dict
        Dictionary of functions. Each function is a tuple of two elements:
        a list of parameters and a block of instructions.
    operations : dict
        Dictionary of operations. Each operation is a function that takes
        two arguments and returns a value.
    Methods
    -------
    reset()
        Reset the visitor. Clear the stack of dictionaries and the function
        dictionary.
    visitRoot(ctx)
        Visit the root of the parse tree and return the result of the
        evaluation.
    visitOperation(ctx)
        Generic method to visit an operation. The operation is determined
        by the context (length of the children and symbol).
    All the other methods are self-explanatory.
    """

    def __init__(self):
        self.variables = []  # Stack of dictionaries
        self.func_dict = {}  # Dictionary of functions (name, ([param], block))
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a // b,
            "%": lambda a, b: a % b,
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
            "!": lambda a: not a,
            "not": lambda a: not a
        }

    def reset(self):
        self.variables = []
        self.func_dict = {}

    def visitRoot(self, ctx: funxParser.RootContext):
        children = list(ctx.getChildren())
        ret = None
        i = 0
        n = len(children)
        while i < n and ret is None:
            ret = self.visit(children[i])
            i += 1
        return ret

    def visitDeclareFunction(self, ctx: funxParser.DeclareFunctionContext):
        print("Declare function")
        children = list(ctx.getChildren())
        functionName = children[0].getText()
        parametersList = []
        i = 1
        while children[i].getText() != "{":
            parametersList.append(children[i].getText())
            i += 1

        instrucBlock = children[i+1]

        if functionName in self.func_dict:
            errorMsg = "Function with name '{}' already defined"
            return VisitorError(errorMsg.format(functionName))

        parametersSet = set(parametersList)
        if not (len(parametersList) == len(parametersSet)):
            errorMsg = "Some parameters in function '{}' have the same name"
            return VisitorError(errorMsg.format(functionName))

        self.func_dict[functionName] = (parametersList, instrucBlock)

    def visitBlock(self, ctx: funxParser.BlockContext):
        """Visit a block of instructions. Stop when a value is returned."""
        children = list(ctx.getChildren())
        ret = None
        i = 0
        n = len(children)
        while i < n and ret is None:
            ret = self.visit(children[i])
            i += 1
        return ret

    def visitParenthesizedInstruc(self, ctx: funxParser.ParenthesizedInstrucContext):
        try:
            children = list(ctx.getChildren())
            return self.visit(children[1])
        except Exception as e:
            error = "Error in parenthesized instruction: " + str(e)
            return VisitorError(error)

    def visitWrite(self, ctx: funxParser.WriteContext):
        children = list(ctx.getChildren())
        ret = self.visit(children[0])
        if ret is not None:
            return ret

    def visitAssignation(self, ctx: funxParser.AssignationContext):
        children = list(ctx.getChildren())
        varName = children[0].getText()
        varValue = self.visit(children[2])
        self.variables[-1][varName] = varValue

    def visitConditional(self, ctx: funxParser.ConditionalContext):
        children = list(ctx.getChildren())
        condition = self.visit(children[1])
        if len(children) == 5:
            if condition:
                return self.visit(children[3])
        else:
            if condition:
                return self.visit(children[3])
            else:
                return self.visit(children[7])

    def visitWhile(self, ctx: funxParser.WhileContext):
        children = list(ctx.getChildren())
        condition = self.visit(children[1])
        while condition:
            ret = self.visit(children[3])
            if ret is not None:
                return ret
            condition = self.visit(children[1])
        return

    def visitVarExpr(self, ctx: funxParser.VarExprContext):
        try:
            varName = ctx.getText()
            # If the variable does not exist, return 0 (task requirement)
            if len(self.variables) == 0:
                return 0
            if varName in self.variables[-1]:
                return self.variables[-1][varName]
            return 0
        except Exception as e:
            return VisitorError("Error evaluating variable expression: " + str(e))

    def visitParenthesizedExpr(self, ctx: funxParser.ParenthesizedExprContext):
        children = list(ctx.getChildren())
        return self.visit(children[1])

    def visitFunctionCall(self, ctx: funxParser.FunctionCallContext):
        children = list(ctx.getChildren())
        functionName = children[0].getText()
        values = []
        try:
            param_count = len(self.func_dict[functionName][0])
        except KeyError:
            return VisitorError("Function '{}' not defined".format(functionName))
        for i in range(1, 1+param_count):
            values.append(self.visit(children[i]))
        parametersList, instrucBlock = self.func_dict[functionName]
        if len(values) != param_count:
            errorMsg = "Wrong number of parameters in function '{}', expected {}, but {} were given"
            return VisitorError(errorMsg.format(functionName, param_count, len(values)))
        d = {}
        for i in range(param_count):
            d[parametersList[i]] = values[i]
        # add the new variables to the stack
        self.variables.append(d)
        # visit the instructions block
        ret = self.visit(instrucBlock)
        # remove the variables from the stack
        self.variables.pop()
        return ret

    def visitOperationExpr(self, ctx: funxParser.OperationExprContext):
        try:
            children = list(ctx.getChildren())
            # Binary operation
            if len(children) == 3:
                a = self.visit(children[0])
                b = self.visit(children[2])
                symbol = children[1].getText()
                if isinstance(a, VisitorError):
                    return a
                if isinstance(b, VisitorError):
                    return b
                return int(self.operations[symbol](a, b))
            # Unary operation
            elif len(children) == 2:
                a = self.visit(children[1])
                symbol = children[0].getText()
                if isinstance(a, VisitorError):
                    return a
                return int(self.operations[symbol](a))
        except Exception as e:
            return VisitorError("Error evaluating binary expression: " + str(e))

    def visitNegativeExpr(self, ctx: funxParser.NegativeExprContext):
        children = list(ctx.getChildren())
        a = self.visit(children[1])
        if isinstance(a, VisitorError):
            return a
        return -a

    def visitBoolExpr(self, ctx: funxParser.BoolExprContext):
        children = list(ctx.getChildren())
        return int(children[0].getText() == "true")

    def visitNumExpr(self, ctx: funxParser.NumExprContext):
        children = list(ctx.getChildren())
        return int(children[0].getText())