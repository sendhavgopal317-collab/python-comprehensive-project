import sqlite3

from rich.console import Console
from rich.table import Table


console = Console()


def show_movies(language):

    connection = sqlite3.connect(
        "gopal_multiplex.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM movies
        WHERE language = ?
    """, (language,))

    movies = cursor.fetchall()

    connection.close()

    table = Table(
        title=f"🎬 {language.upper()} MOVIES"
    )

    table.add_column(
        "No.",
        justify="center"
    )

    table.add_column("Movie")

    table.add_column("Language")

    table.add_column("Duration")

    table.add_column(
        "Price",
        justify="center"
    )

    for movie in movies:

        table.add_row(
            str(movie[0]),
            movie[1],
            movie[2],
            movie[3],
            "₹" + str(movie[4])
        )

    console.print(table)

    return movies


def choose_movie(language):

    movies = show_movies(language)

    while True:

        choice = input(
            "\nEnter movie number: "
        )

        if choice.isdigit():

            choice = int(choice)

            for movie in movies:

                if movie[0] == choice:

                    console.print(
                        f"\n[green]✓ "
                        f"{movie[1]} selected"
                        f"[/green]"
                    )

                    return movie

        console.print(
            "[red]Please enter a valid movie number.[/red]"
        )