# assignment-03-bitsom_ba_2511918_python_assignment_part3
Part 3: File I/O, APIs &amp; Exception Handling
Theme: Product Explorer & Error-Resilient Logger

Build a program that fetches real product data from a public API, processes it, saves results to files, and handles all failure scenarios gracefully — just like a production-grade application.
Task 1: File Read & Write Basics
Part A: Write
Create a Python script that writes the student notes to a file called python_notes.txt.
Append two more lines of your own to the same file using append mode ('a').
Print a confirmation message after each file operation.
Part B: Read
Read the file back and print each line numbered, stripping the trailing newline character (\n) from each line.
Count and print the total number of lines in the file.
Ask the user for a keyword and print all lines that contain that keyword (case-insensitive). If no match is found, print a helpful message.
Task 2: API Integration
Use Python's requests library to interact with the DummyJSON Products API.
Step 1 — Fetch and Display Products:
Make a GET request to fetch 20 products:
https://dummyjson.com/products?limit=20
Parse the JSON response. Each product has fields including id, title, category, price, and rating.
Print a formatted table
Step 2 — Filter and Sort:
From the 20 fetched products, filter only those with a rating ≥ 4.5.
Sort the filtered list by price in descending order and print the result.
Step 3 — Search by Category.
Make a GET request to fetch all products in the laptops category: "https://dummyjson.com/products/category/laptops", and print the name and price of each laptop found.
Step 4 — POST Request and print the full response returned by the server.
Task 3: Exception Handling: a). Guarded Calculator b). Guarded File Reader c). Robust API calls d). Input Validation loop
Task 4: Logging to File
Build a simple error logger that writes a timestamped entry to error_log.txt whenever an exception or unexpected response is caught.
