class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True


    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self,value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def __repr__(self):
        values = list(self.dictionary.keys())
        return f"MySet({values})"
    
my_set = MySet([1,2,3])

print(my_set.has(2))

my_set.add(4)
my_set.add(5)
my_set.delete(5)
print(my_set.size())

print(my_set)








