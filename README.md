# 🚌 Bus Booking System

A simple **Bus Booking System** developed as a team project for the **final lab examination of Computational Problem Solving (CPS)** during the first semester.

The project demonstrates fundamental Python programming concepts such as **dictionaries, functions, loops, conditional statements, lists, user input, and basic authentication logic**.

> 🎓 **Academic Project**
> Developed as part of the First Semester Computational Problem Solving Lab Examination.

---

## 📌 Project Overview

The Bus Booking System is a command-line-based Python application that allows users to:

* Create a user account
* Enter a phone number and password
* Log in using their credentials
* Search for buses based on starting and ending locations
* Check bus category and fare
* Check seat availability
* Generate a basic booking receipt
* Handle blocked accounts

The system uses Python dictionaries to store bus and account information during program execution.

---

## ✨ Features

### 👤 Account Creation

Users can create an account by providing:

* User ID / Email
* 10-digit phone number
* Password

The account is assigned an active status by default.

### 🔐 Login System

Users can log in using their registered User ID and password.

The system checks:

* Whether the user exists
* Whether the entered password is correct
* Whether the account is active or blocked

### 🚌 Bus Search

Users can enter:

```text
Start Location
End Location
```

The program searches the available buses and displays matching buses.

### 💺 Seat Availability

The system checks whether seats are available before proceeding with a booking.

### 🎫 Booking Receipt

A basic booking receipt is displayed containing information such as:

* User ID
* Bus number
* Starting point
* Destination
* Bus category
* Fare
* Seats available after booking

### 🚫 Account Blocking

The project also demonstrates basic account-status handling by allowing an account to have a `blocked` status.

---

## 🛠️ Technologies Used

* **Python 3**
* Python Dictionaries
* Python Functions
* Loops
* Conditional Statements
* Lists
* User Input / Command Line Interface

No external libraries are required.

---

## 📂 Project Structure

```text
Bus-Booking-System/
│
├── CPS HACKATHON CODE.py
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Protocol-Wizard/wayfarer.git
```

### 2. Open the project folder

```bash
cd wayfarer
```

### 3. Run the Python program

```bash
python "CPS HACKATHON CODE.py"
```

Depending on your system, you may need:

```bash
python3 "CPS HACKATHON CODE.py"
```

---

## 🧠 Concepts Demonstrated

This project was created during the first semester, so its primary purpose was to demonstrate fundamental **Computational Problem Solving** concepts.

### Data Structures

Python dictionaries are used to represent buses and user accounts.

For example:

```python
buses = {
    1: {
        'startpoint': 'Chennai',
        'endpoint': 'Madurai',
        'fare': 670,
        'totalseats': 20,
        'seatsavailable': 6,
        'category': 'AC'
    }
}
```

### Functions

The program is divided into functions such as:

```python
account()
login()
```

This provides a basic modular structure.

### Conditional Logic

`if`, `elif`, and `else` statements are used for:

* Validating phone numbers
* Checking login credentials
* Checking account status
* Matching routes
* Checking seat availability
* Identifying bus categories

### Loops

`while` and `for` loops are used for:

* Creating multiple accounts
* Searching through accounts
* Searching through available buses

---

## 🚌 Sample Bus Data

The program contains sample bus information including routes such as:

| Bus | Route                  | Category |   Fare | Available Seats |
| --: | ---------------------- | -------- | -----: | --------------: |
|   1 | Chennai → Madurai      | AC       |   ₹670 |               6 |
|   2 | Bangalore → Mysore     | AC       | ₹1,220 |               7 |
|   3 | Chennai → Madurai      | Non-AC   | ₹1,040 |               0 |
|   4 | Bangalore → Mysore     | Non-AC   | ₹1,400 |               4 |
|   5 | Vijayawada → Hyderabad | AC       | ₹1,001 |               3 |
|   6 | Chennai → Bangalore    | AC       |   ₹420 |               7 |
|   7 | Vijayawada → Hyderabad | Non-AC   | ₹1,000 |               0 |
|   8 | Chennai → Bangalore    | Non-AC   | ₹1,500 |               8 |
|   9 | Bangalore → Mangalore  | Non-AC   | ₹1,000 |              20 |
|  10 | Coimbatore → Ooty      | AC       |   ₹999 |              19 |

---

## ⚠️ Limitations & Disadvantages

This project was developed as a **first-semester academic lab project**, so it has several limitations and should not be considered a production-ready booking application.

### 1. No Database

All user and bus information is stored in Python dictionaries.

Once the program terminates, the data is lost.

A real application would require a database such as:

* MySQL
* PostgreSQL
* SQLite

### 2. Passwords Are Not Securely Stored

Passwords are stored directly in memory as plain text.

A real-world application should use secure password hashing techniques such as:

* bcrypt
* Argon2
* PBKDF2

### 3. No Actual Seat Reservation

Although the program displays a booking confirmation and calculates the number of seats after booking, the underlying bus data is not permanently updated.

Therefore, the same seat availability can remain unchanged during subsequent operations.

### 4. No Seat Selection

Users cannot choose a specific seat.

For example, there is no functionality for:

```text
Seat 1
Seat 2
Seat 3
...
Seat 20
```

The system only works with the overall number of available seats.

### 5. No Payment System

The project does not include:

* Online payment
* Payment verification
* Transaction history
* Refunds
* Payment receipts

### 6. Command-Line Interface

The application runs entirely in the terminal.

There is no graphical user interface or web interface.

### 7. Limited Input Validation

Only basic validation is implemented, such as checking whether the phone number contains 10 digits.

More comprehensive validation would be required for a real application.

### 8. Hardcoded Data

Bus information is directly written into the Python program.

Adding, removing, or modifying buses requires changing the source code.

### 9. Limited User Management

There are no advanced features such as:

* Password reset
* Email verification
* Profile management
* Account recovery
* Multiple user roles

### 10. No Booking History

Users cannot view their previous bookings.

A real system would maintain a booking history containing information such as:

```text
Booking ID
User
Bus
Route
Date
Seat
Fare
Booking Status
```

### 11. No Date or Time Selection

The system does not allow users to select a travel date or departure time.

### 12. No Cancellation System

There is currently no functionality for cancelling a booking or receiving a refund.

---

## 🚀 Possible Future Improvements

The project can be extended significantly.

Some possible improvements include:

* 🗄️ Add MySQL/SQLite database integration
* 🖥️ Develop a GUI using Tkinter or PyQt
* 🌐 Convert the system into a web application
* 🔐 Implement password hashing
* 💺 Add individual seat selection
* 📅 Add travel dates and departure times
* 💳 Integrate a payment system
* 🎫 Generate unique booking IDs
* 📜 Add booking history
* ❌ Add cancellation and refund functionality
* 👤 Add user profiles
* 🚌 Add an administrator interface
* 🔎 Add advanced bus filtering
* 📧 Add email/SMS booking confirmation
* 📊 Add administrative reports and statistics

---

## 📚 Academic Purpose

This project was created as a **final lab examination project for Computational Problem Solving during the first semester**.

The main objective was not to develop a commercial booking platform, but to apply the programming and problem-solving concepts learned during the course to a practical problem.

The project helped demonstrate the use of:

**Problem → Algorithm → Data Structures → Python Implementation → Output**

---

## 👥 Team Project

This project was developed collaboratively as a team for the Computational Problem Solving final lab examination.

> **Team Members:**
>
> * [Logicweaver715](https://github.com/Logicweaver715)
> * [Kayab6](https://github.com/Kayab6)
> * [Kage-no-Yume](https://github.com/Kage-no-Yume)
> * [Protocol-Wizard](https://github.com/Protocol-Wizard)

---

## 📄 Project Status

**Status:** Completed – Academic Project

This repository represents the version of the project developed for the **First Semester Computational Problem Solving Lab Examination**.

It is preserved as an academic project and as a record of our early programming work.

---

## ⭐ Acknowledgement

This project was developed as part of the **Computational Problem Solving** course during the first semester.

The project provided practical experience in applying basic programming concepts to a real-world-inspired problem.

---

## 📜 License

This project is intended primarily for **educational and academic purposes**.

You are free to study and modify the code for learning purposes.
