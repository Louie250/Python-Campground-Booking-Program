import os
from random import randrange
from datetime import date

pricePerNight = 7
date = date.today().strftime("%d/%m/%Y")

def addSale(date, name, nights, pricePerNight, saleValue):
    with open('Sales.txt', 'a') as salesF:
        salesF.write(str(date))
        salesF.write(" - ")
        salesF.write(str(name))
        salesF.write(" - ")
        salesF.write(str(nights))
        salesF.write(" - ")
        salesF.write(str(pricePerNight))
        salesF.write(" - ")
        salesF.write(str(saleValue))
        salesF.write("\n")

def addBooking(name, people, plot, nights):
    cost = nights * pricePerNight
    insertBooking = [name,people,"Plot "+ str(plot),nights, date, "£"+str(cost)]
    addSale(date, name, nights, pricePerNight, cost)
    with open('Bookings.txt', 'a') as bookings:
        bookings.write(str(insertBooking))
        bookings.write('\n')
    
    print("Details: ",insertBooking, "\n")

def remBooking(plot):
    with open("Bookings.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        if ("Plot "+ str(plot)) in new_f:
            if plot not in line:
                f.write(line)
        f.truncate()
        print("Successfully removed listing\n")

def checkPlot(plot):
    with open("Bookings.txt","r") as f:
        index = 0
        for line in f:
            index += 1
            if ("Plot "+ str(plot)) in line:
                print(line)
                return True
        if ("Plot "+ str(plot)) not in line:
            print("Error, there is no booking at plot " + str(plot) + "\n")
            return False

def choosePlot():
    plot = randrange(2)
    tries = 0
    if os.stat("Bookings.txt").st_size == 0:
            return plot
    with open("Bookings.txt","r") as f:
            index = 0
            for line in f:
                index += 1
                while ("Plot "+ str(plot)) in line:
                    tries += 1
                    if tries == 2:
                        print("Error, there are no more bookings")
                        tries = 0
                        plot = -1
                        return plot
                    else:
                        plot = randrange(2)
                    
            return plot
