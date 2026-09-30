import random
import string

from datetime import datetime


def generate_ticket_id():

    letters = random.choices(
        string.ascii_uppercase,
        k=3
    )

    number = random.randint(
        1000,
        9999
    )

    return (
        "".join(letters)
        + str(number)
    )


def create_ticket(
        customer_name,
        phone,
        movie,
        show_time,
        seats,
        payment_type):

    ticket_id = generate_ticket_id()

    now = datetime.now()

    ticket = {

        "ticket_id":
            ticket_id,

        "customer_name":
            customer_name,

        "phone":
            phone,

        "movie_name":
            movie[1],

        "language":
            movie[2],

        "duration":
            movie[3],

        "show_time":
            show_time,

        "seats":
            seats,

        "ticket_price":
            movie[4],

        "total":
            movie[4] * len(seats),

        "payment_type":
            payment_type,

        "booking_date":
            now.strftime(
                "%d-%m-%Y"
            ),

        "booking_time":
            now.strftime(
                "%I:%M %p"
            )
    }

    return ticket