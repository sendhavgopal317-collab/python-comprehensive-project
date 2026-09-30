import sqlite3
from rich.console import Console
from rich.table import Table


console = Console()


def choose_language():

    connection = sqlite3.connect("gopal_multiplex.db")
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT language FROM movies")

    languages = cursor.fetchall()

    connection.close()

    table = Table(title="SELECT LANGUAGE")

    table.add_column("No.")
    table.add_column("Language")

    for number, language in enumerate(languages, start=1):
        table.add_row(
            str(number),
            language[0]
        )

    console.print(table)

    choice = int(input("Enter language number: "))

    selected_language = languages[choice - 1][0]

    return selected_language