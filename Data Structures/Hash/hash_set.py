# Give me an example implemenation of basic hash set


class HashSet:
    def __init__(self, size=100):
        self.size = size
        self.data = [[] for _ in range(size)]

    def _hash(self, key):
        '''
        This function will return the hash of the key
        '''
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        return hash

    def add(self, key):
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = []
        if key not in self.data[hash]:
            self.data[hash].append(key)
        return self.data

    def remove(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i] == key:
                    self.data[hash].pop(i)
                    return
        return False

    def contains(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i] == key:
                    return True
        return False

    def keys(self):
        keys = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    keys.append(self.data[i][j])
        return keys

    def __repr__(self):
        return str(self.data)


if __name__ == '__main__':
    hs = HashSet()
    hs.add('apple')
    hs.add('banana')
    hs.add('cherry')
    hs.add('durian')
    hs.add('eggplant')
    hs.add('fig')
    hs.add('grape')
    hs.add('honeydew')
    hs.add('ice cream')
    hs.add('jackfruit')
    hs.add('kiwi')
    hs.add('lemon')
    hs.add('mango')
    hs.add('nectarine')
    hs.add('orange')
    hs.add('pineapple')
    hs.add('quince')
    hs.add('raspberry')
    hs.add('strawberry')
    hs.add('tomato')
    hs.add('ugli')
    hs.add('vanilla')
    hs.add('watermelon')
    hs.add('xylophone')
    hs.add('yam')
    hs.add('zucchini')
    print(hs)
    print(hs.contains('apple'))
    print(hs.contains('banana'))
    print(hs.contains('cherry'))
    print(hs.contains('durian'))
    print(hs.contains('eggplant'))
    print(hs.contains('fig'))
    print(hs.contains('grape'))
    print(hs.contains('honeydew'))
    print(hs.contains('ice cream'))
    print(hs.contains('jackfruit'))
    print(hs.contains('kiwi'))
    print(hs.contains('lemon'))
    print(hs.contains('mango'))
    print(hs.contains('nectarine'))
    print(hs.contains('orange'))
    print(hs.contains('pineapple'))
    print(hs.contains('quince'))
    print(hs.contains('raspberry'))
    print(hs.contains('strawberry'))
    print(hs.contains('tomato'))
    print(hs.contains('ugli'))
    print(hs.contains('vanilla'))
    print(hs.contains('watermelon'))
    print(hs.contains('xylophone'))
    print(hs.contains('yam'))
    print(hs.contains('zucchini'))
    print(hs.contains('apple'))
    print(hs.contains('banana'))
    print(hs.contains('cherry'))
    print(hs.contains('durian'))
    print(hs.contains('eggplant'))
    print(hs.contains('fig'))
    print(hs.contains('grape'))
