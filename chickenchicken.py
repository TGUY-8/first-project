#百钱买百鸡
#x+y+z=100
#5x+3y+z/3=100,求出所有可能的x,y,z组合
for x in range(100):
    y=25-x*(7/4)
    z=75+x*(3/4)
    if y%1==0 and z%1==0 and y>=0 and z>=0:
        print(f"There are {x} roosters, {y} hens, and {z} chicks")
#该题目数字范围较小，而python中for循环可以便捷地实现遍历枚举。但如果对x,y,z遍历，则数字将变为100的三次幂，代码效率低，则考虑将y,z用x表示（引入第四个变量也可）