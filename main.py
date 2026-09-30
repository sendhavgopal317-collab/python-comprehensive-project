from database import create_tables
from database import add_movies
from database import save_booking

from language import choose_language
from movies import choose_movie

from booking import customer_details
from booking import choose_show_time
from booking import choose_seats

from payment import payment
from ticket import create_ticket

from display import welcome_screen
from display import today_information
from display import show_ticket

from gui_ticket import show_ticket_window

import admin


def main():

    # Create database tables first
    create_tables()

    # Add default movies
    add_movies()

    # Admin
    admin.admin_login()
    admin.add_movie_window()
    admin.delete_movie_window()

    # Welcome screen
    welcome_screen()

    # Today's information
    today_information()

    # Customer details
    customer_name, phone = customer_details()

    # Language
    language = choose_language()

    # Movie
    movie = choose_movie(language)

    # Show time
    show_time = choose_show_time()

    # Seats
    seats = choose_seats()

    # Total amount
    total_amount = movie[4] * len(seats)

    # Payment
    payment_type = payment(total_amount)

    # Create ticket
    ticket = create_ticket(
        customer_name,
        phone,
        movie,
        show_time,
        seats,
        payment_type
    )

    # Save booking
    save_booking(
        ticket["ticket_id"],
        ticket["customer_name"],
        ticket["phone"],
        ticket["movie_name"],
        ticket["language"],
        ticket["show_time"],
        ", ".join(ticket["seats"]),
        ticket["total"],
        ticket["payment_type"],
        ticket["booking_date"]
    )

    # Show ticket in terminal
    show_ticket(ticket)

    # Show ticket in GUI
    show_ticket_window(ticket)


main()