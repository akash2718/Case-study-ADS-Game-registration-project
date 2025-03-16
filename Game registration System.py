class Student:

    def __init__(self, id, name, age, college):
        self.id = id
        self.name = name
        self.age = age
        self.college = college

    def display(self):

        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, College: {self.college}")


reservations = []


def add_reservation(id, name, age, college):

    if search_reservation(id):
        print("Error: Student ID already exists!")
        return
    student = Student(id, name, age, college)
    reservations.append(student)
    print("Reservation added successfully!")

def search_reservation(id):

    for student in reservations:
        if student.id == id:
            return student
    return None


def update_reservation(id, name=None, age=None, college=None):

    student = search_reservation(id)
    if student:
        if name: student.name = name
        if age: student.age = age
        if college: student.college = college
        print("Reservation updated successfully!")
    else:
        print("Error: Reservation not found!")

def delete_reservation(id):

    global reservations
    if search_reservation(id):
        reservations = [s for s in reservations if s.id != id]
        print("Reservation deleted successfully!")
    else:
        print("Error: Reservation not found!")


def display_reservations():

    if not reservations:
        print("No reservations available.")
        return
    print("\nAll Reservations:")
    for student in reservations:
        student.display()
    print()

# Menu-driven program
def main():
    while True:
        print("\nGame Reservation System")
        print("1. Add Reservation")
        print("2. Search Reservation")
        print("3. Update Reservation")
        print("4. Delete Reservation")
        print("5. Display All Reservations")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            college = input("Enter College Name: ")
            add_reservation(id, name, age, college)

        elif choice == "2":
            id = int(input("Enter Student ID to search: "))
            student = search_reservation(id)
            if student:
                print("\nReservation Found:")
                student.display()
            else:
                print("Reservation not found!")

        elif choice == "3":
            id = int(input("Enter Student ID to update: "))
            name = input("Enter new Name (leave blank to keep unchanged): ") or None
            age = input("Enter new Age (leave blank to keep unchanged): ")
            college = input("Enter new College Name (leave blank to keep unchanged): ") or None
            update_reservation(id, name, int(age) if age else None, college)

        elif choice == "4":
            id = int(input("Enter Student ID to delete: "))
            delete_reservation(id)

        elif choice == "5":
            display_reservations()

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
