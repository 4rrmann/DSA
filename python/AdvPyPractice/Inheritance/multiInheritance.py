class Father():
    def skills(self):
        print("Gardening, Programming")

class Mother():
    def skills(self):
        print("Cooking, Art")

class Child(Father,Mother):
    def skills(self):
        print("Combo Skill Genes: \n")
        Father.skills(self)
        Mother.skills(self)
        print("Sports")


c = Child()
c.skills()