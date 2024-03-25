class Playslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " has not paid yet"
        
ribs = Playslips("Ribesh", "no" , 3000)
roger = Playslips("Roger", "no", 1000)
print(ribs.status() ,"\n" , roger.status())

ribs.pay()

print("After payment \n")
print(ribs.status() ,"\n" , roger.status())


sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)



def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()


class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())