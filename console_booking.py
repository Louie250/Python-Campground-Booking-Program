import backend_functions

while True:
    choice = input("Do you want to add or remove a booking (add/rem/exit): ")
    if choice == "add":
        name = input("\nEnter the customer's name: ")
        numberOfPeople = int(input("Enter number of people staying: "))
        nightsStaying = int(input("Enter number of nights staying: "))
        backend_functions.addBooking(name, numberOfPeople, nightsStaying)

    elif choice == "rem":
        customerPlot = int(input("\nAsk customer for plot number that they stayed at: "))
        if backend_functions.checkPlot(customerPlot):
            backend_functions.remBooking(customerPlot)
    
    elif choice == "exit":
        break
