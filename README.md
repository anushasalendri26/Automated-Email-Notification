# Task 3: Automated Email Notification System

## Description

This project is a Python-based automated email notification system that reads a list of customer email addresses from a text file and sends personalized confirmation emails automatically.

The project also demonstrates secure management of email credentials using environment variables and a `.env` file instead of storing passwords directly in the Python code.

## Tech Stack

* Python
* smtplib
* email.mime
* python-dotenv

## Features

* Reads customer email addresses from a text file
* Sends personalized confirmation emails
* Uses Gmail SMTP for email delivery
* Uses `python-dotenv` to load credentials securely
* Avoids hardcoding passwords in the source code
* Handles email-sending errors

## Project Structure

```text
Task3-Automated-Email-Notification/
│
├── email_sender.py
├── customers.txt
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

Install the required package:

```bash
pip install python-dotenv
```

Or install using:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project folder:

```text
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_APP_PASSWORD=your_app_password
```

Do not upload the `.env` file to GitHub.

The `.env` file is protected using `.gitignore`.

## Customer Email File

Add customer email addresses to `customers.txt`, one email address per line:

```text
customer1@example.com
customer2@example.com
customer3@example.com
```

## How to Run

Run the following command in the terminal:

```bash
python email_sender.py
```

## Sample Output

```text
Email sent successfully to: customer1@example.com
Email sent successfully to: customer2@example.com
Email sent successfully to: customer3@example.com
```

## Security

Sensitive credentials should never be hardcoded in the Python source code or uploaded to GitHub.

This project uses a `.env` file to store the email address and app password securely.

The `.env` file is excluded from GitHub using:

```text
.env
```

in the `.gitignore` file.

## Learning Outcomes

Through this project, I learned:

* Python email automation
* SMTP communication
* Sending emails using `email.mime`
* Reading data from files
* Environment variable management
* Secure handling of credentials
* Error handling in Python

## Conclusion

This project demonstrates how Python can be used to automate personalized email notifications while following basic security practices for protecting sensitive credentials.

