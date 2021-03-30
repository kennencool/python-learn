# 父类
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()
print(summer.way_of_reproduction)
print('after move:', summer.move(5, 8))

# 子类
class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()
print(summer.have_feather)
print(summer.move(5, 8))

# self 的引用
class Human(object):
    laugh = 'hahaha'
    def show_laugh(self):
        print(self.laugh)
    def laugh_5th(self):
        for i in range(5):
            self.show_laugh();

lilei = Human()
lilei.laugh_5th()

# __init__ 的使用
class happyBird(Bird):
    def __init__(self, move_words):
        print('We are happy birds.', move_words)

summer = happyBird('wuhu!')