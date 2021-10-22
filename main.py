
class Product(object):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            cur, self.num = self.n, self.num + 1
            return cur
        else:
            raise StopIteration()

    def __getitem__(self):
        return self.price

    def __setitem__(self, price):
        self.price = price

    def __str__(self):
        return str(self.name) + ', ' + str(self.price) + ', ' + str(self.quantity)

##################################################
def makeDiscount(name, price):  # through iterator
    i = 0
    for j in list(name):
        if j in list('Kosher Passover'):
            i += 1
        if i == 2:
            p = price * 95 / 100
            return p
    return price
#################################################
def makeDiscount2(lst): # through generator
    for j in range(len(lst)):
        i = 0
        for c in list(lst[j].name):
            if c in list('Kosher Passover'):
                i += 1
            if i == 2:
                price = lst[j].price * 95 / 100
                yield price
        if i < 2:
            yield lst[j].price
###################################################

P = Product('Milk', 5.5, 32)
P2 = Product('Khhosher', 100, 45)
P3 = Product('Pssa vvcjh', 200, 29)
# print(P)
# print(P2)
# print(P3)
lst = [P, P2, P3]  # make a list of products

print("Iterator type type:")
itList = iter(lst)
it1 = next(itList)
it2 = next(itList)
it3 = next(itList)
print(makeDiscount(it1.name, it1.price))
print(makeDiscount(it2.name, it2.price))
print(makeDiscount(it3.name, it3.price))

print("Generator type:")
for price in makeDiscount2(lst):
    print(price)