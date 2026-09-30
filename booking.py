from datetime import datetime


def customer_details():

    print(
        "\n========== CUSTOMER DETAILS =========="
    )

    while True:
        name = input(
            "Enter customer name: "
        ).strip()
        if name != "":
            break
        print(
            "Name cannot be empty."
        )
    while True:
        phone = input(
            "Enter mobile number: "
        )

        if phone.isdigit() and len(phone) == 10:
            break

        print(
            "Enter a valid 10 digit mobile number."
        )

    return name, phone


def show_times():

    print(
        "\n========== SHOW TIMES =========="
    )

    print("1. 10:00 AM")
    print("2. 01:30 PM")
    print("3. 04:30 PM")
    print("4. 07:30 PM")
    print("5. 10:30 PM")


def choose_show_time():

    show_times()

    times = {
        1: "10:00 AM",
        2: "01:30 PM",
        3: "04:30 PM",
        4: "07:30 PM",
        5: "10:30 PM"
    }

    while True:

        choice = input(
            "Select show time: "
        )

        if choice.isdigit():

            choice = int(choice)

            if choice in times:

                return times[choice]

        print(
            "Please select a valid show time."
        )


def show_seats():

    print(
        "\n========== AVAILABLE SEATS =========="
    )

    seats = []

    for row in ["A", "B", "C", "D", "E"]:

        row_seats = []

        for number in range(1, 11):

            seat = row + str(number)

            row_seats.append(seat)

        seats.append(row_seats)

    for row in seats:

        print(
            "  ".join(row)
        )

    return seats


def choose_seats():

    show_seats()

    while True:

        value = input(
            "\nEnter seats separated by comma "
            "(Example: A1,A2,A3): "
        )

        selected = (
            value
            .upper()
            .replace(" ", "")
            .split(",")
        )

        valid = True

        for seat in selected:

            if len(seat) < 2:

                valid = False
                break

            row = seat[0]
            number = seat[1:]

            if row not in [
                "A", "B", "C", "D", "E"
            ]:

                valid = False
                break

            if not number.isdigit():

                valid = False
                break

            number = int(number)

            if number < 1 or number > 10:

                valid = False
                break

        if valid and len(selected) > 0:

            return selected

        print(
            "Invalid seat selection."
        )


def booking_date():

    now = datetime.now()

    return now.strftime(
        "%d-%m-%Y"
    )