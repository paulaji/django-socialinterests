from django.db import models
import random

# logic to create 5 digit ticket number
# Function to generate a random Ticket number with a minimum of 5 digits
def generate_ticket_number():
    return random.randint(10000, 99999)  # Adjust the range as needed

# Create your models here.
# New Lead model
class NewLead(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    ticketno = models.AutoField(primary_key=True, default=generate_ticket_number)

    # there is a special method in python (used below) in which the whole model or object can be represented as a string
    # in this case, it is defined such that it returns a string to represent the customer object we created
    # the string returned is name of the new lead
    def __str__(self):
        return(f"{self.name}")
    
# to register out New Lead model we just created in the admin panel, go add this in the admin.py file