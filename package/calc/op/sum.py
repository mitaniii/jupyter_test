def summary(*nums):
    return sum(nums)

if __name__ == '__main__':
    print(summary(1, 2, 3, 4, 5))
    print(summary(*[1, 2, 3, 4, 5]))
    print(summary(*range(1, 6))) #展開