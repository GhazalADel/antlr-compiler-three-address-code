# Generated from MyGrammer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete listener for a parse tree produced by MyGrammerParser.
class MyGrammerListener(ParseTreeListener):

    def __init__(self):
        self.current_function_index = 0
        self.function_names = set()
        self.has_duplicate_function = False
        self.duplicate_functions_indices = []
        self.has_main_function = -1 # -1 : initial 0 : no 1 : yes 
        self.has_invalid_return_type = False
        self.invalid_return_type_code = []
        self.valid_types = ["void", "boolean", "int", "double"]
        self.scope_stack = []

    # Enter a parse tree produced by MyGrammerParser#program.
    def enterProgram(self, ctx:MyGrammerParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#program.
    def exitProgram(self, ctx:MyGrammerParser.ProgramContext):
        ctx.code = ctx.func_list().code
        print(ctx.code)

    # Enter a parse tree produced by MyGrammerParser#func_list.
    def enterFunc_list(self, ctx:MyGrammerParser.Func_listContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#func_list.
    def exitFunc_list(self, ctx:MyGrammerParser.Func_listContext):
        if ctx.func_list_prime():
            func_def_code = ctx.func_def().code
            func_list_prime_code = ctx.func_list_prime().code
            ctx.code = func_def_code + "\n" + func_list_prime_code

            if "main" not in ctx.code:
                self.has_main_function = False
                raise TypeError("There is no main function in your program.")
            else:
                ctx.code = self.move_main_to_front(ctx.code)

        else:
            ctx.code = ctx.func_def().code

            if ctx.func_def().ID().getText() != "main":
                self.has_main_function = False
                raise TypeError("There is no main function in your program.")
            else:
                ctx.code = "main\n" + ctx.func_def().code


    def move_main_to_front(self, code):
        lines = code.splitlines()
        main_index = next((i for i, line in enumerate(lines) if "main" in line), None)
        if main_index is not None and main_index != 0:
            main_function = lines.pop(main_index)
            lines.insert(0, main_function)
            return "\n".join(lines)
        return code

   
    # Enter a parse tree produced by MyGrammerParser#func_list_prime.
    def enterFunc_list_prime(self, ctx:MyGrammerParser.Func_list_primeContext):
        ctx.code = ctx.func_def().code if ctx.func_def() else ""

    # Exit a parse tree produced by MyGrammerParser#func_list_prime.
    def exitFunc_list_prime(self, ctx:MyGrammerParser.Func_list_primeContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#func_def.
    def enterFunc_def(self, ctx:MyGrammerParser.Func_defContext):
        self.scope_stack.append({})
        self.scope_stack[-1]['_outer'] = self.scope_stack[-2] if len(self.scope_stack) > 1 else None

        name = ctx.ID().getText()
        return_type = ctx.data_type().getText()

        initial_size = len(self.function_names)
        self.function_names.add(name)
        if len(self.function_names) == initial_size:
            self.has_duplicate_function = True
            self.duplicate_functions_indices.append(self.current_function_index)

        if name == "main":
            self.has_main_function = 1

        if return_type not in self.valid_types:
            self.has_invalid_return_type = True
            self.invalid_return_type_code.append(self.current_function_index)
        
        param_list_code = ctx.param_list().code if ctx.param_list() else ""
        param_assignments = ""
        params = ctx.param_list().param() if ctx.param_list() else []
        for _, param in enumerate(params):
            param_type = param.data_type().getText()
            param_assignments += f"m[top+{self.memory_index}].{param_type} = m[top+{self.memory_index}].{param_type};\n"
            self.memory_index += 1
        ctx.code = f"{ctx.data_type().getText()} {ctx.ID().getText()}({param_list_code}) {{\n"
        ctx.code += param_assignments

        self.current_function_index += 1
    

    # Exit a parse tree produced by MyGrammerParser#func_def.
    def exitFunc_def(self, ctx:MyGrammerParser.Func_defContext):
        return_type = ctx.data_type().getText()
        function_name = ctx.ID().getText()
        code_block_code = ctx.code_block().code

        if not return_type:
            raise TypeError(f"Function '{function_name}' is missing a return type.")
        
        if return_type == "void" and "return" in code_block_code:
            raise TypeError(f"Function '{function_name}' has return statements but its return type is 'void'.")

        ctx.code = f"{return_type} {function_name}({ctx.param_list().code}) {code_block_code}"
        self.current_function_index += 1
        self.scope_stack.pop()

    # Enter a parse tree produced by MyGrammerParser#param_list.
    def enterParam_list(self, ctx:MyGrammerParser.Param_listContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#param_list.
    def exitParam_list(self, ctx:MyGrammerParser.Param_listContext):
        if ctx.param_list_prime():
            ctx.code = ctx.param().code + ", " + ctx.param_list_prime().code
        else:
            ctx.code = ctx.param().code


    # Enter a parse tree produced by MyGrammerParser#param_list_prime.
    def enterParam_list_prime(self, ctx:MyGrammerParser.Param_list_primeContext):
        ctx.code = ctx.param_list().code

    # Exit a parse tree produced by MyGrammerParser#param_list_prime.
    def exitParam_list_prime(self, ctx:MyGrammerParser.Param_list_primeContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#param.
    def enterParam(self, ctx:MyGrammerParser.ParamContext):
        param_name = ctx.ID().getText()
        param_type = ctx.type().getText()
        if param_type not in ["boolean", "int", "double"] or not param_type:
            raise TypeError(f"Unsupported parameter type: {param_type}")
        
        if param_name in self.scope_stack[-1]:
            raise ValueError(f"Duplicate variable definition: {param_name}")
        self.scope_stack[-1][param_name] = param_type
        
    # Exit a parse tree produced by MyGrammerParser#param.
    def exitParam(self, ctx:MyGrammerParser.ParamContext):
        ctx.code = f"{ctx.data_type().getText()} {ctx.ID().getText()}"

    # Enter a parse tree produced by MyGrammerParser#data_type.
    def enterData_type(self, ctx:MyGrammerParser.Data_typeContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#data_type.
    def exitData_type(self, ctx:MyGrammerParser.Data_typeContext):
        data_type = ctx.getText()

        if data_type not in self.valid_types:
            raise TypeError(f"Unsupported data type: {data_type}")

        ctx.code = data_type


    # Enter a parse tree produced by MyGrammerParser#code_block.
    def enterCode_block(self, ctx:MyGrammerParser.Code_blockContext):
       pass

    # Exit a parse tree produced by MyGrammerParser#code_block.
    def exitCode_block(self, ctx:MyGrammerParser.Code_blockContext):
        stmt_list_code = ctx.stmt_list().code if ctx.stmt_list() else ""
        ctx.code = f"{{\n{stmt_list_code}\n}}"
    

    # Enter a parse tree produced by MyGrammerParser#stmt_list.
    def enterStmt_list(self, ctx:MyGrammerParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#stmt_list.
    def exitStmt_list(self, ctx:MyGrammerParser.Stmt_listContext):
        if ctx.stmt_list():
            ctx.code = ctx.stmt().code + "\n" + ctx.stmt_list().code
        else:
            ctx.code = ctx.stmt().code


    # Enter a parse tree produced by MyGrammerParser#decide.
    def enterDecide(self, ctx:MyGrammerParser.DecideContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#decide.
    def exitDecide(self, ctx:MyGrammerParser.DecideContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#stmt.
    def enterStmt(self, ctx:MyGrammerParser.StmtContext):
        if ctx.data_type() and ctx.var_list():
            data_type = ctx.data_type().getText()
            var_list = ctx.var_list().code.split(',')
            for var_name in var_list:
                if var_name.strip() in self.scope_stack[-1]:
                    raise ValueError(f"Duplicate variable definition: {var_name.strip()}")
                self.scope_stack[-1][var_name.strip()] = data_type
    
    def get_variable_type(self, var_name):
        # Search for variable type from current scope to outer scopes
        for scope in reversed(self.scope_stack):
            if var_name in scope:
                return scope[var_name]
        return None  # Variable not found

    # Exit a parse tree produced by MyGrammerParser#stmt.
    def exitStmt(self, ctx:MyGrammerParser.StmtContext):
        if ctx.SEMICOLON():
            ctx.code = ";"
        elif ctx.code_block():
            ctx.code = ctx.code_block().code
        elif ctx.data_type():
            ctx.code = f"{ctx.data_type().getText()} {ctx.var_list().code};"
        elif ctx.ID() and ctx.expr():
            var_name = ctx.ID().getText()
            var_type = self.get_variable_type(var_name) 
            expr_type = ctx.expr().type  

            if var_type != expr_type:
                raise TypeError(f"Type mismatch: Cannot assign {expr_type} to {var_type}")

            ctx.code = f"{var_name} = {ctx.expr().code};"
        elif ctx.ID() and ctx.getChild(1).getText() == "++":
            ctx.code = f"{ctx.ID().getText()}++;"
        elif ctx.ID() and ctx.getChild(1).getText() == "--":
            ctx.code = f"{ctx.ID().getText()}--;"
        elif ctx.getChild(0).getText() == "return":
            if ctx.stmt_return_prime().expr():
                return_expr_type = ctx.stmt_return_prime().expr().type
                if return_expr_type != self.current_function_return_type:
                    raise TypeError(f"Return type mismatch: Expected {self.current_function_return_type}, but got {return_expr_type}")

                ctx.code = f"return {ctx.stmt_return_prime().expr().code};"
            else:
                if self.current_function_return_type != "void":
                    raise TypeError(f"Return type mismatch: Expected {self.current_function_return_type}, but found 'void'")
                ctx.code = "return;"
        elif ctx.decide() and ctx.expr() and ctx.stmt():
            condition_type = ctx.expr().type
            if condition_type != "boolean":
                raise TypeError(f"If statement condition must be boolean, but got {condition_type}")

            condition_code = ctx.expr().code
            if_statement = ctx.stmt(0).code
            if ctx.stm_decide_prime().getChildCount() > 0:
                else_statement = ctx.stmt(1).code
                ctx.code = f"if ({condition_code}) {{\n{if_statement}}} else {{\n{else_statement}}}"
            else:
                ctx.code = f"if ({condition_code}) {{\n{if_statement}}}"
        elif ctx.loop_stmt():
            ctx.code = ctx.loop_stmt().code
        elif ctx.expr():
            ctx.code = f"{ctx.expr().code};"
        elif ctx.init_stmt():
            ctx.code = f"{ctx.init_stmt().code};"


    # Enter a parse tree produced by MyGrammerParser#stmt_return_prime.
    def enterStmt_return_prime(self, ctx:MyGrammerParser.Stmt_return_primeContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#stmt_return_prime.
    def exitStmt_return_prime(self, ctx:MyGrammerParser.Stmt_return_primeContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#stm_decide_prime.
    def enterStm_decide_prime(self, ctx:MyGrammerParser.Stm_decide_primeContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#stm_decide_prime.
    def exitStm_decide_prime(self, ctx:MyGrammerParser.Stm_decide_primeContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#loop.
    def enterLoop(self, ctx:MyGrammerParser.LoopContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#loop.
    def exitLoop(self, ctx:MyGrammerParser.LoopContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#loop_stmt.
    def enterLoop_stmt(self, ctx:MyGrammerParser.Loop_stmtContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#loop_stmt.
    def exitLoop_stmt(self, ctx:MyGrammerParser.Loop_stmtContext):
        condition_code = ctx.expr().code
        loop_body = ctx.stmt().code
        ctx.code = f"while ({condition_code}) {{\n{loop_body}\n}}"


    # Enter a parse tree produced by MyGrammerParser#init_stmt.
    def enterInit_stmt(self, ctx:MyGrammerParser.Init_stmtContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#init_stmt.
    def exitInit_stmt(self, ctx:MyGrammerParser.Init_stmtContext):
        if ctx.data_type():
            ctx.code = f"{ctx.data_type().getText()} {ctx.ID().getText()} = {ctx.expr().code}"
        else:
            ctx.code = f"{ctx.ID().getText()} = {ctx.expr().code}"


    # Enter a parse tree produced by MyGrammerParser#post_stmt.
    def enterPost_stmt(self, ctx:MyGrammerParser.Post_stmtContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#post_stmt.
    def exitPost_stmt(self, ctx:MyGrammerParser.Post_stmtContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#var_list.
    def enterVar_list(self, ctx:MyGrammerParser.Var_listContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#var_list.
    def exitVar_list(self, ctx:MyGrammerParser.Var_listContext):
        if ctx.var_list():
            ctx.code = f"{ctx.var().code}, {ctx.var_list().code}"
        else:
            ctx.code = ctx.var().code


    # Enter a parse tree produced by MyGrammerParser#var.
    def enterVar(self, ctx:MyGrammerParser.VarContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#var.
    def exitVar(self, ctx:MyGrammerParser.VarContext):
        if ctx.var_prime().expr():
            ctx.code = f"{ctx.ID().getText()} = {ctx.var_prime().expr().code}"
        else:
            ctx.code = ctx.ID().getText()


    # Enter a parse tree produced by MyGrammerParser#var_prime.
    def enterVar_prime(self, ctx:MyGrammerParser.Var_primeContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#var_prime.
    def exitVar_prime(self, ctx:MyGrammerParser.Var_primeContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#expr.
    def enterExpr(self, ctx:MyGrammerParser.ExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#expr.
    def exitExpr(self, ctx:MyGrammerParser.ExprContext):
        if ctx.number():
            ctx.code = ctx.number().getText()
        elif ctx.ID():
            if ctx.getChildCount() == 1:
                ctx.code = ctx.ID().getText()
            else:
                args_code = ctx.args().code if ctx.args() else ""
                ctx.code = f"{ctx.ID().getText()}({args_code})"
        elif ctx.getChild(0).getText() == "true":
            ctx.code = "true"
        elif ctx.getChild(0).getText() == "false":
            ctx.code = "false"
        elif ctx.STRING_LIT():
            ctx.code = ctx.STRING_LIT().getText()
        elif ctx.getChild(0).getText() == "(" and ctx.getChild(2).getText() == ")":
            ctx.code = f"({ctx.expr(0).code})"
        elif ctx.unop():
            ctx.code = f"{ctx.unop().getText()}{ctx.expr(0).code}"
        elif ctx.binop():
            left_expr = ctx.expr(0).code
            right_expr = ctx.expr(1).code
            ctx.code = f"{left_expr} {ctx.binop().getText()} {right_expr}"


    # Enter a parse tree produced by MyGrammerParser#args.
    def enterArgs(self, ctx:MyGrammerParser.ArgsContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#args.
    def exitArgs(self, ctx:MyGrammerParser.ArgsContext):
        if ctx.args_prime():
            ctx.code = f"{ctx.expr().code}, {ctx.args_prime().code}"
        else:
            ctx.code = ctx.expr().code



    # Enter a parse tree produced by MyGrammerParser#args_prime.
    def enterArgs_prime(self, ctx:MyGrammerParser.Args_primeContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#args_prime.
    def exitArgs_prime(self, ctx:MyGrammerParser.Args_primeContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#unop.
    def enterUnop(self, ctx:MyGrammerParser.UnopContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#unop.
    def exitUnop(self, ctx:MyGrammerParser.UnopContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#binop.
    def enterBinop(self, ctx:MyGrammerParser.BinopContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#binop.
    def exitBinop(self, ctx:MyGrammerParser.BinopContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#and.
    def enterAnd(self, ctx:MyGrammerParser.AndContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#and.
    def exitAnd(self, ctx:MyGrammerParser.AndContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#or.
    def enterOr(self, ctx:MyGrammerParser.OrContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#or.
    def exitOr(self, ctx:MyGrammerParser.OrContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#number.
    def enterNumber(self, ctx:MyGrammerParser.NumberContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#number.
    def exitNumber(self, ctx:MyGrammerParser.NumberContext):
        ctx.code = ctx.getText()



del MyGrammerParser