import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:

    event = pygame.event.wait()         # 等待时间发生
    event_text.append(str(event))       # 获得时间的名称

    event_text = event_text[int(-SCREEN_SIZE[1]/font_height):]      # 这个切片操作保证了event_text里面只保留一个屏幕的文字

    if event.type == QUIT:
        exit()

    screen.fill((0, 0, 255))

    y = SCREEN_SIZE[1]-font_height      # 找一个合适的起笔位置，最下面开始但是要留一行的空
    for text in reversed(event_text):
        screen.blit( font.render(text, True, (255, 255, 0)), (0, y))
        y -= font_height      # 把笔提一行

    pygame.display.update()


# Pygame可以自己产生事件并获取该事件
# CATONKEYBOARD = USEREVENT + 1
# my_event = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
# pygame.event.post(my_event)

# # 然后获得它
# for event in pygame.event.get():
#     if event.type == CATONKEYBOARD:
#         print(event.message)

# 事件过滤
# pygame.event.set_blocked(事件名)