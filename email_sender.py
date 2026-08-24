import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Load environment variables from .env
load_dotenv()

sender_email = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("EMAIL_APP_PASSWORD")


def send_email(receiver_email):
    # Create email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Tour Enquiry Confirmation"

    body = f"""
Hello,

Thank you for contacting us regarding your tour enquiry.

We have successfully received your enquiry associated with {receiver_email}.

Our team will contact you shortly with further details.

Best regards,
Tour Enquiry Team
"""

    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(message)

        print(f"Email sent successfully to: {receiver_email}")

    except Exception as error:
        print(f"Failed to send email to {receiver_email}")
        print("Error:", error)


def main():
    try:
        with open("customers.txt", "r", encoding="utf-8") as file:
            customers = [
                line.strip()
                for line in file
                if line.strip()
            ]

        if not customers:
            print("No customer email addresses found.")
            return

        for email in customers:
            send_email(email)

    except FileNotFoundError:
        print("customers.txt file not found.")


if __name__ == "__main__":
    main()
