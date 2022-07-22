import numpy

PI = 3.14159

def check_hit(*balls):
    # 不适用于推广成cube的情况，如果不规则应该检查是否有重叠的x,y坐标
    for a in balls:
        for b in balls:
            if not a == b:
                distance = (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)
                if distance <= (a.r + b.r) * (a.r + b.r):  # 碰撞
                    tan_angle = (a.y - b.y) / (a.x - b.x)
                    angle = numpy.arctan(tan_angle)
                    if a.y > b.y and a.x>b.x :
                        a.giveForce(angle,force=)   # TODO 根据speed等计算force
                        b.giveForce(angle+PI,force=)



class Ball(object):
    def __init__(self, r, m, x, y):
        self.__radius = r
        self.__m = m
        self.__x = x
        self.__y = y
        self.__speed = [None, 0]
        self.__force = []  # [(),(),(),...,()]

    def __getattr__(self, item):
        if item == 'r':
            return self.__radius
        elif item == 'm':
            return self.__m
        elif item == 'x':
            return self.__x
        elif item == 'y':
            return self.__y
        else:
            return None

    def giveForce(self, angle, force):
        f = [angle, force]
        self.__force.append(f)






# class PhysicsSystem(object):
#     def __init__(self):
#         self.__ball_list = []
#
#     def addBall(self,id,r,x,y,speed,force):
#         pass
#
