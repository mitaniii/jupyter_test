import sys
print(sys.argv)
sum = 0
for arg in sys.argv[1:]:
    if arg.isdigit(): #数字の時だけ
        sum += int(arg)

print(sum)

sys.stderr.write("erroe")
sys.exit(1)