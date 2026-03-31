#Task 2: API Integration 

import requests

url = "https://dummyjson.com/products?limit=20"
#---------------------------------------
#Step 1: Fetch and Display Products
response = requests.get(url)
data = response.json()
products = data.get("products", [])

# Print table header
print(f"{'ID':<4} | {'Title':<30} | {'Category':<15} | {'Price':<10} | {'Rating':<6}")
print("-" * 80)

# Print product data
for product in products:
        product_id = product.get("id")
        title = product.get("title", "")[:30]  # limit title length
        category = product.get("category")
        price = product.get("price")
        rating = product.get("rating")

        print(f"{product_id:<4} | {title:<30} | {category:<15} | ${price:<9} | {rating:<6}")

#Step 2: Filter and Sort

filtered_products = [p for p in products if p.get("rating", 0) >= 4.5] #Filter products with ratings>=4.5

#sort by price (descending)
sorted_products = sorted(filtered_products, key=lambda i: i.get("price", 0), reverse=True) 

# Print filtered and sorted results
print("\n--- Filtered (Rating ≥ 4.5) & Sorted by Price (Descending) ---")
print(f"{'ID':<4} | {'Title':<30} | {'Price':<10} | {'Rating':<6}")
print("-" * 50)

for product in sorted_products:
        print(f"{product['id']:<4} | {product['title'][:30]:<30} | ${product['price']:<9} | {product['rating']:<6}")

#Step 3: Search by Category

print("\n--- Laptops Category ---")

laptop_url = "https://dummyjson.com/products/category/laptops"
laptop_response = requests.get(laptop_url)
laptop_data = laptop_response.json()
laptops = laptop_data.get("products", [])

for laptop in laptops:
        print(f"{laptop.get('title')} - ${laptop.get('price')}")

#Step 4: Post request - send data
print("\n--- Adding New Product (POST Request) ---")

post_url = "https://dummyjson.com/products/add"

new_product = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"
    }

post_response = requests.post(post_url, json=new_product)
post_response.raise_for_status()

result = post_response.json()

print("\nResponse from server:")
print(result)
#----------------------------------------------------------
#Task 3: Exception Handling
#Part A: Guarded Calculator
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


# Test cases
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

#Part B: Guarded File Reader
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")


# Test cases
print("\nReading python_notes.txt:")
print(read_file_safe("python_notes.txt"))

print("\nReading ghost_file.txt:")
print(read_file_safe("ghost_file.txt"))

#Part C: Robust API Calls
import requests

def safe_get(url, params=None):
    try:
        response = requests.get(url, params=params, timeout=5)
        return response
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:", e)


def safe_post(url, data):
    try:
        response = requests.post(url, json=data, timeout=5)
        return response
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:", e)

response = safe_get(f"{"https://dummyjson.com"}/products", params={"limit": 20})
if response:
    data = response.json()
    print("Fetched products successfully.")

#Part D: Input validation loop
import requests

while True:
    user_input = input("\nEnter a product ID to look up (1–100), or 'quit' to exit: ")

    if user_input.lower() == "quit":
        print("Exiting program.")
        break

    # Validate input
    if not user_input.isdigit():
        print("Invalid input. Please enter a number between 1 and 100.")
        continue

    product_id = int(user_input)

    if product_id < 1 or product_id > 100:
        print("Invalid range. Please enter a number between 1 and 100.")
        continue

    # API call with exception handling
    try:
        response = requests.get(f"{"https://dummyjson.com"}/products/{product_id}", timeout=5)

        if response.status_code == 404:
            print("Product not found.")
        elif response.status_code == 200:
            product = response.json()
            print(f"Title: {product.get('title')}")
            print(f"Price: ${product.get('price')}")
        else:
            print("Unexpected response:", response.status_code)

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:", e)