# 1 九九乘法表

for i in range(9):        # 从0循环到8
  i += 1                  # 等价于 i = i+1
  for j in range(i):      # 从0循环到i
  j += 1
  print(j,'*',i,'=',i*j,end = ' ',sep='')
                          # end默认在结尾输出换行，将它改成空格 sep 默认 j,'*',i,'=',i*j 各元素输出中间会有空格
  print()                 # 这里作用是输出换行符

# 2nd method
i = 1
while i <= 9:
  j = 1
  while j <= i:
  print("%d*%d=%d" % (j,i,i*j),end=' ') # 格式化输出
  j += 1
  i += 1
  print()    

# 3 rd method
for i in range(1, 72):
  n = i // 9 + 2
  m = i % 9 + 1
  print('%d x %d = %d' % (n, m, n * m))    
    
    
    
# 2 登录程序
'''
复制代码
登录程序，有三次输入账号、密码的机会，错误三次账号锁定
'''

user = 'hello world'
paswd = 123456
username = input("请输入用户名：")
password = input("请输入密码:")
for i in range(3):
    if username == user and int(password) == paswd: #判断用户名和密码是否都匹配
        print("欢迎您的到来")
        break
    elif i < 2:
        username = input("请输入用户名：")
        password = input("请输入密码")
    elif i == 2:
        print("账户已锁定")
        break



# 3，购物车程序
'''
复制代码
功能：
1，输入余额
2，显示商品列表
3，输入要购买的东西
4，判断是否有能力购买
5，是否继续
6，输出已购买的商品和余额
'''

shop_car = []#用来存放购买的商品
goods = {
    1:['手机',2500],
    2:['电脑',3500],
    3:['自行车',4500],
    4:['宝马',20000]
}#商品列表
while True:
    salary = input("你有多少钱：") # 输入有多少钱
    if salary.isdigit(): # 判断是否为整数
        salary = int(salary) # 将字符串转化为整数
        print("是否要买东西：")
        flag1 = input("Y      N:")
        if flag1.upper() == 'N': # 将字符串大写
            exit("欢迎下次光临") # 退出程序并输出“欢迎下次光临”
        elif flag1.upper() == 'Y':
            break                # 终止循环
        elif flag1.upper() == 'Q':
            exit("欢迎下次光临")
    elif salary.upper() == 'Q':
        exit("欢迎下次光临")
while True:
        print("淘宝".center(30,'-')) # 输出以-----淘宝------
        for i in goods: # 循环输出
            print(i,goods[i])
        print("淘宝".center(30, '-'))
        choice_good = input("请输入商品编码：")#接受一个字符串
        if choice_good.isdigit() :
            choice_good = int(choice_good)
            if choice_good >= 1 and choice_good <= 4:
                if salary >= goods[choice_good][1]:
                    shop_car.append(goods[choice_good][0]) # 给字典中添加元素
                    salary = salary - goods[choice_good][1]
                    print("您购买的商品为：", goods[choice_good][0])
                    print("余额为：", salary)
                    print("是否继续：")
                    contin = input("Y    N")
                    if contin.upper() == 'N':
                        break
                    elif contin.upper() == 'Q':
                        break
                else:
                    print('余额不足')
                    print("是否继续：")
                    contin = input("Y    N")
                    if contin.upper() == 'N':
                        break
                    elif contin.upper() == 'Q':
                        break
            else :
                print("没有这个编号")
                continue # 暂停本次循环
        elif choice_good.upper() == "Q" :
            break
        else:
            print("我看不懂。。。")
print("你买了：",end =' ')
for i in shop_car:
    print(i,end=' ')
print()
print("余额为：",salary)
print("欢迎下次光临")   
