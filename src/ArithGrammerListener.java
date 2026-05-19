// Generated from ArithGrammer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ArithGrammerParser}.
 */
public interface ArithGrammerListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ArithGrammerParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ArithGrammerParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArithGrammerParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ArithGrammerParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ArithGrammerParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(ArithGrammerParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArithGrammerParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(ArithGrammerParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ArithGrammerParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(ArithGrammerParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArithGrammerParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(ArithGrammerParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link ArithGrammerParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(ArithGrammerParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ArithGrammerParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(ArithGrammerParser.TypeContext ctx);
}