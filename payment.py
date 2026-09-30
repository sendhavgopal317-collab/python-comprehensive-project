import time

from rich.console import Console


console = Console()


def payment(total_amount):

    print(
        "\n========== PAYMENT =========="
    )

    print(
        "Total Amount: ₹",
        total_amount
    )

    print("\n1. UPI")
    print("2. Card")

    while True:

        choice = input(
            "Select payment method: "
        )

        if choice == "1":

            while True:

                upi_id = input(
                    "Enter UPI ID: "
                )

                if (
                    "@" in upi_id
                    and len(upi_id) >= 5
                ):

                    break

                print(
                    "Enter a valid UPI ID."
                )

            print(
                "\nProcessing UPI payment",
                end=""
            )

            for i in range(3):

                time.sleep(1)

                print(
                    ".",
                    end=""
                )

            print()

            console.print(
                "[green]"
                "✓ UPI payment successful"
                "[/green]"
            )

            return "UPI"

        elif choice == "2":

            while True:

                card_number = input(
                    "Enter 16 digit card number: "
                )

                if (
                    card_number.isdigit()
                    and len(card_number) == 16
                ):

                    break

                print(
                    "Card number must contain "
                    "16 digits."
                )

            print(
                "\nProcessing card payment",
                end=""
            )

            for i in range(3):

                time.sleep(1)

                print(
                    ".",
                    end=""
                )

            print()

            console.print(
                "[red]"
                "✓ Card payment successful"
                "[/green]"
            )

            return "CARD"

        else:

            print(
                "Please select 1 or 2."
            )