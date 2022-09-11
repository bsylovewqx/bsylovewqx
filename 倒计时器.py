import time
a = int(input('倒计时还是指定时间(0,1)'))
if a == 0:
    d = int(input('倒计时是分钟还是秒钟(0,1,2)'))
    s = int(input('倒计时:'))
    if d == 0:
        s *= 60
    if d == 2:
        s *= 60
        d = int(input('多少秒'))
        s += d

        print('时间到')
    if d == 1:
        pass
    while s>0:
            print(s)
            time.sleep(1)
            s -= 1

elif a == 1:
    pass

