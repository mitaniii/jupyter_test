# import calc.fibo #import the fibo module
# calc.fibo.fib(1000)
# print(calc.fibo.fib2(1000))

# from calc.fibo import fib, fib2
# fib(1000)
# print(fib2(1000))

# import calc
# calc.fibo.fib(1000)
# print(calc.fibo.fib2(1000))
# print(calc.rand.get_random_number(1, 30))


#calcフォルダをまとめてパッケージ化してインポートしてみた
#__init__.pyが存在するフォルダがパッケージになる

# from calc import *   #__init__.pyにallの記述で*が使えるようになる
from calc import rand, fibo
print(rand.get_random_number(1, 30))
fibo.fib(1000)
print(fibo.fib2(1000))

from calc.op import sum #2つ下の階層の場合もその階層に__init__.pyを作る必要がある
print(sum.summary(1,2,3,4,5))