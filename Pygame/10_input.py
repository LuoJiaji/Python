from math import *
import pygame
from pygame.locals import *
from sys import exit

class Vector2(tuple):
    def __new__(typ, x=0.0, y=0.0):
        n = tuple.__new__(typ,(int(x),int(y)))
        n.x = x
        n.y = y
        return n

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    @classmethod
    def from_points(cls, P1, P2):
        return cls( P2[0] - P1[0], P2[1] - P1[1] )

    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )

    def normalize(self):
        magnitude = self.get_magnitude()
        if magnitude != 0:
            self.x /= magnitude
            self.y /= magnitude


background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(*(200.0, 150.0))
speed = 100.0
rotation = 0.0        # 出事角度
rotation_speed = 360. # 每秒转动的角度数（转速）

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    rotation_direction = 0.0
    movement_direction = 0.0

    # 更改角度
    if pressed_keys[K_LEFT]:
        rotation_direction = +1.0
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.0
    # 前进、后退
    if pressed_keys[K_UP]:
        movement_direction = +1.0
    if pressed_keys[K_DOWN]:
        movement_direction = -1.0

    # 获得一条转向后的鱼
    rotated_sprite = pygame.transform.rotate(sprite, rotation)
    # 转向后，图片的长宽会变化，因为图片永远是矩形，为了放得下一个转向后的矩形，外接的矩形势必会比较大
    w, h = rotated_sprite.get_size()
    # 获得绘制图片的左上角（感谢pltc325网友的指正）
    sprite_draw_pos = Vector2(position.x - w / 2, position.y - h / 2)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 图片的转向速度也需要和行进速度一样，通过时间来控制
    rotation += rotation_direction * rotation_speed * time_passed_seconds

    # 获得前进（x方向和y方向），这两个需要一点点三角的知识
    heading_x = sin(rotation * pi / 180.)
    heading_y = cos(rotation * pi / 180.)
    # 转换为单位速度向量
    heading = Vector2(heading_x, heading_y)
    # 转换为速度
    heading *= movement_direction

    position += heading * speed * time_passed_seconds

    screen.blit(background, (0, 0))
    screen.blit(rotated_sprite, sprite_draw_pos)

    pygame.display.update()