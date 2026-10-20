
# ===== Shoe Inventory Management System =====

from pathlib import Path

# Store inventory.txt in the same folder as inventory.py.
INVENTORY_FILE = Path(__file__).resolve().parent / "inventory.txt"

# Create an empty list to store shoe objects.
shoes_list = []


class Shoe:
    """Represent a shoe in the inventory."""

    def __init__(self, country, code, product, cost, quantity):
        """Initialise the shoe attributes."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of shoes in stock."""
        return self.quantity

    def __str__(self):
        """Return the shoe details as a readable string."""
        return (
            f"Country: {self.country}, "
            f"Code: {self.code}, "
            f"Product: {self.product}, "
            f"Cost: R{self.cost:.2f}, "
            f"Quantity: {self.quantity}"
        )


# ===== Read Shoes Data =====

def read_shoes_data():
    """Read shoe records from inventory.txt into shoes_list."""

    shoes_list.clear()

    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            # Skip the header line.
            next(file)

            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    country, code, product, cost, quantity = (
                        value.strip() for value in line.split(",")
                    )

                    shoe = Shoe(
                        country,
                        code,
                        product,
                        float(cost),
                        int(quantity)
                    )

                    shoes_list.append(shoe)

                except (ValueError, TypeError):
                    print(f"Skipping invalid inventory record: {line}")

        print(f"{len(shoes_list)} shoe records loaded successfully.")

    except FileNotFoundError:
        print("Error: inventory.txt could not be found.")

    except OSError as error:
        print(f"Error reading inventory.txt: {error}")


# ===== Save Inventory Data =====

def save_shoes_data():
    """Save all shoe objects to inventory.txt."""

    try:
        with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoes_list:
                file.write(
                    f"{shoe.country},"
                    f"{shoe.code},"
                    f"{shoe.product},"
                    f"{shoe.cost:g},"
                    f"{shoe.quantity}\n"
                )

        return True

    except OSError as error:
        print(f"Error saving inventory: {error}")
        return False


# ===== Capture New Shoes =====

def capture_shoes():
    """Capture a new shoe and save it to the inventory."""

    print("\n===== Capture New Shoe =====")

    country = input("Enter the country: ").strip()
    code = input("Enter the shoe code: ").strip()
    product = input("Enter the product name: ").strip()

    if not country or not code or not product:
        print("Country, code and product cannot be empty.")
        return

    # Validate the cost.
    while True:
        try:
            cost = float(input("Enter the cost: "))

            if cost <= 0:
                print("Cost must be greater than zero.")
                continue

            break

        except ValueError:
            print("Please enter a valid numerical cost.")

    # Validate the quantity.
    while True:
        try:
            quantity = int(input("Enter the quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            break

        except ValueError:
            print("Please enter a valid whole number.")

    # Prevent duplicate shoe codes.
    for shoe in shoes_list:
        if shoe.code.lower() == code.lower():
            print("A shoe with this code already exists.")
            return

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(new_shoe)

    if save_shoes_data():
        print("New shoe captured successfully.")
        print(new_shoe)
    else:
        shoes_list.remove(new_shoe)
        print("The new shoe was not saved.")


# ===== View All Shoes =====

def view_all():
    """Display all shoes in the inventory."""

    print("\n===== All Shoes =====")

    if not shoes_list:
        print("There are no shoes in the inventory.")
        return

    for shoe in shoes_list:
        print(shoe)


# ===== Restock Shoes =====

def re_stock():
    """Find the shoe with the lowest quantity and restock it."""

    if not shoes_list:
        print("There are no shoes in the inventory.")
        return

    # Find the shoe with the lowest quantity.
    lowest_shoe = min(shoes_list, key=lambda shoe: shoe.quantity)

    print("\n===== Shoe Requiring Restocking =====")
    print(lowest_shoe)

    choice = input(
        "Would you like to restock this shoe? (Y/N): "
    ).strip().lower()

    if choice != "y":
        print("No stock was added.")
        return

    while True:
        try:
            additional_quantity = int(
                input("Enter the quantity to add: ")
            )

            if additional_quantity <= 0:
                print("Enter a quantity greater than zero.")
                continue

            break

        except ValueError:
            print("Please enter a valid whole number.")

    old_quantity = lowest_shoe.quantity
    lowest_shoe.quantity += additional_quantity

    if save_shoes_data():
        print("Stock updated successfully.")
        print(lowest_shoe)
    else:
        lowest_shoe.quantity = old_quantity
        print("The stock update could not be saved.")


# ===== Search for a Shoe =====

def search_shoe():
    """Search for a shoe using its unique code."""

    if not shoes_list:
        print("There are no shoes in the inventory.")
        return

    code = input("Enter the shoe code to search for: ").strip()

    for shoe in shoes_list:
        if shoe.code.lower() == code.lower():
            print("\n===== Shoe Found =====")
            print(shoe)
            return shoe

    print("No shoe was found with that code.")
    return None


# ===== Calculate Value Per Item =====

def value_per_item():
    """Calculate and display the total stock value of each shoe."""

    if not shoes_list:
        print("There are no shoes in the inventory.")
        return

    print("\n===== Inventory Value =====")

    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()

        print(
            f"Product: {shoe.product} | "
            f"Cost: R{shoe.get_cost():.2f} | "
            f"Quantity: {shoe.get_quantity()} | "
            f"Total value: R{value:.2f}"
        )


# ===== Find Shoe With Highest Quantity =====

def highest_qty():
    """Find the shoe with the highest quantity for sale."""

    if not shoes_list:
        print("There are no shoes in the inventory.")
        return

    highest_shoe = max(shoes_list, key=lambda shoe: shoe.quantity)

    print("\n===== Shoe With Highest Quantity For Sale =====")
    print(highest_shoe)


# ===== Main Menu =====

def main():
    """Display the menu and execute the selected function."""

    read_shoes_data()

    while True:
        print("\n======================================")
        print("       SHOE INVENTORY MANAGEMENT")
        print("======================================")
        print("1. View all shoes")
        print("2. Capture a new shoe")
        print("3. Restock shoes")
        print("4. Search for a shoe")
        print("5. Calculate inventory value")
        print("6. Find shoe with highest quantity")
        print("7. Reload inventory from file")
        print("8. Exit")
        print("======================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            view_all()

        elif choice == "2":
            capture_shoes()

        elif choice == "3":
            re_stock()

        elif choice == "4":
            search_shoe()

        elif choice == "5":
            value_per_item()

        elif choice == "6":
            highest_qty()

        elif choice == "7":
            read_shoes_data()

        elif choice == "8":
            print("Thank you for using the Shoe Inventory Management System.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()