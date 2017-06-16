import pygame                   # 导入pygame库
from pygame.locals import *     # 导入一些常用的函数和常量
from sys import exit            # 向sys模块借一个exit函数用来退出程序

# 指定图像文件名称
background_image_filename = './pygame/source/sushiplate.jpg'
mouse_image_filename = './pygame/source/fugu.png'

pygame.init()       # 初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((640, 480), 0, 32) # 创建了一个窗口
pygame.display.set_caption("Hello, World!")         # 设置窗口标题

# 加载并转换图像
# convert函数是将图像数据都转化为Surface对象，每次加载完图像以后就应该做这件事件（事实上因为 它太常用了，如果你不写pygame也会帮你做）
# convert_alpha相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:          # 接收到退出事件后退出程序
            exit()


    x, y = pygame.mouse.get_pos()       # 获得鼠标位置

    x -= mouse_cursor.get_width() / 2   # 计算光标的左上角位置
    y -= mouse_cursor.get_height() / 2

    screen.blit(background, (0, 0))     # 将背景图画上去
    screen.blit(mouse_cursor, (x, y))   # 把光标画上去

    pygame.display.update()             # 刷新一下画面