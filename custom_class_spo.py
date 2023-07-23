# -*- coding: utf-8 -*-            
# @Author : Zhihao Zhang
# @Time : 2023/7/23 13:30


class SPO:
    def __init__(self, s, p, o):
        self.s = s
        self.p = p
        self.o = o

    def __hash__(self):
        return hash((self.s, self.p, self.o))

    def __eq__(self, other):
        return self.s == other.s and \
               self.p == other.p and \
               self.o == other.o

    def __repr__(self):
        return f'SPO(S={self.s},P={self.p},O={self.o})'


a = SPO("a", "p", "c")
# b = SPO("a1", "p1", "c1")
#
# a1 = SPO("a", "p", "c")
# b1 = SPO("a2", "p2", "c2")
#
# print(a)
#
# print(list(set([a, b]) & set([a1, b1])))
