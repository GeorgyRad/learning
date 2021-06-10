sec = int(input("Введите время в секундах: \n"))
hour = 00;
if sec > 60:
    min = sec//60
    sec = sec - 60*min
elif sec < 60:
    min = 00;
if min > 60:
        hour = min//60
        min = min - 60*hour
elif min < 60:
        hour = 00
if hour < 10:
    hour = "0" + str(hour)
else:
    hour = str(hour)
if min < 10:
    min = "0"+ str(min)
else:
    min = str(min)
if sec < 10:
    sec = "0"+str(sec)
else:
    sec = str(sec)
print(hour,":", min,":", sec, sep="")