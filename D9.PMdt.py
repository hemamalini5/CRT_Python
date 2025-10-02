#Duck Typing
class Duck:
    def walk(self):
        print('thapak thapak thapak')
class Horse:
    def walk(self):
        print('tabdack tabdack tabdack')
def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)