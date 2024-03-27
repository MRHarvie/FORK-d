from dataclasses import dataclass
@dataclass
class Person:
    first_name: str
    last_name: str
    email: str

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
@dataclass
class Customer(Person):
    number: str
@dataclass
class Employee(Person):
    ssn: str

def display_person_info(person):
    if isinstance(person, Customer):
        print("CUSTOMER")
        print(f"Name: \t\t{person.get_full_name()}")
        print(f"Email: \t\t{person.email}")
        print(f"Number: \t{person.number}")
        print()
    elif isinstance(person, Employee):
        print("EMPLOYEE")
        print(f"Name: \t\t{person.get_full_name()}")
        print(f"Email: \t\t{person.email}")
        print(f"SSN: \t{person.ssn}")
        print()


def main():
    print("Customer/Employee Data Entry\n")
    run = 'y'
    while run.lower() == 'y':
        choice = input("Customer or employee? (c/e):  ")
        print()
        print("DATA ENTRY")
        if choice.lower() == "c":
            customer_data = {
                "first_name": input("First Name: "),
                "last_name": input("Last Name: "),
                "email": input("Email: "),
                "number": input("Number: ")}
            print()
            customer = Customer(**customer_data)
            display_person_info(customer)
        elif choice.lower() == "e":
            employee_data = {
                "first_name": input("First Name: "),
                "last_name": input("Last Name: "),
                "email": input("Email: "),
                "ssn": input("SSN: ")}
            print()
            employee = Employee(**employee_data)
            display_person_info(employee)
        else:
            print("Invalid Choice. Please enter y or n.")
        run = input("Continue? (y/n): ").lower()
        print()
    print("Bye!")

if __name__ == "__main__":
    main()

