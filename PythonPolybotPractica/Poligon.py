# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:05:43 2020

@author: raul
"""
import math

from PIL import Image, ImageDraw


class ConvexPolygon:

    color = (0, 0, 0)

    @staticmethod
    def getStats(l):

        minx, miny = l[0][0], l[0][1]
        minV = min(l[0][0], l[0][1])
        maxV = max(l[0][0], l[0][1])
        maxx, maxy = l[0][0], l[0][1]
        if(len(l) > 1):
            for i in range(1, len(l)):
                minT = min(l[i][0], l[i][1])
                maxT = max(l[i][0], l[i][1])
                if(minV > minT):
                    minV = minT
                if(maxV < maxT):
                    maxV = maxT
                if(minx > l[i][0]):
                    minx = l[i][0]
                if(miny > l[i][1]):
                    miny = l[i][1]
                if(maxx < l[i][0]):
                    maxx = l[i][0]
                if(maxy < l[i][1]):
                    maxy = l[i][1]
        return minx, maxx, miny, maxy

    @staticmethod
    def transformPointDecimalToInt(lP, minx, maxx, miny, maxy):

        varX = maxx - minx
        varY = maxy - miny
        lista = []
        if(len(lP) == 1):
            if(len(lP[0].listaP) == 1):
                lista.append([(200, 200)])
            elif(varX <= varY):
                var = (varY-varX)/2
                lista.append([(1+((p[0]-minx+var)*397/(abs(miny-maxy))), 398-((p[1]-miny)*397/abs(miny-maxy))) for p in lP[0].listaP])
            elif(varX > varY):
                var = (varX-varY)/2
                lista.append([(1+((p[0]-minx)*397/(abs(minx-maxx))), 398-((p[1]-miny+var)*397/abs(minx-maxx))) for p in lP[0].listaP])
        else:
            for i in lP:

                if(varX <= varY):
                    lista.append([(1+((p[0]-minx)*397/(abs(miny-maxy))), 398-((p[1]-miny)*397/abs(miny-maxy))) for p in i.listaP])
                else:
                    lista.append([(1+((p[0]-minx)*397/(abs(minx-maxx))), 398-((p[1]-miny)*397/abs(minx-maxx))) for p in i.listaP])
        return lista

    def creuat(self, o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def convexHull(self, l):
        l = sorted(set(l))
        if(len(l) > 1):
            lower = []
            for p in l:
                while len(lower) >= 2 and self.creuat(lower[-2], lower[-1], p) <= 0:
                    lower.pop()
                lower.append(p)
            print("lower")
            print(lower)
            upper = []
            for p in reversed(l):
                while len(upper) >= 2 and self.creuat(upper[-2], upper[-1], p) <= 0:
                    upper.pop()
                upper.append(p)
            print("upper")
            print(upper)
            return list(reversed(upper))[:-1] + list(reversed(lower))[:-1]
        else:
            return l

    def __init__(self, l=[(0, 0), (0, 1), (1, 1), (0.2, 0.8)]):
        self.listaP = self.convexHull(l)

    def vertices(self):
        print(len(self.listaP))
        return len(self.listaP)

    def centroid(self):
        x = 0
        y = 0
        n = len(self.listaP)
        for i in range(n):
            x += self.listaP[i][0]
            y += self.listaP[i][1]
        print(x/n, y/n)
        return(x/n, y/n)

    def isRegular(self):
        regular = True
        if(len(self.listaP) > 2):
            length = math.sqrt(pow((self.listaP[len(self.listaP)-1][0]-self.listaP[0][0]), 2)+(pow((self.listaP[len(self.listaP)-1][1]-self.listaP[0][1]), 2)))
            for i in range(len(self.listaP)-1):
                if(length != math.sqrt(pow((self.listaP[i][0]-self.listaP[i+1][0]), 2)+(pow((self.listaP[i][1]-self.listaP[i+1][1]), 2)))):
                    regular = False
                    break
        print(regular)
        return regular

    def isEqual(self, p):
        print(self.listaP == p.listaP)
        return self.listaP == p.listaP

    def area(self):
        n = len(self.listaP)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.listaP[i][0] * self.listaP[j][1]
            area -= self.listaP[j][0] * self.listaP[i][1]
        area = abs(area) / 2.0
        print(area)
        return area

    def setColor(self, tup):
        self.color = (tup[0]*255, tup[1]*255, tup[2]*255)

    def boundingBox(self):
        minx = self.listaP[0][0]
        miny = self.listaP[0][1]
        maxx = self.listaP[0][0]
        maxy = self.listaP[0][1]
        for i in range(1, len(self.listaP)):
            if(minx > self.listaP[i][0]):
                minx = self.listaP[i][0]
            elif(maxx < self.listaP[i][0]):
                maxx = self.listaP[i][0]
            if(miny > self.listaP[i][1]):
                miny = self.listaP[i][1]
            elif(maxy < self.listaP[i][1]):
                maxy = self.listaP[i][1]
        print(minx, " ", maxx, "\n", miny, " ", maxy)
        return self.convexHull([(minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)])

    def perimeter(self):
        suma = 0
        for i in range(len(self.listaP)-1):
            suma += math.sqrt(pow((self.listaP[i][0]-self.listaP[i+1][0]), 2)+(pow((self.listaP[i][1]-self.listaP[i+1][1]), 2)))
        suma += math.sqrt(pow((self.listaP[len(self.listaP)-1][0]-self.listaP[0][0]), 2)+(pow((self.listaP[len(self.listaP)-1][1]-self.listaP[0][1]), 2)))
        print(suma)
        return suma

    def pointInside(self, point):
        lold = self.listaP
        lnew = self.convexHull(self.listaP + [point])
        newP = [item for item in lnew if item not in lold]

    def polygonInside(self, poly):
        lold = self.listaP
        lnew = self.convexHull(self.listaP + poly.listaP)
        newP = [item for item in lnew if item not in lold]
        print(newP == [])
        return newP == []

    def det(self, a, b):
        return a[0] * b[1] - a[1] * b[0]

    def intersection(self, poly):
        if(self.isEqual(poly)):
            return self.listaP
        l = self.listaP + poly.listaP
        cHull = self.convexHull(l)
        linside = [item for item in l if item not in cHull]
        lintersect = []
        for i in range(len(self.listaP)):
            i2 = (i + 1) % len(self.listaP)
            for j in range(len(poly.listaP)):
                j2 = (j + 1) % len(poly.listaP)
                xdiff = (self.listaP[i][0] - self.listaP[i2][0], poly.listaP[j][0] - poly.listaP[j2][0])
                ydiff = (self.listaP[i][1] - self.listaP[i2][1], poly.listaP[j][1] - poly.listaP[j2][1])
                div = self.det(xdiff, ydiff)
                if div != 0:
                    d = (self.det(self.listaP[i], self.listaP[i2]), self.det(poly.listaP[j], poly.listaP[j2]))
                    x = self.det(d, xdiff) / div
                    y = self.det(d, ydiff) / div
                    xminp1 = min(self.listaP[i][0], self.listaP[i2][0])
                    xmaxp1 = max(self.listaP[i][0], self.listaP[i2][0])
                    xminp2 = min(poly.listaP[j][0], poly.listaP[j2][0])
                    xmaxp2 = max(poly.listaP[j][0], poly.listaP[j2][0])
                    yminp1 = min(self.listaP[i][1], self.listaP[i2][1])
                    ymaxp1 = max(self.listaP[i][1], self.listaP[i2][1])
                    yminp2 = min(poly.listaP[j][1], poly.listaP[j2][1])
                    ymaxp2 = max(poly.listaP[j][1], poly.listaP[j2][1])

                    if ((x) >= (xminp1) and (x) <= (xmaxp1) and (y) >= (yminp1) and (y) <= (ymaxp1) and (x) >= (xminp2) and (x) <= (xmaxp2) and (y) >= (yminp2) and (y) <= (ymaxp2)):
                        xf = 0
                        yf = 0
                        if(x == -0):
                            print("I entered")
                            print(x)
                            xf = 0
                            print(x)
                        elif(y == -0):
                            yf = 0
                        else:
                            xf = x
                            yf = y
                        print (xf, yf)
                        lintersect.append((xf, yf))
        print("Hola")
        print(self.convexHull(linside + lintersect))
        return self.convexHull(linside + lintersect)

    def union(self, poly):
        union = self.convexHull(self.listaP + poly.listaP)
        print(union)
        return union

    @staticmethod
    def draw(lop, name):

        listOfPoints = [item for sublist in lop for item in sublist.listaP]
        polys = [[]]
        if(len(listOfPoints) > 0):
            minx, maxx, miny, maxy = ConvexPolygon.getStats(listOfPoints)
            print(minx, maxx, miny, maxy)
            print(lop)
            polys = ConvexPolygon.transformPointDecimalToInt(lop, minx, maxx, miny, maxy)
            print(polys)
        with Image.new('RGB', (400, 400), (255, 255, 255)) as im:
            draw = ImageDraw.Draw(im)
            for i in range(len(polys)):
                print(polys[i])
                if(len(polys[i]) == 1):
                    draw.point(polys[i], fill=lop[i].color)
                elif(len(polys[i]) > 1):
                    draw.polygon(polys[i], outline=lop[i].color)
            im.save(name)
