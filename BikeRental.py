
"""Bike Rental project which involves...Renting a bike on hourly,daily,and weekly basis.In this I'm going
to keep trak of stock and issue bill when the customer return the bike"""
"""To keep track of time we need DateTime Module"""

import datetime

"""Main class BikeRental"""

class Bikerental:
    """constructor for the bike rental which involves maintaing the stock"""
    def __init__(self,stock =0):
        self.stock = stock

    """Displaying the bike stock to the customer"""
    def display_stock(self):
        print("we are current having {} bikes available".format(self.stock))
        return self.stock

    """Rent on Hourly basis
        n is the number of bikes requested by the customer"""
    def rent_On_Hourly_Basis(self,n):
        """Invalid Request"""
        if n<=0:
            print("Please Enter the right number")
            return None
        elif n>self.stock:
            print("Sorry we have current {} availale bikes only".format(self.stock))
            return None
        else:
            """now is for recording the time when the bike is rented"""
            now = datetime.datetime.now()
            """now.hour gives the time in hour when the bike is rented"""
            print("You have rented {} bikes on hourly basis today at hour {}".format(n,now.hour))
            print("You will be charged 300 rupees per hour ")
            print("Have a good ride")

            self.stock-=n
            return now

    """Rent on dailybasis and the cost is 1400 per day"""
    def rent_on_daily_basis(self,n):
        """Invalid Request"""
        if n < =0:
            print("Please Enter the right number")
            return None
        elif n > self.stock:
            print("Sorry we have current {} availale bikes only".format(self.stock))
            return None
        else:
            """now is for recording the time when the bike is rented"""
            now = datetime.datetime.now()
            """now.hour gives the time in hour when the bike is rented"""
            print("You have rented {} bikes on daily basis today at hour {}".format(n, now.hour))
            print("You will be charged 1400 rupees per day ")
            print("Have a good ride")

            self.stock -= n
            return now

    """Rent on weeklybasis and the cost is 4200 per week"""
    def rent_on_weely_basis(self,n):
        """Invalid Request"""
        if n <=0:
            print("Please Enter the right number")
            return None
        elif n > self.stock:
            print("Sorry we have current {} availale bikes only".format(self.stock))
            return None
        else:
            """now is for recording the time when the bike is rented"""
            now = datetime.datetime.now()
            """now.hour gives the time in hour when the bike is rented"""
            print("You have rented {} bikes on hourly basis today at hour {}".format(n, now.hour))
            print("You will be charged 4200 rupees per hour ")
            print("Have a good ride")

            self.stock -= n
            return now

    """Returning the bike and issuing the bill"""
    def returnBike(self,request):
        """This involves adding back the bike to inventory
            Issuing the bill and applying discount based on the bikes rented"""
        rental_basis,rental_time,no_of_bikes = request
        bill =0

        if rental_basis and rental_time and no_of_bikes:
            #adding the bike to stock
            self.stock += no_of_bikes
            now = datetime.datetime.now()
            rental_period = now - rental_time

            #Hourly basis
            if rental_basis==1:
                bill = round(rental_period.seconds/3600)*5*no_of_bikes

            #Daily basis
            if rental_basis == 2:
                bill = round(rental_period.days)*20*no_of_bikes

            #weekly basis
            if rental_basis ==3:
                bill = round(rental_period.days//7)*60*no_of_bikes

            #applying discount for more than 3 bikes and less than 5 bikes
            if (3<=no_of_bikes<=5):
                print("Your aligible for the discount of 30% on your bill")
                bill = bill*0.7
            print("THanks for returning the bike...Hope you had a good ride")
            print("Your bill is {}".format(bill))
            return bill
        else:
            print("You haven't rented a bike")
            return  None

"""Creating the Customer class for making the request abd return ing the bike"""

class Customer:
    """Class constructor for no_of_bikes,rental_basis,rental_time and bill"""

    def __init__(self):
        self.no_of_bikes = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    """Making a request for renting a bike"""
    def requestbike(self):
        #Input no_of_bike
        bikes = input("How many bikes do you want? ")

        try:
            bikes = int(bikes)
        except ValueError:
            print("Please enter a positive value")
            return -1

        if bikes<1:
            print("The number should be greater than zero ")
            return -1
        else:
            self.no_of_bikes = bikes
            return self.no_of_bikes

    def return_bike(self):
        if self.rental_time and self.rental_basis and self.no_of_bikes:
            return self.rental_time,self.rental_basis,self.no_of_bikes
        else:
            return 0,0,0

