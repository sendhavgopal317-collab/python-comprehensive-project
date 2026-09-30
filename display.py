import time
import calendar

from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box


console = Console()


def welcome_screen():

    console.clear()

    console.print(
        Panel.fit(

            "[bold red]"
            "🎬 GOPAL MULTIPLEX 🎬"
            "[/bold red]\n\n"

            "[cyan]"
            "MOVIE TICKET BOOKING COUNTER"
            "[/cyan]\n\n"

            "[white]"
            "Welcome to Gopal Multiplex!"
            "[/white]",

            border_style="magenta"
        )
    )

    time.sleep(2)


def today_information():

    now = datetime.now()

    day = now.strftime(
        "%A"
    )

    date = now.strftime(
        "%d-%m-%Y"
    )

    month = calendar.month_name[
        now.month
    ]

    console.print(
        f"\n[cyan]Today:[/cyan] "
        f"{day}, {date}"
    )

    console.print(
        f"[cyan]Month:[/cyan] "
        f"{month}"
    )


def show_ticket(ticket):

    console.clear()

    table = Table(
        title="🎟 GOPAL MULTIPLEX TICKET",
        box=box.DOUBLE
    )

    table.add_column(
        "DETAIL"
    )

    table.add_column(
        "INFORMATION"
    )

    table.add_row(
        "Ticket ID",
        ticket["ticket_id"]
    )

    table.add_row(
        "Customer",
        ticket["customer_name"]
    )

    table.add_row(
        "Mobile",
        ticket["phone"]
    )

    table.add_row(
        "Movie",
        ticket["movie_name"]
    )

    table.add_row(
        "Language",
        ticket["language"]
    )

    table.add_row(
        "Duration",
        ticket["duration"]
    )

    table.add_row(
        "Show Time",
        ticket["show_time"]
    )

    table.add_row(
        "Seats",
        ", ".join(
            ticket["seats"]
        )
    )

    table.add_row(
        "Ticket Price",
        "₹" + str(
            ticket["ticket_price"]
        )
    )

    table.add_row(
        "Total Amount",
        "₹" + str(
            ticket["total"]
        )
    )

    table.add_row(
        "Payment",
        ticket["payment_type"]
    )

    table.add_row(
        "Booking Date",
        ticket["booking_date"]
    )

    table.add_row(
        "Booking Time",
        ticket["booking_time"]
    )

    console.print(table)

    console.print(
        Panel(

            "[bold green]"
            "✓ TICKET SUCCESSFULLY BOOKED!"
            "[/bold green]\n\n"

            "[white]"
            "Thank you for booking with "
            "Gopal Multiplex."
            "[/white]\n\n"

            "[yellow]"
            "Enjoy your movie! 🍿🎬"
            "[/yellow]",

            border_style="green"
        )
    )