# SE-4458-Midterm

## ✈️ Flight Booking API
This project is a simplified flight booking system built using FastAPI. It supports the following key functionalities:

* Adding and querying flights

* Buying tickets and checking in

* Listing passengers of a specific flight

## 🧱 Design Overview
The API is split into the following modules:

### Flights

* Add new flights

* Query available flights with pagination

### Tickets

* Buy tickets

* Check-in process

### Passengers

Get a paginated list of passengers on a specific flight

Each endpoint is protected using an authentication dependency (get_current_user) to simulate secure access.

## Database Models
Three core SQLAlchemy models:

* FlightDB: Represents a flight with metadata like date, airports, capacity, and one-way flag.

* TicketDB: Represents a ticket booked by a passenger.

* UserDB: Dummy user authentication system for demonstration.

## 🧠 Assumptions
A simple dict-based mock authentication is used (get_current_user). In production, this should be replaced with real JWT-based authentication.

Pagination is handled manually in services or using FastAPI Pagination where supported.

Ticket capacity enforcement is assumed to be handled inside the FlightService (not shown here).

Dates are passed as query parameters in ISO format (yyyy-mm-ddThh:mm:ss) in the API.

The relationship between tickets and flights is handled via flight_number and date, assuming uniqueness.

⚠️ Issues Encountered
Pagination Limitation: The fastapi-pagination library wasn't fully utilized across all endpoints due to differing return formats.

Date Matching: Precise flight matching by date required careful datetime parsing to avoid mismatches.

Scalability Concerns: The current in-memory FlightService, TicketService, and PassengerService implementations would not scale for production use.

No foreign key constraints: Relationships (e.g., between tickets and flights) are loosely enforced by logic, not by schema.



![ER Diagram ](https://github.com/user-attachments/assets/4dfb8613-db92-4207-9089-db7a17ac8428)

## Video of system working: https://drive.google.com/file/d/1-XJqkss4TEBbRWfbhqL_4BY3ieA8GiP7/view?usp=drive_link
