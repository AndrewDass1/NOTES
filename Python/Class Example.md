# Using Classes
```
# This script is just an example
class Rollthedice:

    def __init__(self, how_many_dice, number_of_face_dices, desired_number_to_land_on):
        self.how_many_dice = how_many_dice
        self.number_of_face_dices = number_of_face_dices 
        self.desired_number_to_land_on = desired_number_to_land_on


    def ask_for_amount_of_dice(self):
        return self.how_many_dice
        

    def highest_number_on_die(self):
        return self.number_of_face_dices

    def ask_what_number_to_land_on(self):    
        return self.desired_number_to_land_on
        probability = number_of_face_dices ** how_many_dice
        return probability



test_the_class1 = Rollthedice(2,1,4)
print(test_the_class1.how_many_dice)

# test the additional functions
test_the_class2 = Rollthedice(3,6,5)

print(test_the_class2.ask_for_amount_of_dice())
print(test_the_class2.highest_number_on_die())
print(test_the_class2.ask_what_number_to_land_on())

```
