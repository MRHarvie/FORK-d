import random
from dataclasses import dataclass
@dataclass #Creating RandomIntList class with list attribute
class RandomIntList(list):
    amount: int

    def __post_init__(self):
        self.generate_rand_int()

    def generate_rand_int(self): #Generate's random int between 1-100
        for i in range(self.amount):
            rand_int = random.randint(1,100)
            self.append(rand_int)

    def get_count(self): #Determines amount of variables
        return len(self)

    def get_total(self): #Determines sum of all variables
        return sum(self)

    def get_average(self): #Determines average of all variables
        return round(sum(self)/len(self),2) if len(self)>0 else 0

    def __str__(self): #Joins the variables as a string with ', ' seperating
        return ', ' .join(str(num) for num in self)

def main():
    print("Random Integer List")
    print()
    try:
        amount = int(input("How many integers should the list contain?:  ")) #Input to determines len of list/num of variables
        print()
        if amount <= 0: #Value Error if input not balid integer
            raise ValueError("Please enter a valid integer.")
        choice = 'y'
        while choice.lower() == 'y': #starting loop
            int_list = RandomIntList(amount)
            print("Random Integers")
            print("="*30)
            print("Integers:\t",int_list)
            print("Count:\t",int_list.get_count())
            print("Total:\t",int_list.get_total())
            print("Average:\t",int_list.get_average())
            print()
            choice = input("Continue (y/n)?:  ").lower()
            print()
    except ValueError:
        print(f"Please enter a valid integer. Error: {ValueError}")

    print("Bye!")

if __name__ == "__main__":
    main()