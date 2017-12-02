# -*-coding:utf-8-*-

#print("start")
#print("+++++++++++++++++++++++")
"""
a = int(input("请输入你的年龄"))
if a>=19:
    print(a)
    print(a)
elif a<=12:
    print("ccc")
    print("ccc")
else:
    print("eee")
    print("eee")

while a<30:
    print(a)
    a = a+1
"""


# 打印直角三角形
"""
n = int(input("输入三角形的行数："))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1

"""


# 石头剪刀布游戏
"""
import random
a = random.randint(0,2)
print(a)
"""

"""
integer = int(input("请输入一个数字"))
print(str(integer))
"""


#字符串函数
"""
mystr = "abcdefABCDEF"
str = mystr[0]
print(str)
index = mystr.find("bc")
print(index)
print(mystr.capitalize())
"""



#去空（tab，制表，空格，换行等）去除
"""
test = 'abc \t bnv  \t abnv  ijgh a \t abr\t'
result = test.split()
result2 = "".join(result)
print(result2)
"""


#列表
"""
list = ['lao刘','123','laowang']
print(list[0])
list.append("centos")#---添加成员
print(list[3])
"""


#列表在表示相同数据时比较方便，但是当需要kv值类型时候，用字典比较方便
#<字典>
"""
#---格式：info = {key:value,key:value}
info = {"职务":"班长","addr":"山东","age":18}
print("%s-%s-%d"%(info["职务"],info["addr"],info["age"]))
"""
#===========================================================

#名片管理系统
"""
print("="*50)
print("名片管理系统")
print("="*50)
print("1.增加名片")
print("2.删除名片")
print("3.展示名片")
print("4.查询名片")
print("5.显示所有")
print("6.退出系统")
print("="*50)
list = []
while True:
    #获取用户输入的功能序号
    num = int(input("输入你想要的功能序号："))
    #添加功能
    if num == 1:
        person = {}
        position = input("输入职位：")
        person["posi"] = position
        address = input("输入地址：")
        person["addr"] = address
        age = input("输入年龄：")
        person["age"] = int(age)
        list.append(person)
    #删除功能
    elif num == 2:
        posi = input("请输入要删除的记录职位：")
        flag = True
        index = 0 #记录for循环到哪里了,用以删除列表中对应的字典
        for temp in list:

            if temp["posi"] == posi:
                del list[index]
                flag = False
            index += 1

        if flag:
            print("删除失败！")
    #展示功能,
    elif num == 3:
        pass
    elif num == 4:
        find_position = input("请输入要查询的职务：")
        flag = False
        for temp in list:
            if find_position == temp["posi"]:
                print("查到了！信息如下：")
                print("职务\t地址\t年龄\t")
                print("%s\t%s\t%d"%(temp["posi"],temp["addr"],temp["age"]))
                flag = True
                break
        if flag == False:
            print("对不起，查无此人！")

    elif num == 5:
        print("职位\t\t地址\t\t年龄\t\t")
        for temp in list:
            print("%s\t%s\t%d\t"%(temp["posi"],temp["addr"],temp["age"]))
    elif num == 6:
        break
    else:
        print("输入数字有错，请重新输入")


"""


#append()与extend的区别
"""
while True:
    list1 = ["aaa", "bbb", "ccc"]
    list2 = ["ddd", "eee", "fff"]
    print("append()与extend()的区别")
    print("list1为：", end="")
    print(list1)
    print("list2为：", end="")
    print(list2)

    choice = int(input("请选择用append(输入1)还是extend(输入2)"))
    if choice == 1:
        list1.append(list2)
        print(list1)
    elif choice == 2:
        list1.extend(list2)
        print(list1)
    else:
        print("输入有误")
        break
"""


#字典遍历方式之一
"""
infor = {"key1":"value1","key2":"value2","key3":"value3"}

#1.kyes()方法()
list = infor.keys() #返回的是一个列表,dict_keys(['key1', 'key2', 'key3'])---python3,['key1', 'key2', 'key3']--python2
print(infor.get("key1")) #value1
#遍历
for key in list:
    print(key)
#2.values()方法
list2 = infor.values() #dict_values(['value1', 'value2', 'value3'])--python3,['value1', 'value2', 'value3']--python2

#3.items()方法
items = infor.items() #元组,#dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])--python2
for item in items:
    print(item[0],end="#")
    print(item[1])
"""


#定义函数
"""
def function():
    pass
#调用函数
function()
"""

#全局变量
"""
a = 100
def test1():
    print(a)
def test2():
    print(a)

test1()
test2()
"""

#全局变量与局部变量的区别
"""
wendu = 0

def get_wendu():
    #wendu = 33 #此处只是定义了一个局部变量,注意，局部变量和全局变量不能同名
    global wendu #全局变量了
    wendu = 44 #这个是全局变量了

def print_wendu():
    print("现在的温度是：%s"%wendu)

get_wendu()
print_wendu()
"""

#查看帮助
"""help(print)"""

#添加函数文档
"""
def function():
    '''这是函数帮助文档，文档说明'''
help(function)
"""

#列表，字典当做全局变量（相当于java中的引用类型）
"""
list = [11,22,33]
dic = {"a":11,"bb":22,"cc":33}
def test():
    list.append(44)
    dic["dd"] = 44
test()
print(list)
print(dic)
"""

#元组赋值
"""
tuple = (12,13)
a,b = tuple
print(a)#12
print(b)#13
"""

#缺省参数
"""
def function(a, b=2,c=3):#b=2就是默认参数(放右边),当调用函数时不给b传参数时，则用b的默认参数
    print(a)
    print(b)
    print(c)

function(10)#这里将用到默认参数b=2
function(10,20)#这里b将用b=20这个参数

#help(print)
#又如help(print)的结果为：print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#则sep=' '等为默认参数
#当不实用默认参数的时候，可以指定参数给某个默认形参如下
function(10,c=20)#直接指定显参给谁，这里直接指定c=20
"""

#可变参数(元组形式,*args)
#单个元素的元组，一定要在该元素后面加上逗号“,”，如(3,)
"""
def function(a,b,*args):
    print(a)
    print(b)
    print(args)
function(1,2,3,4,5) #1 2 (3, 4, 5) *args是以元组形式存在
"""

#可变参数(字典形式,**kwargs)
#也就是当要用到key-value形式的时候就用**kwargs将多余的参数放在字典中
#当不需要key-value形式的可变参数时，用*args将多余的参数放在元组中
"""
def function(a,b,c=1,*args,**kwargs):
    print("a=%d"%a)
    print("b=%d"%b)
    print("c=%d"%c)
    print("args = ",end='')
    print(args)
    print("kwargs = ", end='')
    print(kwargs)

function(1,2,3,4,5,age= 18,name = "liuwei")  #---a=1 b=2 c=3 args = (4, 5)
                                            #---kwargs = {'age': 18, 'name': 'liuwei'}
"""

#元组&字典的拆包
"""
def function(a,b,c=1,*args,**kwargs):
    print("a=%d" % a)
    print("b=%d" % b)
    print("c=%d" % c)
    print("args = ", end='')
    print(args)
    print("kwargs = ", end='')
    print(kwargs)

A = (44,45,46)#元组
B = {"name":"liuwei","age":18}
function(1,2,3,A,B)
#输出
#a=1
#b=2
#c=3
#args = ((44, 45, 46), {'name': 'liuwei', 'age': 18})
#kwargs = {}
#拆包
function(1,2,3,*A,**B)  #意思就是将A拆包放在元组args中，将B拆包放在字典kwargs中
#a=1
#b=2
#c=3
#args = (44, 45, 46)
#kwargs = {'name': 'liuwei', 'age': 18}
"""

#引用
#python中所有的赋值都是引用类型
"""
a = 12
print(id(a))
b = a #引用，即b指向了a的那块内存
print(id(b))
def function(c):
    print(id(c))
    
    
function(a)
print(a)
print(b)
"""

#字典里面的key只能用不可变类型担当，如数字，元组，字符串。列表却不可以
"""
info = {"1":11,"2":12,"3":13}#合法的
info1 = {"a":12,"b":2,"c":3}#合法的
info2 = {"(1,2,3)":1,"(2,3,4)":2,"(3,4,5)":3}#合法的

info3 = {"[1,2,3]":1,"[2,3,4]":2,"[3,4,5]":3}#非法的，unhashable type “list”
print(info2["[1,2,3]"])#错误
"""



#匿名函数
"""
list = [1,3,6,2,7,23,45,23,75,43,13,67,43]
list.sort()#顺序排序
list.sort(reverse=True)#逆序排序
list.reverse()#反转
print(list)
"""

    #匿名函数
#匿名函数，即lambda，常规版本：
    #def fun(x,y)
        #return x*y
#lambda版本：
    #r = lambda x,y:x*y
    #格式：lambda 参数列表:return[表达式]变量
#匿名函数作为实参
"""
def test(a,b,func):
    result = func(a,b)
    return result

func_new = input("请输入一个匿名函数：")#注意，在python3里面，所有的输入均为字符串，所以要想达到python2的那种输入作为可执行语句，需要用eval()函数转化
func_new = eval(func_new)
num = test(11,22,func_new)
print(num)
"""

#python中的幂次方
"""
a = 4
print(a**3)
"""

#交换a，b的值
"""
a = 3
b = 4
a,b = b,a
print("a=%d,b=%d"%(a,b))
"""

#可变数据类型与不可变类型
"""
a = 100#不可变类型
b = [100]
def test(num):
    num += num #能修改可变类型的值，不可修改不可变类型值
    print(num)
test(a)
test(b)
print(a)#100
print(b)#[100, 100]
"""

#num+=num与num=num+num的区别
"""
a = 100#不可变类型
b = [100]
def test(num):
    num = num + num #这里num是局部变量，num+num是一个新的内存空间，因此num指向了另一块内存，由此可以看出num+=num并不等价于num=num+num
                    #在python中，a=a+b是先创建一个新的对象并让变量a引用这个对象，a+=b是让a所引用的对象的值变成a+b的值
    print(num)
test(a)
test(b)
print(a)#100
print(b)#[100]
"""

#文件操作
#文件写
"""
path = r"a.txt"
f = open(path,"a")
num = f.write("liuwei's file")
print(num)
"""

#文件读
"""
f = open("a.txt","r")
#string = f.read()#读取全部
string = f.read(1)#读一个字符
print(string)
"""

#文件复制
#文件的一般复制(小文件复制)
"""
old_file_name = input('输入想要复制的文件：')
old_file = open(old_file_name,"r")
#可以用rfind()从后往前找某个字符
new_file_name = old_file_name[0:old_file_name.find(".")]+"[复制]"+old_file_name[old_file_name.find("."):]
new_file = open(new_file_name,"w")
num = old_file.read()
#print(num)
new_file.write(num)
"""
#按行读取文件readline和readlines的区别
#一个返回的是单个字符串，一个是列表


#如何复制大文件,分步复制
"""
old_file_name = input('输入想要复制的文件：')
old_file = open(old_file_name,"rb")

new_file_name = old_file_name[0:old_file_name.rfind(".")]+"[复制]"+old_file_name[old_file_name.rfind("."):]
new_file = open(new_file_name,"wb")

string = old_file.read(1024*1024)
while len(string) != 0:
    new_file.write(string)
    string = old_file.read(1024*1024)#读取1024*1024字节，即1M
"""

#seek(offset[, whence]) 方法用于移动文件读取指针到指定位置,返回当前位置。tell()当前位置
#offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
#whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；# 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
"""
f = open("a.txt","rb")
index = f.seek(-2,2)
print(index)
"""

#文件，文件夹的常见操作
#os模块中的常见方法
import os
#os.rename("old_file_name","new_file_name")
#等等，见菜鸟教程
#name = os.getcwd()#显示当前的工作目录。
#print(name)

#面向对象
#----|
    #|--1.类的组成:类成员，方法，数据属性。
    #|--2.类的帮助信息可以通过ClassName.__doc__查看。
    #|--3.创建类的格式：#|class ClassName:
                      #|    '类的帮助信息'   #类文档字符串
                      #|    class_suite    #类体
#定义一个类，
"""
class Employee:
    '这是雇佣类'
    something = 10
    def test(self):
        print("This is a method")
    def eat(self):
        print("Eat something ,I'm a cat")
#创建实例，调用其中的方法
person = Employee()
person.eat()
"""

#self注意事项:第一个参数默认是self，代表实例自己，self只能代表实例，不能代表类。但是名字可以不是self，但是大家默认都这样写
"""
class Cat:
    '这是一个猫类'
    #属性
    name = '111'
    age = 0
    #方法
    def introduce(a):#a就是self
        print("%s"%(a.name))

tom = Cat()
tom.introduce()
"""

# __init__()方法,初始化方法，注意是两杠
"""
class Cat:
    '猫类'
    #属性，定义在这里的属性是该类所有类的共享属性，用"类名.属性名"调用，如：=
    count = 0 #所有实例共享的属性，用Cat.count调用
    #初始化对象,初始化函数
    def __init__(self,name,age):
        self.name = name #这里是实例属性，与java有区别
        self.age = age #这里是实例属性，与java有区别
"""

"""
1	__init__ ( self [,args...] )
        构造函数
        简单的调用方法: obj = className(args)
2	__del__( self )
        析构方法, 删除一个对象
        简单的调用方法 : del obj
3	__repr__( self )
        转化为供解释器读取的形式
        简单的调用方法 : repr(obj)
4	__str__( self )
        用于将值转化为适于人阅读的形式
        简单的调用方法 : str(obj)
5	__cmp__ ( self, x )
        对象比较
        简单的调用方法 : cmp(obj, x)
"""

#存放家具(将一个对象放在另一个对象属性里面)
"""
class Home:
    '这是房子类'
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area #房子剩余面积


    def __str__(self):
        return "房子的总面积是%d，剩余面积为%s，户型是%s，地址是%s"%(self.area,self.left_area,self.info,self.addr)
    def add_item(self,item):
        self.left_area -= item.get_area()

class Bed:
    '这是床类'
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
    def __str__(self):
        return "%s占用面积为%s"%(self.name,self.area)

    #返回床的面积
    def get_area(self):
        return self.area

    #返回床的名字
    def get_name(self):
        return self.name

fangzi = Home(168,"三室一厅","长沙岳麓区557号")
bed1 = Bed("ximengsi",10)
fangzi.add_item(bed1)
print(fangzi)
fangzi.add_item(Bed("sanrenchuang",15))#匿名对象
print(fangzi)
"""

#隐藏属性，属性直接被修改将存在风险
"""
class Dog:
    '狗类'
    pass
    def set_age(self,new_age):
        if new_age<=0:
            self.age = 0
        else:
            self.age = new_age

    def get_age(self):
        return self.age
dog = Dog()
#dog.name = "xiao白"  #----存在风险
#dog.age = 18   #----存在风险
"""

#私有方法：在方法名前加两杠"__"，并且用self.__method()的形式在共有方法中调用
"""
class Xiaofei:
    '消费类'
    def __consume(self):
        print("正在发送消费信息到银行......")
    def consume(self,money):
        if money>10000:
            print("金额过大，请重新输入")
        else:
            self.__consume() # 调用私有函数
"""

#继承
"""
class Animal:   #父类
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def sleep(self):
        print("睡")
    def run(self):
        print("跑")


class Dog(Animal):#Dog继承Animal类,在类的定义中添加括号加上父类即可
    def bark(self):
        print("吠")

class Cat(Animal):
    def dark(self):
        print("喵")

class Xiaotianquan(Dog):#孙子辈
    def fly(self):
        print("飞")
    #重写,如何调用父类的方法？
    def bark(self):
        print("哮")
        # 第一种调用被覆盖的父类的方法，格式：父类.被覆盖方法(self)
        #Dog.bark(self)
        # 第二种调用被覆盖的父类的方法，格式：super().被覆盖方法()
        super().bark()
dog = Dog()
dog.eat()

cat = Cat()
cat.eat()

x = Xiaotianquan()
x.eat()
x.bark()
"""

#删除对象，删除的是引用，而不是对象本身，除非是删除最后一个引用
#在真正删除调对象或者程序运行结束之后，每个被销毁的对象会自动调用__del__(self)方法
"""
import sys
class A:
    def __del__(self):
        print("对象被销毁了，这里是一系列动作")

a = A()
b = a

num = sys.getrefcount(a)
print(num)  #num = 3,即该对象有三个引用
del a
num2 = sys.getrefcount(b)
print(num2) #num2 = 2

del b #“对象被销毁了，这里是一系列动作”
"""

#私有的方法是不会被继承的，即__fangfa()类的方法是不会被继承的
#私有的方法只能被本类方法调用
#下面做个实验
"""
class Father:
    def __init__(self):
        print("父类初始化")
    def __test(self):
        print("父类私有方法")
    def test2(self):
        self.__test()
        print("父类普通方法")

class Son(Father):
    '这时候只能继承父类普通方法'
    def test3(self):
        #super().__test()#错误调用
        pass

s = Son()
s.test2() #父类初始化
         #父类私有方法
         #父类普通方法
#s.test3()#错误调用
"""

#类属性，实例属性
"""
class Tools(object):
    '工具类'
    #类属性
    num = 0

    def __init__(self,new_name,new_function):
        #实例属性
        self.name = new_name
        self.function = new_function
        Tools.num += 1

    def intruduce(self):
        print("我是%s类型的工具"%self.name)
t1 = Tools("起子","拧螺丝")
t2 = Tools("扳手","扳大螺丝")
t1.intruduce()
t2.intruduce()
print(Tools.num)

"""

#类方法，实例方法，静态方法
"""
class Tools(object):
    #类属性
    num = 0

    #实例方法，第一个参数是self
    def __init__(self,new_name,new_function):
        self.name = new_name
        self.function = new_function
        #Tools.num += 1
        #用类方法代替
        Tools.add_num()

    def intruduce(self):
        print("我是%s类型的工具" % self.name)
    #类方法
    @classmethod  #第一个参数是cls
    def add_num(cls):
        cls.num += 1

    # 静态方法，既不属于实例又不属于类，无参数，但又服务于该类,并且可以用类名或者类的实例对象调用
    @staticmethod
    def menu():
        print("=========")
        print("工具选择")
        print("1.起子")
        print("2.扳手")
        print("=========")

Tools.menu()
t1 = Tools("起子","拧螺丝")
t2 = Tools("扳手","扳大螺丝")
t1.menu()
t1.intruduce()
t2.intruduce()

print(Tools.num)
"""


#设计4s店类
"""
class CarStore(object):

    #过耦合，添加一款车就要修改代码
    '''
    def order(self,car_type):
        if car_type == "sangtana":
            return Sangtana()
        if car_type == "suotu":
            return Suotu()
    '''
    def order(self,car_type):
        return return_car_typy(car_type)
    #1.用函数解耦合
def return_car_typy(car_type):
    if car_type == "sangtana":
        return Sangtana(car_type)
    if car_type == "suotu":
        return Suotu(car_type)
class Car(object):
    def __init__(self,new_name):
        self.name = new_name
    def introduce(self):
        print("我是一辆%s的车"%self.name)
    def move(self):
        print("车子移动")
    def music(self):
        print("放音乐")
    def stop(self):
        print("车停")

class Sangtana(Car):
    #自动调用父类的init()
    '''def __init__(self,new_name):
        self.name = new_name'''
class Suotu(Car):
    #自动调用父类的init()
    '''def __init__(self,new_name):
        self.name = new_name'''

car_store = CarStore()
car = car_store.order("sangtana") #返回car类
car.introduce()
"""

#用类实现解耦(简单工厂类，即用该类生产类)
"""
class CarStore(object):

    #过耦合，添加一款车就要修改代码
    '''
    def order(self,car_type):
        if car_type == "sangtana":
            return Sangtana()
        if car_type == "suotu":
            return Suotu()
    '''
    def __init__(self):
        self.factory = Factory()
    def order(self,car_type):
        return self.factory.return_car_typy(car_type)
#2.用类实现解耦，工厂类
class Factory(object):
    def return_car_typy(self,car_type):
        if car_type == "sangtana":
            return Sangtana(car_type)
        if car_type == "suotu":
            return Suotu(car_type)
class Car(object):
    def __init__(self,new_name):
        self.name = new_name
    def introduce(self):
        print("我是一辆%s的车"%self.name)
    def move(self):
        print("车子移动")
    def music(self):
        print("放音乐")
    def stop(self):
        print("车停")

class Sangtana(Car):
    #自动调用父类的init()
    '''def __init__(self,new_name):
        self.name = new_name'''
class Suotu(Car):
    #自动调用父类的init()
    '''def __init__(self,new_name):
        self.name = new_name'''

car_store = CarStore()
car = car_store.order("suotu") #返回car类
car2 = car_store.order("sangtana")
car.introduce()
car2.introduce()
print(car) #<__main__.Suotu object at 0x01DF3950>
print(car2) #<__main__.Sangtana object at 0x01DF3970>
"""

