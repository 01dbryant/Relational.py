# Relational.py - SQLAlchemy Shop Database

A simple Python application demonstrating SQLAlchemy ORM with a shop database containing users, products, and orders.

## Features

- User management with email validation
- Product catalog with pricing
- Order tracking system
- SQLite database backend
- Automatic database creation and seeding

## Setup Instructions

1. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   ```bash
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```bash
   pip install sqlalchemy
   ```

4. **Run the application:**
   ```bash
   python Relational.py
   ```

## What It Does

The application will:
- Create a SQLite database (`shop.db`) if it doesn't exist
- Populate it with sample users, products, and orders
- Display all users, products, and orders
- Update a product price (Laptop: $1000 → $1200)
- Delete a user and their associated orders

## Database Schema

- **Users**: id, name, email
- **Products**: id, name, price
- **Orders**: id, user_id, product_id, quantity

## Requirements

- Python 3.x
- SQLAlchemy
