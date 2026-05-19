from antlr4 import *
from src import MyGrammerLexer,MyGrammerParser,MyGrammerListener

def main():
    lexer = MyGrammerLexer(FileStream('test002.txt'))
    stream = CommonTokenStream(lexer)
    parser = MyGrammerParser(stream)
    tree = parser.program()

    listener = MyGrammerListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
