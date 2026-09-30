import tkinter as tk
from tkinter import messagebox

from database import add_movie, delete_movie, get_next_movie_id


ADMIN_PASSWORD = "batch19"


def admin_login():

    window = tk.Toplevel()

    window.title("Admin Login")
    window.geometry("400x300")

    title = tk.Label(
        window,
        text="ADMIN LOGIN",
        font=("Arial", 22, "bold")
    )

    title.pack(pady=30)

    password_label = tk.Label(
        window,
        text="Enter Admin Password",
        font=("Arial", 12)
    )

    password_label.pack(pady=10)

    password_entry = tk.Entry(
        window,
        show="*",
        font=("Arial", 12)
    )

    password_entry.pack(pady=10)

    def check_password():

        password = password_entry.get()

        if password == ADMIN_PASSWORD:

            window.destroy()
            admin_menu()

        else:

            messagebox.showerror(
                "Login Failed",
                "Wrong Admin Password"
            )

    login_button = tk.Button(
        window,
        text="LOGIN",
        command=check_password,
        width=15
    )

    login_button.pack(pady=20)


def admin_menu():

    window = tk.Toplevel()

    window.title("Admin Panel")
    window.geometry("500x900")

    title = tk.Label(
        window,
        text="ADMIN PANEL",
        font=("Arial", 24, "bold")
    )

    title.pack(pady=30)

    add_button = tk.Button(
        window,
        text="ADD MOVIE",
        width=25,
        height=2,
        command=add_movie_window
    )

    add_button.pack(pady=10)

    delete_button = tk.Button(
        window,
        text="DELETE MOVIE",
        width=25,
        height=2,
        command=delete_movie_window
    )

    delete_button.pack(pady=10)

    exit_button = tk.Button(
        window,
        text="EXIT",
        width=25,
        height=2,
        command=window.destroy
    )

    exit_button.pack(pady=10)


def add_movie_window():

    window = tk.Toplevel()

    window.title("Add Movie")
    window.geometry("450x500")

    tk.Label(
        window,
        text="ADD NEW MOVIE",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(
        window,
        text="Movie ID"
    ).pack()

    movie_id = tk.Entry(window)

    movie_id.pack(pady=5)

    # Automatically generate next movie ID
    next_id = get_next_movie_id()

    movie_id.insert(0, str(next_id))

    # User cannot change the automatically generated ID
    movie_id.config(state="readonly")


    tk.Label(
        window,
        text="Movie Name"
    ).pack()

    movie_name = tk.Entry(window)

    movie_name.pack(pady=5)


    tk.Label(
        window,
        text="Language"
    ).pack()

    language = tk.Entry(window)

    language.pack(pady=5)


    tk.Label(
        window,
        text="Duration"
    ).pack()

    duration = tk.Entry(window)

    duration.pack(pady=5)


    tk.Label(
        window,
        text="Ticket Price"
    ).pack()

    price = tk.Entry(window)

    price.pack(pady=5)


    def save_movie():

        movie_id.config(state="normal")

        add_movie(
            int(movie_id.get()),
            movie_name.get(),
            language.get(),
            duration.get(),
            int(price.get())
        )

        messagebox.showinfo(
            "Success",
            "Movie added successfully"
        )

        window.destroy()


    tk.Button(
        window,
        text="ADD MOVIE",
        width=20,
        command=save_movie
    ).pack(pady=25)


def delete_movie_window():

    window = tk.Toplevel()

    window.title("Delete Movie")
    window.geometry("400x300")

    tk.Label(
        window,
        text="DELETE MOVIE",
        font=("Arial", 20, "bold")
    ).pack(pady=30)

    tk.Label(
        window,
        text="Enter Movie ID"
    ).pack()

    movie_id = tk.Entry(window)

    movie_id.pack(pady=10)


    def remove_movie():

        deleted = delete_movie(
            int(movie_id.get())
        )

        if deleted > 0:

            messagebox.showinfo(
                "Success",
                "Movie deleted successfully"
            )

            window.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Movie ID not found"
            )


    tk.Button(
        window,
        text="DELETE MOVIE",
        width=20,
        command=remove_movie
    ).pack(pady=20)