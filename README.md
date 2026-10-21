# Shoe Inventory Management System

Project Description

The Shoe Inventory Management System is a Python application that manages shoe stock records using a text file. It allows users to view shoes, add new shoes, restock items, search by shoe code, calculate inventory values, and identify shoes with the highest and lowest quantities.

## Features

View all shoes in the inventory.

Capture new shoe records.

Restock shoes with the lowest quantity.

Search for a shoe using its unique code.

Calculate the total value of stock for each shoe.

Find the shoe with the highest quantity.

Reload inventory data from the text file.

Validate user input and prevent duplicate shoe codes.

Technologies Used

Python 3

File handling

Object-oriented programming

pathlib module

Project Files

inventory.py — contains the main program and inventory management functions.

inventory.txt — stores the shoe inventory records.

How to Run

Install Python 3.

Ensure inventory.py and inventory.txt are in the same folder.

Open the project folder in VS Code.

Open the terminal.

Run the program using:

python inventory.py

Inventory File Format

The inventory.txt file must contain a header followed by comma-separated records in this format:

Country,Code,Product,Cost,Quantity

Example:

South Africa,SKU001,Nike Air Max,1500,10

Purpose

This project demonstrates Python classes, functions, file handling, input validation, and basic inventory management.
