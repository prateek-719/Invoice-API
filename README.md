# Invoice-API

A web-based invoice management system built with Django & Django REST framework.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Database Models](#database-models)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

Invoice API is a Django-powered system for efficient management of invoices and associated details. It facilitates tasks such as invoice creation, updates, and retrieval with simplicity and effectiveness.

## Features

Invoice API provides the following features:

- **Invoice Creation:** Users can effortlessly create new invoices, specifying date and customer name.

- **Invoice Details:** Detailed invoice items, including description, quantity, unit price, and total price, can be added or updated.

- **Full CRUD Operations:** Comprehensive support for Create, Read, Update, and Delete operations on both invoices and their details.

- **Payload Handling:** The API efficiently accepts invoice details in the payload, simplifying the creation and update processes.

- **Test Cases:** Robust test cases ensure the reliability of all API endpoints, covering various scenarios.

- **Data Integrity:** The system ensures data integrity, handling multiple details for each invoice with precision.

- **Django Admin Integration:** Models are seamlessly integrated into the Django Admin panel for convenient management.

## Database Models

This project uses the following database models:

- **Invoice:** Stores information about invoices, including date and customer name.

- **InvoiceDeatail:** Represents details of each invoice, such as description, quantity, unit price, and total price.

## Requirements

Before you begin, ensure you have the following requirements installed:

- Python 3.9+
- Django 4.2.8
- Django REST framework 3.14.0

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/Invoice-API.git
   cd Invoice-API
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv  #On Windows, virtualenv virtual_environment_name
   source venv/bin/activate  # On Windows, use: virtual_environment_name\Scripts\activate
   ```
3. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
    ```
4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Make a superuser to access the admin panel (Optional):
   ```bash
   python manage.py createsuperuser
   ```
6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

## Usage

To use Invoice-API, follow these steps:

1. **Access the Django Admin Panel:**

   Use the Django admin panel to manage users, loans, and transactions. Access it at [http://localhost:8000/admin/](http://localhost:8000/admin/).

2. **API Endpoints:**

   Use the following API endpoints to interact with the system:

   - **Create a New Invoice:** 
     ```
     POST: http://localhost:8000/invoices/
     ```
     - **Sample JSON 1 (with details):**
     {
    "date": "2024-01-04",
    "customer_name": "Test Invoice 1",
    "details": [
        {
            "description": "Item 1",
            "quantity": 2,
            "unit_price": 10.0,
            "price": 20.0
        },
        {
            "description": "Item 2",
            "quantity": 3,
            "unit_price": 15.0,
            "price": 45.0
        }
    ]
}
     - **Sample JSON 2 (without details):**
    {
    "date": "2024-01-04",
    "customer_name": "Test Invoice 1"
    }

   - **Get All Invoices:** 
     ```
     GET: http://localhost:8000/invoices/
     ```

   - **Get a Specific Invoice:** 
     ```
     GET: http://localhost:8000/invoices/{invoice_id}/
     ```

   - **Update an Invoice:** 
     ```
     PUT or PATCH: http://localhost:8000/invoices/{invoice_id}/
     ```
     - **Sample JSON:**{
    "date": "2024-01-05",
    "customer_name": "Updated Invoice"
}


   - **Delete an Invoice:** 
     ```
     DELETE: http://localhost:8000/invoices/{invoice_id}/
     ```
   - **Create Invoice Details:** Add details to a specific invoice
     ```
     POST: http://localhost:8000/invoices/{invoice_id}/details/
     ```
     - **Sample JSON:** {
    "invoice": <invoice_id>,
    "description": "New Item",
    "quantity": 1,
    "unit_price": 12.0,
    "price": 12.0
}

   - **Get All Details of an Invoice:** 
     ```
     GET: http://localhost:8000/invoices/{invoice_id}/details/
     ```
   - **Get a Specific Detail of an Invoice:** 
     ```
     GET: http://localhost:8000/invoices/{invoice_id}/details/{detail_id}/
     ```
   - **Update a Detail of an Invoice:** Update details of a specific detail in a specific invoice.
     ```
     PUT or PATCH: http://localhost:8000/invoices/{invoice_id}/details/{detail_id}/
     ```
     - **Sample JSON:** {
    "description": "Updated Item",
    "quantity": 2,
    "unit_price": 15.0,
    "price": 30.0
}

   - **Delete a Detail of an Invoice:** Deletes a specific detail of a specific invoice.
     ```
     DELETE: http://localhost:8000/invoices/{invoice_id}/details/{detail_id}/
     ```
   
**If you have any questions or need further assistance, feel free to contact me:**
- Email: ritika310302@gmail.com

## Happy Coding!

   



