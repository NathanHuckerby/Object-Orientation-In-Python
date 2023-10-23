#. Create two new vehicles called car1 and car2. 
#Set car1 to be a red convertible worth $60,000.00 with a name of Fer, 
#and car2 to be a blue van named Jump worth $10,000.00.

class vehicles:
    name = " "
    colour = " "
    kind = " "
    value = " "

    def description(self):
        desc = "%s is a %s %s worth $%s" % (self.name, self.colour, self.kind, self.value)
        return desc

Car1 = vehicles()
Car2 = vehicles()

Car1.name = "Fer"
Car1.colour = "red"
Car1.kind = "convertable"
Car1.value = 60000

Car2.name = "Jump"
Car2.colour = "blue"
Car2.kind = "van"
Car2.value = 10000

print(Car1.description())
print(Car2.description())


    