# Generated from ArithGrammer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithGrammerParser import ArithGrammerParser
else:
    from ArithGrammerParser import ArithGrammerParser

# This class defines a complete listener for a parse tree produced by ArithGrammerParser.
class ArithGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by ArithGrammerParser#prog.
    def enterProg(self, ctx:ArithGrammerParser.ProgContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#prog.
    def exitProg(self, ctx:ArithGrammerParser.ProgContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#func_list.
    def enterFunc_list(self, ctx:ArithGrammerParser.Func_listContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#func_list.
    def exitFunc_list(self, ctx:ArithGrammerParser.Func_listContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#func_def.
    def enterFunc_def(self, ctx:ArithGrammerParser.Func_defContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#func_def.
    def exitFunc_def(self, ctx:ArithGrammerParser.Func_defContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#param_list.
    def enterParam_list(self, ctx:ArithGrammerParser.Param_listContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#param_list.
    def exitParam_list(self, ctx:ArithGrammerParser.Param_listContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#param.
    def enterParam(self, ctx:ArithGrammerParser.ParamContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#param.
    def exitParam(self, ctx:ArithGrammerParser.ParamContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#data_type.
    def enterData_type(self, ctx:ArithGrammerParser.Data_typeContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#data_type.
    def exitData_type(self, ctx:ArithGrammerParser.Data_typeContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#code_block.
    def enterCode_block(self, ctx:ArithGrammerParser.Code_blockContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#code_block.
    def exitCode_block(self, ctx:ArithGrammerParser.Code_blockContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#stmt_list.
    def enterStmt_list(self, ctx:ArithGrammerParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#stmt_list.
    def exitStmt_list(self, ctx:ArithGrammerParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#decide.
    def enterDecide(self, ctx:ArithGrammerParser.DecideContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#decide.
    def exitDecide(self, ctx:ArithGrammerParser.DecideContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#stmt.
    def enterStmt(self, ctx:ArithGrammerParser.StmtContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#stmt.
    def exitStmt(self, ctx:ArithGrammerParser.StmtContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#loop.
    def enterLoop(self, ctx:ArithGrammerParser.LoopContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#loop.
    def exitLoop(self, ctx:ArithGrammerParser.LoopContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#loop_stmt.
    def enterLoop_stmt(self, ctx:ArithGrammerParser.Loop_stmtContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#loop_stmt.
    def exitLoop_stmt(self, ctx:ArithGrammerParser.Loop_stmtContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#init_stmt.
    def enterInit_stmt(self, ctx:ArithGrammerParser.Init_stmtContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#init_stmt.
    def exitInit_stmt(self, ctx:ArithGrammerParser.Init_stmtContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#post_stmt.
    def enterPost_stmt(self, ctx:ArithGrammerParser.Post_stmtContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#post_stmt.
    def exitPost_stmt(self, ctx:ArithGrammerParser.Post_stmtContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#var_list.
    def enterVar_list(self, ctx:ArithGrammerParser.Var_listContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#var_list.
    def exitVar_list(self, ctx:ArithGrammerParser.Var_listContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#var.
    def enterVar(self, ctx:ArithGrammerParser.VarContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#var.
    def exitVar(self, ctx:ArithGrammerParser.VarContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#expr.
    def enterExpr(self, ctx:ArithGrammerParser.ExprContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#expr.
    def exitExpr(self, ctx:ArithGrammerParser.ExprContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#unop.
    def enterUnop(self, ctx:ArithGrammerParser.UnopContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#unop.
    def exitUnop(self, ctx:ArithGrammerParser.UnopContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#and.
    def enterAnd(self, ctx:ArithGrammerParser.AndContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#and.
    def exitAnd(self, ctx:ArithGrammerParser.AndContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#or.
    def enterOr(self, ctx:ArithGrammerParser.OrContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#or.
    def exitOr(self, ctx:ArithGrammerParser.OrContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#args.
    def enterArgs(self, ctx:ArithGrammerParser.ArgsContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#args.
    def exitArgs(self, ctx:ArithGrammerParser.ArgsContext):
        pass


    # Enter a parse tree produced by ArithGrammerParser#number.
    def enterNumber(self, ctx:ArithGrammerParser.NumberContext):
        pass

    # Exit a parse tree produced by ArithGrammerParser#number.
    def exitNumber(self, ctx:ArithGrammerParser.NumberContext):
        pass



del ArithGrammerParser