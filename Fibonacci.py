#计算斐波那契数列的第n项
#f(x)=f(x-1)+f(x-2)
#1,1,(1+1),(1+2)
def Fibonacci_(n):
    if n==1 or n==2:
        return 1
    elif n>2:
        return Fibonacci_(n-1)+Fibonacci_(n-2)
    else:
        return False
def main():
    try:
        x=int(input("Calculate the n-th value of the Fibonacci sequence,n="))
        k=Fibonacci_(x)
        if k>0:
            print("The value is",k)
        else:
            print("POSITIVE INTEGER ONLY!")
    except ValueError:
        print("Please enter a number!")
if __name__=='__main__':
    main()#确保被其他模块导入时main()不会被直接执行
