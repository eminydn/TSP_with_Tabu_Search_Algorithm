class TabuAlgorithm:
    def __init__(self):
        self.run = True
        self.cityNumber = int(input("Enter the number of cities: "))
        self.cityBegin = int(input("Choose the beginning city between 1 and {}: ".format(self.cityNumber)))
        self.d1 = []            #distances
        self.fWay = []          #first way randomly
        self.realWay = []       #
        self.tabuList = []

    def takeDistance1(self):
        i = self.cityNumber
        for a in range(0, i):
            d2 = []
            for b in range(i - 1 - a, i):
                d2.append(0)
            for c in range(a + 1, i):
                distances = int(input('Enter the distance between city {} and {}: '.format(a + 1, c + 1)))
                d2.append(distances)
            self.d1.append(d2)
        # print(self.d1)
        for a in range(0, i):
            for b in range(0, i):
                self.d1[b][a] = self.d1[a][b]
        # print(self.d1)
        return self.d1

    def takeDistance2(self):
        pass

    def takeDistance3(self):
        import numpy as np
        i = self.cityNumber
        a = int(i*(i-1)/2)
        rand_numbers = np.random.uniform(10, 40, size=a)
        rand_numbers = rand_numbers.round()
        d3 = []
        print(rand_numbers)
        for e in range(0,a):
            d3.append(int(rand_numbers[e]))
        print(d3)
        for a in range(0, i):
            d2 = []
            for b in range(i - 1 - a, i):
                d2.append(0)
            for c in range(a + 1, i):
                d2.append(d3[0])
                d3.pop(0)
            self.d1.append(d2)
            print(self.d1)
        print(self.d1)
        for a in range(0, i):
            for b in range(0, i):
                self.d1[b][a] = self.d1[a][b]
        print(self.d1)
        return self.d1

    def firstWay(self):
        import random
        i = self.cityNumber
        fWay1 = []
        fWay2 = []
        fCity = self.cityBegin
        for a in range(1, i + 1):
            fWay1.append(a)
        fWay2.append(fCity)
        fWay1.remove(fCity)
        print(fWay1, fWay2)
        while not fWay1 == []:
            r = random.randint(1, i)
            if r in fWay1:
                fWay2.append(r)
                fWay1.remove(r)
        fWay2.append(fCity)
        self.fWay = fWay2
        print(self.fWay)
        return self.fWay

    def calcDistance(self, a):      # a is the list which has the city way
        way = a
        print(way)
        i = len(way)
        print(i)
        dist = self.d1
        print(dist)
        totDis = 0
        for a in range(0, i - 1):
            x = way[a]
            y = way[a + 1]
            mDis = dist[x - 1][y - 1]
            totDis += mDis
        print(totDis)
        return totDis

    def searches(self):
        import random
        search = []
        i = self.cityNumber
        j = self.cityBegin
        b = 1
        while b < i:
            miniTryList = []
            trylist = []
            for a in range(1, i + 1):
                trylist.append(a)
            trylist.remove(j)
            c = 1
            while c < 3:
                r = random.randint(1, i)
                if r in trylist:
                    miniTryList.append(r)
                    trylist.remove(r)
                else:
                    while not r in trylist:
                        r = random.randint(1, i)
                    miniTryList.append(r)
                    trylist.remove(r)
                c = c + 1
            if miniTryList in search:
                b = b - 1
                search.remove(miniTryList)
                continue
            miniTryList.reverse()
            if miniTryList in search:
                b = b - 1
                search.remove(miniTryList)
                miniTryList.reverse()
                continue
            miniTryList.reverse()
            search.append(miniTryList)
            b = b + 1
        print(search)
        return search

    def tabu(self, a, b):
        self.tabuList.append(b)
        if len(self.tabuList)>a:
            self.tabuList.pop(0)
        return

    def change(self, list1, i):
        first = i[0]
        second = i[1]
        i1 = list1.index(first)
        i2 = list1.index(second)
        list1[i1], list1[i2] = list1[i2], list1[i1]
        return list1

    def changeOperator(self, list, search):
        k = []
        for a in range(0,len(search)):
            list2 = list.copy()
            changes = search[a]
            k.append(self.change(list2,changes))
        return print(k)

    def appIteration(self):
        self.changeOperator(self.firstWay(), self.searches())



        return

    def showMenu(self):
        print("""
        1)
        2)
        3)
        """)
        return

    def close(self):
        self.run = False
        return

    def choose(self):
        chs = int(input("Choose the number of operation you want to do: "))
        while chs < 1 or chs > 6:
            print("Wrong Number")
            chs = int(input("Choose the number of operation you want to do: "))
        return chs

    def runner(self):
        self.showMenu()
        choose = self.choose()
        if choose == 1:
            print("""
            1) If you want to input distances with hand:
            2) If you want to input distances from a text file:
            """)
            takeDisOp = int(input(" 1 or 2"))
            while takeDisOp < 1 or takeDisOp > 3:
                print("Wrong Number")
                takeDisOp = int(input("Choose the number of operation you want to do: "))
            if takeDisOp == 1:
                self.takeDistance1()
            elif takeDisOp == 2:
                self.takeDistance2()
            elif takeDisOp == 3:
                self.takeDistance3()
        elif choose == 2:
            self.close()
        elif choose == 3:
            self.firstWay()
        elif choose == 5:
            self.searches()
        elif choose == 6:
            self.appIteration()
        else:
            pass
        return


tabu = TabuAlgorithm()
while tabu.run == True:
    tabu.runner()
print("---Program Closed---")
