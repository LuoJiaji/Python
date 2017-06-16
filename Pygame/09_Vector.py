import math
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

position = Vector2(*(100.0, 100.0))
heading = Vector2()
print(Vector2(1,2)-Vector2(3,4)*(1/2))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))
    screen.blit(sprite, tuple(position))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 参数前面加*意味着把列表或元组展开
    destination = Vector2( *position ) + Vector2( *sprite.get_size() )*0.5    # 获取物体中心点的绝对向量
    # 计算鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = Vector2.from_points(destination, pygame.mouse.get_pos()) # 计算物体中心点到鼠标之间的向量
    # 向量规格化
    vector_to_mouse.normalize()

    # 这个heading可以看做是鱼的速度，但是由于这样的运算，鱼的速度就不断改变了
    # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动。

    heading = heading + (vector_to_mouse * 0.5 ) # 让物体做加速运动
    # heading = vector_to_mouse*100   # 让物体做匀速运动
    # print(heading)
    position += heading * time_passed_seconds
    print(position)
    pygame.display.update()