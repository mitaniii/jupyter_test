# デシジョンテーブルの問題

from datetime import datetime, time

def get_first_drink_price(dt, coupon=False):
    if coupon:
        return 100
    else:
        t = dt.time()
        if t >= time(16, 0,) and t < time(18, 00):
            return 290
    return 490

happy_hour = datetime(2023, 2, 15, 17, 59, 30)
nomal_hour = datetime(2023, 2, 15, 19, 0, 0)

print(get_first_drink_price(happy_hour, coupon=True) == 100)
print(get_first_drink_price(happy_hour) == 290)
print(get_first_drink_price(nomal_hour) == 490)
print(get_first_drink_price(datetime.now()) == 100)