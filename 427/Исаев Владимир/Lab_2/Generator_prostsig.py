from Nasl_gen import Garmonic
class Treug(Garmonic):
    def foo(self):
        print('bye')
        return
class Pil(Garmonic): pass
class Shim(Garmonic):pass
t=Treug(1,2,3,4)
t.foo()
y=Pil(1,2,3,4)
mygenerator = y.createGenerator() # создаём генератор
print(mygenerator) # mygenerator является объектом!

for i in mygenerator:
         
         print(i)