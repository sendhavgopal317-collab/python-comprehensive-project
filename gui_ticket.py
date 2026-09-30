import customtkinter as ctk


def show_ticket_window(ticket):

    window = ctk.CTk()

    window.title("GOPAL Multiplex - Booking Ticket")
    window.geometry("700x750")

    # =========================
    # TITLE
    # =========================

    title = ctk.CTkLabel(
        window,
        text="🎬 GOPAL MULTIPLEX",
        font=("Arial", 30, "bold")
    )

    title.pack(pady=(25, 5))

    subtitle = ctk.CTkLabel(
        window,
        text="MOVIE TICKET",
        font=("Arial", 18, "bold")
    )

    subtitle.pack(pady=(0, 20))


    # =========================
    # TICKET FRAME
    # =========================

    ticket_frame = ctk.CTkFrame(
        window,
        corner_radius=15
    )

    ticket_frame.pack(
        padx=40,
        pady=10,
        fill="both",
        expand=True
    )


    # =========================
    # TICKET INFORMATION
    # =========================

    ticket_id = ctk.CTkLabel(
        ticket_frame,
        text="Ticket ID: " + str(ticket["ticket_id"]),
        font=("Arial", 18, "bold"),
        anchor="w"
    )

    ticket_id.pack(
        padx=30,
        pady=(30, 15),
        fill="x"
    )


    customer = ctk.CTkLabel(
        ticket_frame,
        text="Customer Name: " + str(ticket["customer_name"]),
        font=("Arial", 16),
        anchor="w"
    )

    customer.pack(
        padx=30,
        pady=8,
        fill="x"
    )


    phone = ctk.CTkLabel(
        ticket_frame,
        text="Phone: " + str(ticket["phone"]),
        font=("Arial", 16),
        anchor="w"
    )

    phone.pack(
        padx=30,
        pady=8,
        fill="x"
    )


    movie = ctk.CTkLabel(
        ticket_frame,
        text="Movie: " + str(ticket["movie_name"]),
        font=("Arial", 18, "bold"),
        anchor="w"
    )

    movie.pack(
        padx=30,
        pady=8,
        fill="x"
    )


    language = ctk.CTkLabel(
        ticket_frame,
        text="Language: " + str(ticket["language"]),
        font=("Arial", 16),
        anchor="w"
    )

    language.pack(
        padx=30,
        pady=8,
        fill="x"
    )


    show_time = ctk.CTkLabel(
        ticket_frame,
        text="Show Time: " + str(ticket["show_time"]),
        font=("Arial", 16),
        anchor="w"
    )

    show_time.pack(
        padx=30,
        pady=8,
        fill="x"
    )


    seats = ctk.CTkLabel(
        ticket_frame,
        text="Seats: " + str(ticket["seats"]),
        font=("Arial", 16),
        anchor="w"
    )

    seats.pack(
        padx=30,
        pady=8,
        fill="x"
    )


    payment_type = ctk.CTkLabel(
        ticket_frame,
        text="Payment: " + str(ticket["payment_type"]),
        font=("Arial", 16),
        anchor="w"
    )

    payment_type.pack(
        padx=30,
        pady=8,
        fill="x"
    )


    total = ctk.CTkLabel(
        ticket_frame,
        text="Total Amount: ₹" + str(ticket["total"]),
        font=("Arial", 22, "bold"),
        anchor="w"
    )

    total.pack(
        padx=30,
        pady=15,
        fill="x"
    )


    booking_date = ctk.CTkLabel(
        ticket_frame,
        text="Booking Date: " + str(ticket["booking_date"]),
        font=("Arial", 14),
        anchor="w"
    )

    booking_date.pack(
        padx=30,
        pady=8,
        fill="x"
    )


    # =========================
    # CLOSE BUTTON
    # =========================

    close_button = ctk.CTkButton(
        window,
        text="CLOSE",
        font=("Arial", 16, "bold"),
        width=200,
        height=45,
        command=window.destroy
    )

    close_button.pack(
        pady=25
    )


    # =========================
    # START WINDOW
    # =========================

    window.mainloop()