#Look up linear probing collision handling for reference
class HashMap():
    def __init__(self):
        self.max = 10
        self.hashArray = [[] for x in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
            return hash % self.max

    def __getitem__(self, key):
        hval = self.get_hash(key)
        for subArray in self.hashArray[hval]:
            if subArray[0] == key:
                return subArray[1]
            else:
                print("No such value exists!")

    def __setitem__(self, key, value):
        hval = self.get_hash(key)
        found = False
        for index, element in enumerate(self.hashArray[hval]):
            if element[0] == key:
                self.hashArray[hval][index] = (key,value)
                found = True
                break
        if not found:
            self.hashArray[hval].append((key,value))

    def __delitem__(self, key):
        hval = self.get_hash(key)
        for index, element in enumerate(self.hashArray[hval]):
            if element[0] == key:
                del self.hashArray[hval][index]
                break


newHM = HashMap()
print(newHM.hashArray)
#print(newHM.get_hash("March"))
#print(newHM.get_hash("May"))
newHM["March"] = 121
newHM["May"] = 323
print(newHM.hashArray)
del newHM["March"]
print(newHM.hashArray)