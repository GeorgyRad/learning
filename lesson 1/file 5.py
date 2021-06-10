begin = int(input("Значение a = "))
off = int(input("Значение b ="))
day = 1
while begin < off:
    begin = begin * 1.1
    day += 1
print(day)