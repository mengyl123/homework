from turtle import *
from datetime import *
import time


def SetupClock(radius):
    # 建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius - 20)
            Skip(radius + 20)
            if i == 0:
                write(int(12), align="center", font=("Courier", 14, "bold"))
            elif i == 30:
                Skip(25)
                write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-25)
            elif (i == 25 or i == 35):
                Skip(20)
                write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-20)
            else:
                write(int(i / 5), align="center", font=("Courier", 14, "bold"))
            Skip(-radius - 20)
        else:
            dot(5)
            Skip(-radius)
        right(6)


def Skip(step):
    penup()
    forward(step)
    pendown()


# 定义表针函数mkHand()
def mkHand(name, length):
    # 注册Turtle形状，建立表针Turtle
    reset()
    Skip(-length * 0.1)
    begin_poly()
    forward(length * 1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm)


def Init():
    global secHand, minHand, hurHand, printer
    mode("logo")  # 重置Turtle指向北
    # 建立三个表针Turtle并初始化
    mkHand("secHand", 130)
    mkHand("minHand", 110)
    mkHand("hurHand", 90)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 建立输出文字Turtle
    printer = Turtle()

    printer.hideturtle()
    printer.penup()


def get_week_day():
    week_day_dict = {
        0: '星期天',
        1: '星期一',
        2: '星期二',
        3: '星期三',
        4: '星期四',
        5: '星期五',
        6: '星期六',
    }
    today = int(time.strftime("%w"))
    return week_day_dict[today]
def get_exact_hour():
    return time.strftime("%H")
def get_exact_minute():
    return time.strftime("%M")
def get_exact_second():
    return time.strftime("%S")

# 更新时钟函数Tick()
def Tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0

    tracer(False)
    printer.forward(65)

    # print(get_week_day())
    printer.write(get_week_day(), align="center", font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write((str(t.year) + "-" + str(t.month) + "-" + str(t.day)), align="center", font=("Courier", 14, "bold"))
    printer.back(60)
    printer.write(get_exact_hour(), align="center", font=("Courier", 14, "bold"))
    printer.left(90)
    printer.back(30)
    printer.write(':', align="center", font=("Courier", 14, "bold"))
    printer.back(30)
    printer.write(get_exact_minute(), align="center", font=("Courier", 14, "bold"))
    printer.back(30)
    printer.write(':', align="center", font=("Courier", 14, "bold"))
    printer.back(30)
    printer.write(get_exact_second(), align="center", font=("Courier", 14, "bold"))
    printer.home()
    tracer(True)
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)
    ontimer(Tick, 100)  # 100ms后继续调用tick
    

def main():
    tracer(False)
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()


if __name__ == '__main__':
    main()
