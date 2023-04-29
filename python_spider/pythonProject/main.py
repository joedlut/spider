import sys
import os

if __name__ == '__main__':
    #for i in sys.argv:
    #    print(i)
    print(sys.path)
    dict = {}
    dict['one'] = "1 - 菜鸟教程"
    dict[2] = "2 - 菜鸟工具"

    tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

    print(dict['one'])  # 输出键为 'one' 的值
    print(dict[2])  # 输出键为 2 的值
    print(tinydict)  # 输出完整的字典
    print(tinydict.keys())  # 输出所有键
    print(tinydict.values())  # 输出所有值
    for i in tinydict.keys():
        print(i)
    tup1 = (50,)
    print(len(tup1))
    age = int(input("请输入你家狗狗的年龄: "))
    print("")
    if age <= 0:
        print("你是在逗我吧!")
    elif age == 1:
        print("相当于 14 岁的人。")
    elif age == 2:
        print("相当于 22 岁的人。")
    elif age > 2:
        human = 22 + (age - 2) * 5
        print("对应人类年龄: ", human)


    def hello():
        print("Hello World!")


    hello()


    def max(a, b):
        if a > b:
            return a
        else:
            return b


    a = 4
    b = 5
    print(max(a, b))
    # python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

    def changeme(mylist):
        "修改传入的列表"
        mylist.append(90)
        print("函数内取值: ", mylist)
        return


    # 调用changeme函数
    mylist = [10, 20, 30]
    changeme(mylist)
    print("函数外取值: ", mylist)


    # 可写函数说明
    def printme(str):
        "打印任何传入的字符串"
        print(str)
        return


    # 调用printme函数
    printme(str="guodonghan")


    def printinfo(name, age):
        "打印任何传入的字符串"
        print("名字: ", name)
        print("年龄: ", age)
        return


    # 调用printinfo函数
    printinfo(age=50, name="runoob")

    # Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。

    #在字典中遍历时，关键字和对应的值可以使用
    #items()
    #方法同时解读出来：
    # 类定义
    class people:
        # 定义基本属性
        name = ''
        age = 0
        # 定义私有属性,私有属性在类外部无法直接进行访问
        __weight = 0

        # 定义构造方法
        def __init__(self, n, a, w):
            self.name = n
            self.age = a
            self.__weight = w

        def speak(self):
            print("%s 说: 我 %d 岁。" % (self.name, self.age))


    # 实例化类
    p = people('runoob', 10, 30)
    p.speak()
    print(os.getcwd())