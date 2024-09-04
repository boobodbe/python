"""2024.07.01 21：10
坦克大战游戏的需求
1.坦克中有哪些类
2.每个类中有哪些方法

1.坦克类（我方坦克、敌方坦克）
	射击
	移动类
	显示坦克的方法
2.子弹类
	移动
	显示子弹的方法
3.墙壁类
	属性：是否可以通过
4.爆炸效果类
	展示爆炸效果
5.音效类
	播放音乐
6.主类
	开始游戏
	结束游戏
"""
# 导入pygame模块
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(100,30,30)

class MainGame():
    window = None
    def __init__(self):
        pass
    # 开始游戏
    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 设置窗口的标题
        pygame.display.set_caption("坦克大战001")
        while True:
            # 给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            # 获取事件
            self.getEvent()
            pygame.display.update()
    # 结束游戏
    def endGame(self):
        print("谢谢使用，欢迎再次使用。")
        exit()

    # 获取事件
    def getEvent(self):
        # 获取所有事件
        eventlist = pygame.event.get()
        # 遍历事件
        for event in eventlist:
            # 判断按下的键是关闭还是键盘按下
            # 如果按的是退出，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()
            # 如果是键盘按下
            if event.type == pygame.KEYDOWN:
                # 判断按下的是上、下、左、右
                if event.key == pygame.K_LEFT:
                    print("按下左键，坦克想左移动。")
                elif event.key == pygame.K_RIGHT:
                    print("按下右键，坦克向右移动。")
                elif event.key == pygame.K_UP:
                    print("按下上键，坦克向上移动。")
                elif event.key == pygame.K_DOWN:
                    print("按下下键，坦克向下移动。")
class Tank():
    def __init__(self):
        pass
    # 移动
    def move(self):
        pass
    # 射击
    def shot(self):
        pass
    # 展示坦克的方法
    def displayTank(self):
        pass

# 我方坦克
def MyTank(Tank):
    def __init__(self):
        pass

# 敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass

# 子弹类
class Bullet():
    def __init__(self):
        pass
    # 移动
    def move(self):
        pass
    # 展示子弹的方法
    def displayBullet(self):
        pass

class Wall():
    def __init__(self):
        pass
    # 展示墙壁的方法
    def displayWall(self):
        pass

class Explode():
    def __init__(self):
        pass
    # 展示爆炸效果的方法
    def displayExplode(self):
        pass

class Music():
    def __init__(self):
        pass
    # 播放音乐的方法
    def playMusic(self):
        pass

if __name__ == "__main__":
    MainGame().startGame()

# 看完70节视频，2024.07.01 21：46，明天继续
# 看完71节视频，2024.07.02 07：29 