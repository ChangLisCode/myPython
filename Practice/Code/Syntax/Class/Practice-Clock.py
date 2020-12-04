 """数字时钟"""


from time import sleep

class Clock(object):

    def __init__(self, hour=0, minute=0, second=0): # 传入初始化参数
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58) # 类的实例化，输入初始值
    while True:
        print(clock.show())   # 显示当前值，该值由show()的self参数，传入self._hour, self._minute, self._second。此self由run()定义
        sleep(1) # 交互显示为：间隔1s运行一次，表现为时钟计时效果
        clock.run() # 实例化后的clock，运行run(), 产生三个值，之后继续循环。


if __name__ == '__main__':    # 运行本程序
    main()
