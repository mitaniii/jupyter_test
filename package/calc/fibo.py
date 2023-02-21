#fibo.py Fibonacci numbers module
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


#直接呼び出した時に実行される
# (__name__はここでは__main__が入り、
# 違うファイルでこのファイルが実行されると、fiboが入る)
print(__name__) #確認用
if __name__ == "__main__":
    import sys
    #引数をとる書き方、もしなかったら1000を渡す
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    fib(num)
    print(fib2(num))