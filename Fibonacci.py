#计算斐波那契数列的第n项
#f(x)=f(x-1)+f(x-2)
#1,1,(1+1),(1+2)
def add_(n):
    if n==1 or n==2:
        return 1
    elif n%1==0 and n>2:
        return add_(n-1)+add_(n-2)
    else:
        print("POSITIVE INTEGER ONLY!")
        return False
def main():
    try:
        x=int(input("Calculate the n-th value of the Fibonacci sequence,n="))
        k=add_(x)
        print("The value is",k)
    except ValueError:
        print("Error")
if __name__=='__main__':
    main()
