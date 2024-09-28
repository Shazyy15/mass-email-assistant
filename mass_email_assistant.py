import tkinter as tk
from tkinter import messagebox, Scrollbar, Frame, Canvas
import smtplib

# Global list to store recipient entries dynamically
recipient_entries = []

# Function to dynamically create email input fields for multiple recipients
def create_email_entries():
    num_recipients = int(num_recipients_entry.get())

    # Clear previous recipient entries
    for entry in recipient_entries:
        entry.destroy()
    recipient_entries.clear()

    # Create recipient email entries dynamically
    for i in range(num_recipients):
        label = tk.Label(recipient_frame, text=f"Recipient Email {i+1}:", bg="#f0f0f0")
        label.pack(pady=5)
        recipient_entry = tk.Entry(recipient_frame, width=40)
        recipient_entry.pack(pady=5)
        recipient_entries.append(recipient_entry)

    # Refresh the scrollbar after adding the new entries
    recipient_canvas.config(scrollregion=recipient_canvas.bbox("all"))

# Function to send the email
def send_email():
    try:
        # Sender details
        sender_email = "myemail@gmail.com"
        password = "mypass"

        # Get the subject and message body from user inputs
        subject = subject_entry.get()
        message_body = message_body_entry.get("1.0", "end-1c")

        # Create the email message
        email_message = f"Subject: {subject}\n\n{message_body}"

        # Initialize SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        # Get recipient emails and send to each
        for entry in recipient_entries:
            receiver_email = entry.get()
            if receiver_email:
                server.sendmail(sender_email, receiver_email, email_message)

        server.quit()
        messagebox.showinfo("Success", "Email sent successfully to all recipients.")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

# GUI setup
app = tk.Tk()
app.title("Virtual Assistant - Email Sender")
app.geometry("500x750")
app.config(bg="#f0f0f0")

# Subject Label and Entry
tk.Label(app, text="Email Subject:", bg="#f0f0f0", font=("Helvetica", 12, "bold")).pack(pady=10)
subject_entry = tk.Entry(app, width=50)
subject_entry.pack(pady=5)

# Message Body Label and Text Area
tk.Label(app, text="Email Message:", bg="#f0f0f0", font=("Helvetica", 12, "bold")).pack(pady=10)
message_body_entry = tk.Text(app, height=10, width=50)
message_body_entry.pack(pady=5)

# Number of Recipients Label and Entry
tk.Label(app, text="Number of Recipients:", bg="#f0f0f0", font=("Helvetica", 12, "bold")).pack(pady=10)
num_recipients_entry = tk.Entry(app, width=10)
num_recipients_entry.pack(pady=5)

# Button to create recipient email input fields
create_recipients_button = tk.Button(app, text="Create Recipient Email Fields", command=create_email_entries)
create_recipients_button.pack(pady=10)

# Scrollable Frame for recipient emails
recipient_frame_outer = Frame(app, bg="#f0f0f0", height=200)
recipient_frame_outer.pack(fill="both", expand=True, padx=10, pady=10)

recipient_canvas = Canvas(recipient_frame_outer, bg="#f0f0f0")
recipient_frame = Frame(recipient_canvas, bg="#f0f0f0")

recipient_scrollbar = Scrollbar(recipient_frame_outer, orient="vertical", command=recipient_canvas.yview)
recipient_canvas.configure(yscrollcommand=recipient_scrollbar.set)

recipient_scrollbar.pack(side="right", fill="y")
recipient_canvas.pack(side="left", fill="both", expand=True)
recipient_canvas.create_window((0, 0), window=recipient_frame, anchor="nw")

# Ensure the scrollbar gets updated when new fields are added
recipient_frame.bind("<Configure>", lambda e: recipient_canvas.config(scrollregion=recipient_canvas.bbox("all")))

# Button to send the email at the bottom of the UI
send_button = tk.Button(app, text="Send Email", command=send_email, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
send_button.pack(pady=10)

# Developer credit at the bottom
credit_frame = tk.Frame(app, bg="#f0f0f0")
credit_frame.pack(pady=10, fill="both")
credit_label = tk.Label(credit_frame, text="Developed by Shazil Shahid", bg="#f0f0f0", font=("Helvetica", 10, "italic"))
credit_label.pack(pady=10)

# Run the application
app.mainloop()
