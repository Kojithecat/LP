from antlr4 import *

if __name__ is not None and "." in __name__:
    from .ExprVisitor import ExprVisitor
else:
    from ExprVisitor import ExprVisitor

if __name__ is not None and "." in __name__:
    from .ExprLexer import ExprLexer
else:
    from ExprLexer import ExprLexer

if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

def pasarText(message):
    l = list(message.split("\n"))
    res = ""
    for msg in l:
        ExprVisitor.result = ""
        input_stream = InputStream(msg)
        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)
        tree = parser.root()
        visitor = ExprVisitor()
        visitor.visit(tree)
        print(visitor.result)
        if(visitor.result != ""):
            res += ExprVisitor.result
            res += "\n"
    print(res)
    return res

