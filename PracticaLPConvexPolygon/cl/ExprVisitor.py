from random import uniform
from antlr4 import *
import sys
sys.path.append("..")
from Poligon import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.


class ExprVisitor(ParseTreeVisitor):

    dict = {}
    result = ""
    # Visit a parse tree produced by ExprParser#root.

    def visitRoot(self, ctx: ExprParser.RootContext):
        var = self.visitChildren(ctx)
        return var

    # Visit a parse tree produced by ExprParser#command.
    def visitCommand(self, ctx: ExprParser.CommandContext):
        l = [n for n in ctx.getChildren()]
        l0 = l[0].getText()
        l1 = l[1].getText()

        if(l1 == ":="):
            pointlist = self.visit(l[2])
            print(pointlist)
            ExprVisitor.dict[l0] = ConvexPolygon(pointlist)
        if(l0 == "area"):
            pointlist = self.visit(l[1])
            p = ConvexPolygon(pointlist)
            ExprVisitor.result = "{0:.3f}".format(p.area())

        elif(l0 == "centroid"):
            pointlist = self.visit(l[1])
            p = ConvexPolygon(pointlist)
            ExprVisitor.result = "{0:.3f}".format(p.centroid()[0]) + ", " + "{0:.3f}".format(p.centroid()[1])

        elif(l0 == "vertices"):
            pointlist = self.visit(l[1])
            p = ConvexPolygon(pointlist)
            ExprVisitor.result = str(p.vertices())
        elif(l0 == "equal"):
            l1 = self.visit(l[1])
            l2 = self.visit(l[3])
            p1 = ConvexPolygon(l1)
            p2 = ConvexPolygon(l2)
            if(p1.isEqual(p2)):
                print("Yes")
                ExprVisitor.result = "yes"
            else:
                print("No")
                ExprVisitor.result = "no"
        elif(l0 == "inside"):
            l1 = self.visit(l[1])
            l2 = self.visit(l[3])
            p1 = ConvexPolygon(l1)
            p2 = ConvexPolygon(l2)
            if(p2.polygonInside(p1)):
                print("Yes")
                ExprVisitor.result = "yes"
            else:
                print("No")
                ExprVisitor.result = "no"

        elif(l0 == "perimeter"):
            pointlist = self.visit(l[1])
            p = ConvexPolygon(pointlist)
            ExprVisitor.result = "{0:.3f}".format(p.perimeter())

        elif(l0 == "draw"):
            filename = l[1].getText()[1:-1]
            listOfPols = []
            for i in l[3::2]:
                print(i.getText())
                listOfPols.append(ExprVisitor.dict[i.getText()])
            ConvexPolygon.draw(listOfPols, filename)
            ExprVisitor.result = "Created_image: " + filename
        elif(l0 == "color"):
            print(l[1].getText())
            print(l[3].getText())
            col = tuple(map(lambda x: int(x), (l[3].getText()[1:-1].split(' '))))
            print(col)
            ExprVisitor.dict[l1].setColor(col)
            print(ExprVisitor.dict[l1].color)

        elif(l0 == "print"):
            if(l1[0] == '"'):
                word = l1
                print(word[1:-1])
                ExprVisitor.result = word[1:-1]
            elif(l1[0] == '['):
                l = self.visit(l[1])
                p = ConvexPolygon(l)
                s = ""
                for i in p.listaP:
                    s += "{0:.3f}".format(i[0]) + " " + "{0:.3f}".format(i[1]) + " "
                print(s)
                ExprVisitor.result = s

            else:
                l = self.visit(l[1])
                s = ""
                for i in l:
                    s += "{0:.3f}".format(i[0]) + " " + "{0:.3f}".format(i[1]) + " "
                print(s)
                ExprVisitor.result = s

        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx: ExprParser.ExprContext):
        l = [n for n in ctx.getChildren()]
        l0 = l[0].getText()
        if(l0[0] == '[' and l0[-1] == ']'):
            if(len(l0) == 2):
                return []
            return list(map(lambda x: (float(x.split(' ')[0]), float(x.split(' ')[1])), tuple(l0[1:-1].split('  '))))
        elif(l0 == "("):
            return self.visit(l[1])

        elif(len(l) == 1 and l0[0] != '['):
            return ExprVisitor.dict[l0].listaP
        elif(l0 == "#"):
            listap = self.visit(l[1])
            p = ConvexPolygon(listap)
            return p.boundingBox()

        elif(l[1].getText() == "*"):
            listap1 = self.visit(l[0])
            p1 = ConvexPolygon(listap1)
            listap2 = self.visit(l[2])
            p2 = ConvexPolygon(listap2)
            return p2.intersection(p1)

        elif(l[1].getText() == "+"):
            listap1 = self.visit(l[0])
            p1 = ConvexPolygon(listap1)
            listap2 = self.visit(l[2])
            p2 = ConvexPolygon(listap2)
            return p2.union(p1)
        elif(l0 == '!'):
            i = 0
            lista = []
            while i < int(l[1].getText()):
                (x, y) = (uniform(0, 1), uniform(0, 1))
                if not (x, y) in lista:
                    lista.append((x, y))
                i += 1
            return lista

        return self.visitChildren(ctx)
