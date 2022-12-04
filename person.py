import random


class Person:
    def __init__(self,firstname,lastname,health,status):
        "Initialize attributes to be used in/available for all\
        class methods in this class, and for class objects created this class"


        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status


    def introduce(self):
        "All people introduce themselves"
        print("Hello my name is {} {}".format(self.firstname,self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy right today".format(self.firstname))
        elif emotion == 1:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >=76:
            print("{} is a little tired today".format(self.firstname))
        elif self.health == 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health <= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconcious.".format(self.firstname))

Abby = Person("Abby","Ruon", 95, status= True)
Sarah = Person("Sarah","Baraza",88,status=False)
Lee = Person("Lee","Williams", 72, status=True)

print("{} is my friend? {}".format(Abby.firstname, Abby.status))
print("{} is my friend? {}".format(Sarah.firstname,Sarah.status))

Abby.introduce()
Sarah.introduce()
Lee.introduce()

Abby.status_change()
Sarah.status_change()
Lee.status_change()

class Enemy(Person):
    def __init__(self,weapon,firstname,lastname,health,status):
        super().__init__(firstname,lastname,health,status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <=80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status == False

Hillary = Enemy('rock','Hillary','Edward',75,status=False)
Hillary.hurt(Abby)
Hillary.insult(Sarah)
Hillary.insult(Lee)
Hillary.steal(Sarah)

Hillary.introduce()