import string
from stack import Stack
import numpy as np
import re
import random
#epsilon=="ε"
#当输入字符串长度大于7时，调整{:10s}{:20s}
#去除直接左递归
class LL1(object):
    def __init__(self,gram):
        self.gram=gram;
        self.origin=list(self.gram.keys())[0]#文法开始符号
        a = self.gram.keys()
        self.table=None
        self.first = self.gram.fromkeys(a, "")
        self.follow = self.gram.fromkeys(a, "")
        self.follow_belong=self.gram.fromkeys(a, "")
        self.col = self.tablecol()
        self.row=self.gram.keys()
        self.flag = False#处理"T": "FS", "S": "ε" 中follow T包含follow F
        self.init_Table()
        self.input_str_stack=Stack()
        self.analyze_stack=Stack()
        self.input_str=""
    #获得表的列self.col
    def tablecol(self):
        char=[]
        for i in self.gram:
            j = self.gram.get(i)
            char += re.findall(r'[a-z+*()]', j)
        char.append("#")
        char=list(set(char))#去除重复
        return char
    #寻找first,follow
    def init_First_Follow(self):
        self.init_First()
        self.init_Follow()
        for i in self.follow_belong:
            j=self.follow_belong.get(i)
            for k in j:
                self.follow[i]+=self.follow[k]
        self.DeleteRepeat()
    def init_First(self):
        for i in self.gram:
            uu=""
            u=self.find_first(i,uu)
            self.first.update({i: u})
    def find_first(self,i,u):
        j = self.gram.get(i).split("|")
        for k in j:
            if k[0]==i:
                continue
            if k[0].isupper():
                u=self.find_first(k[0],u)
                for m in u:
                    if m!='ε':
                        t = self.find_col_and_row(m, i)
                        ss = i + "::=" + k
                        self.table[t[0]][t[1]] = ss
            else:
                if k[0]!='ε':
                    t=self.find_col_and_row(k[0],i)
                    ss=i + "::=" + k
                    self.table[t[0]][t[1]]=ss
                u+=self.first.get(i)+k[0]
        return u;
    def init_Follow(self):
        for i in self.gram:
            if i==self.origin:
                self.follow.update({i: "#"})#源E添加#
            self.find_follow(i)
        for i in self.follow_belong:
            if self.follow_belong.get(i) != "":  # E->T follow_belong:{T:E}即T包含E
                for j in self.follow_belong.get(i):
                    u=self.follow.get(i)+self.follow.get(j)
                    self.follow.update({i:u})
    def find_follow(self,i):
        j = self.gram.get(i).split("|")
        for k in j:
            flag = False
            data = ""
            for m in k:
                if flag:
                    flag=False
                    if m.isupper():
                        uu=self.find_follow2(m)
                        u = self.follow.get(data) + uu
                        if self.flag:
                            ss = self.follow_belong.get(data) + i
                            self.follow_belong.update({data: ss})
                            self.flag=False

                    else:
                        u=self.follow.get(data)+m
                    self.follow.update({data: u})
                if m.isupper():
                    flag=True;
                    data=m
            if flag:
                #u=self.follow.get(k[-1])+self.follow.get(i)#E->T follow_belong:{T:E}即T包含E
                #self.follow.update({k[-1]:u })
                u=self.follow_belong.get(k[-1])+i
                self.follow_belong.update({k[-1]:u})
    def find_follow2(self,i):
        u=""
        j = self.gram.get(i).split("|")
        for k in j:
            if k[0]==i:
                continue
            if k[0].isupper():
                u+=self.find_follow2(k[0])
            else:
                if k[0]!="ε":
                    u+=k[0]
                else:
                    self.flag=True
        return u
    #消除 self.follow 和self.follow_belong 的重复的
    def DeleteRepeat(self):
        for i in self.follow:
            a=self.follow.get(i)
            b=""
            for j in a:
                if j not in b:
                    b+=j
            self.follow.update({i:b})
        for i in self.follow_belong:
            a=self.follow_belong.get(i)
            b=""
            for j in a:
                if j not in b:
                    b+=j
            self.follow_belong.update({i:b})
    def init_Table(self):
        self.table = [[" " * 20] * (len(self.col) + 1)] * (len(self.row) + 1)
        self.table = np.array(self.table)
        for i in range((len(self.row) + 1)):
            for j in range((len(self.col) + 1)):
                self.table[i][j]=" "
        count = 0
        for i in self.row:
            count += 1
            self.table[count][0] = i
        count = 0
        for i in self.col:
            count += 1
            self.table[0][count] = i
     # 对应[A,a]寻找Table行列坐标k是a，i是A :[A,a]
    def find_col_and_row(self,k,i):
        count = 0
        for j in self.table[0,]:
            if j == k:
                break
            count += 1
        c=count
        count = 0
        for j in self.table[:,0]:
            if j == i:
                break
            count += 1
        r=count
        t=[r,c]
        return t
    def buildLL1Table(self):
        for i in self.first:
            if "ε" in self.first.get(i):
                for j in self.follow.get(i):
                    t = self.find_col_and_row(j, i)
                    ss = i + "::=" + "ε"
                    self.table[t[0]][t[1]] =ss
    def print_Table(self):
        for i in self.gram:
            print("{:10s}{:10s}".format(i, self.gram.get(i)))
        print("____________________________\nfirst集:")
        for i in self.first:
            print("{:10s}{:10s}".format(i,self.first.get(i)))
        print("____________________________\nfollow集:")
        for i in self.follow:
            print("{:10s}{:10s}".format(i, self.follow.get(i)))
        ll1.buildLL1Table()
        print("____________________________\ntable分析表:")
        for i in ll1.table:
            for j in i:
                print("{:10s}".format(j),end='')
            print()

    def init_Stack(self):
        s=list(self.input_str+'#')
        s.reverse()
        for i in s:
            self.input_str_stack.push(i)
        self.analyze_stack.push('#')
        self.analyze_stack.push(self.origin)
    def analyze_LL1(self):
        k=1
        while True:
            A=self.analyze_stack.stack[self.analyze_stack.top]
            a=self.input_str_stack.stack[self.input_str_stack.top]
            t=self.find_col_and_row(a,A)
            #if k==4:
                #print() #调试时用
            if A!=a and A=="#":
                print('{:10s}{:10s}{:10s}{:10s}'.format(str(k), self.analyze_stack.showStack_as_str(),self.input_str_stack.showStack_as_str(), "匹配失败"))
                print(self.input_str + "不是文法所定义的句子。")
                # 失败
                break
            if A==a and A=="#":
                print('{:10s}{:10s}{:10s}{:10s}'.format(str(k),self.analyze_stack.showStack_as_str(),self.input_str_stack.showStack_as_str(),"匹配成功"))
                print(self.input_str+"是文法所定义的句子。")
                #匹配成功
                break
            elif A==a and A!="#":
                print('{:10s}{:10s}{:10s}{:10s}'.format(str(k),self.analyze_stack.showStack_as_str(), self.input_str_stack.showStack_as_str(),""))
                k+=1
                self.analyze_stack.pop()
                self.input_str_stack.pop()

            else:
                ss = str(self.table[t[0]][t[1]])
                if ss!=" ":
                    print( '{:10s}{:10s}{:10s}{:10s}'.format(str(k),self.analyze_stack.showStack_as_str(), self.input_str_stack.showStack_as_str(),ss))
                    k += 1
                    self.analyze_stack.pop()
                    p=list(ss.split("::=")[1])
                    p.reverse()
                    p=''.join(p)
                    if p!="ε":
                        for i in p:
                            self.analyze_stack.push(i)
                else:
                    print('{:10s}{:10s}{:10s}{:10s}'.format(str(k),self.analyze_stack.showStack_as_str(), self.input_str_stack.showStack_as_str(),"匹配失败"))
                    print(self.input_str+"不是文法所定义的句子。")
                    #失败
                    break
def eliminate_left_recursion(G):
    for i in list(G.keys()):
        flag = 0
        j = G.get(i).split("|")
        for m in j:
            if m[0] == i:
                flag += 1
        if flag == 0:
            break
        while True:
            q = string.ascii_uppercase
            newVn = random.choice(q)
            if newVn not in G:
                break
        s = ''  # 原Vn
        ss = ''  # 新Vn
        for m in j:
            if m[0] != i:
                if m == 'ε':
                    s += newVn + '|'
                else:
                    s += m + newVn + '|'
            else:
                ss += m[1:] + newVn + '|'
        s = s[:-1]
        ss += 'ε'
        G[i] = s
        G.update({newVn: ss})
if __name__=='__main__':
    G = {"E": "E+T|ε|T", "T": "T*F|F", "F": "(E)|i"}
    #G={"E": "TR", "R": "+TR|ε", "T": "FS", "S": "*FS|ε", "F": "(E)|i"}
    #G={"S":"iCtSB|a","B":"eS|ε","C":"b"}#二义
    eliminate_left_recursion(G)
    ll1=LL1(G)
    ll1.init_First_Follow()
    ll1.print_Table()
    s=input("____________________________\n请输入句子：")
    ll1.input_str=s
    ll1.init_Stack()
    ll1.analyze_LL1()