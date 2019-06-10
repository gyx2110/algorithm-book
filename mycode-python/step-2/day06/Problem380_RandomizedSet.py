# class RandomizedSet(object):

#     def __init__(self):
#         self.element = set()
#         self.map = {}
#         self.size = 0

#     def insert(self, val):
#         if val in self.map:
#             return False
#         self.map[val] = self.size
#         self.element.add(val)

#         self.size+=1
#         return True

#     def remove(self, val):
#         if val not in self.map or size==0:
#             return False
#         self.map.pop(val)
#         self.element.remove(val)
#         self.size-=1
#         return True

#     def getRandom(self):
#         import random
#         return sele.map.keys()[random.randint(0,self.size-1)]


class RandomizedSet(object):

    def __init__(self):
        self.element = []
        self.map = {}
        self.size = 0
    def insert(self, val):
        if self.map.has_key(val):
            return False
        
        self.element.append(val)

        self.map[val] = self.size
        
        self.size+=1
        return True

    def remove(self, val):
        if not self.map.has_key(val) or self.size==0:
            return False
        #将最后一个元素交换到val所在的位置
        tail = self.element[self.size-1]
        self.element[self.map.get(val)] = tail
        self.map[tail] = self.map.get(val)
        #删除最后一个元素
        self.element.pop()
        self.map.pop(val)

        self.size -=1
        return True

    def getRandom(self):
        import random
        return self.element[random.randint(0,self.size-1)]
if __name__ == "__main__":
    s = RandomizedSet()
    print s.insert(1)
    print s.getRandom()