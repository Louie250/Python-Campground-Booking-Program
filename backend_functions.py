import os
from random import choice as r_choice
from datetime import date

PRICE_PER_NIGHT = 7
NUMBER_OF_PLOTS = 50

def addSale(date_today, name, people, nights, saleValue):
    with open('Sales.txt', 'a') as salesF:
        salesF.write(f"{date_today} - {name} - {people} - {nights} - {PRICE_PER_NIGHT} - {saleValue}")

def addBooking(name, people, nights):
    plot = choosePlot()
    date_today = date.today().strftime("%d/%m/%Y")
    cost = nights * people * PRICE_PER_NIGHT
    insertBooking = f"['{name}', {people}, 'Plot {plot}', {nights}, '{date_today}', {cost}]\n"
    addSale(date_today, name, people, nights, cost)
    with open('Bookings.txt', 'a') as bookings:
        bookings.write(insertBooking)
    
    print("Details: ",insertBooking, "\n")

def remBooking(plot):
    with open("Bookings.txt") as f:
        lines = f.readlines()
    
    with open("Bookings.txt", 'w') as f:
        for line in lines:
            if f"Plot {plot}'" in line:
                print("Successfully removed listing\n")
            else:
                f.write(line)
        

def checkPlot(plot):
    with open("Bookings.txt") as f:
        # the ' is important because otherwise searching for "Plot 1" will return True if "Plot 10" is booked
        plot_is_booked = f"Plot {plot}'" in str([x for x in f.readlines()])
        if not plot_is_booked:
            print(f"Error, there is no booking at plot {plot}\n")
        return plot_is_booked
            

def choosePlot():
    try:
        with open("Bookings.txt") as f:
            bookings = [l.strip('\n') for l in f.readlines()]
    except FileNotFoundError:
        bookings = []

    if len(bookings) == NUMBER_OF_PLOTS:
        print("Error, there are no more bookings available.")
        return -1

    return r_choice([x for x in range(NUMBER_OF_PLOTS) if x not in bookings])
