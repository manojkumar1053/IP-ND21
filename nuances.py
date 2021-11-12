class Dog:
    #tricks = set()
    def __init__(self, name):
        self.name = name
        self.tricks = set()
    def teach(self, trick):
        self.tricks.add(trick)

#Change the broken code above so that the following lines work:

buddy = Dog('Buddy')
pascal = Dog('Pascal')
buddy.teach('sit')
pascal.teach('fetch')
buddy.teach('roll over')
print(buddy.tricks)  # {'sit', 'roll over'}
print(pascal.tricks)  # {'fetch'}


class Dog:
    def __init__(self, name,tricks=None):
        self.name = name
        if tricks:
            self.tricks = tricks
        else:
            self.tricks = set()
    def teach(self, trick):
        self.tricks.add(trick)

# Change the broken code above so that the following lines work:
#
# buddy = Dog('Buddy')
# pascal = Dog('Pascal')
# kimber = Dog('Kimber', tricks={'lie down', 'shake'})
# buddy.teach('sit')
# pascal.teach('fetch')
# buddy.teach('roll over')
# kimber.teach('fetch')
# print(buddy.tricks)  # {'sit', 'roll over'}
# print(pascal.tricks)  # {'fetch'}
# print(kimber.tricks)  # {'lie down', 'shake', 'fetch'}

# This one's a bit different, representing an unusual (and honestly,
# not recommended) strategy for tracking users that sign up for a service.

class User:
    # An (intentionally shared) collection storing users who sign up for some hypothetical service.
    # There's only one set of members, so it lives at the class level!
    members = set()
    def __init__(self, name):
        self.name = name
        #self.members = set()  # Not signed up to begin with.
    def sign_up(self):
        self.members.add(self.name)

# Change the code above so that the following lines work:
#
# sarah = User('sarah')
# heather = User('heather')
# cristina = User('cristina')
# print(User.members)  # {}
# heather.sign_up()
# cristina.sign_up()
# print(User.members)  # {'heather', 'cristina'}
