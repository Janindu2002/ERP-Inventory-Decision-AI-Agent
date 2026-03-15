from data_loader import load_inventory_data
from analysis_engine import find_low_stock, calculate_days_remaining, urgent_reorder
from invoice_generator import generate_invoice


DATA_FILE = "data/inventory_data.csv"


def run_inventory_analysis():

    data = load_inventory_data(DATA_FILE)

    if data is None:
        return

    print("\nInventory Loaded\n")

    data = calculate_days_remaining(data)

    low_stock = find_low_stock(data)

    urgent = urgent_reorder(data)

    print("Products below reorder level:\n")

    for _, row in low_stock.iterrows():

        print(f"Product: {row['product']}")
        print(f"Current Stock: {row['current_stock']}")
        print(f"Reorder Level: {row['reorder_level']}")
        print()

    print("\nUrgent Reorders:\n")

    for _, row in urgent.iterrows():

        print(f"Product: {row['product']}")
        print(f"Days Remaining: {row['days_remaining']:.2f}")
        print()

        generate_invoice(
            row["product"],
            row["reorder_level"] * 2,
            row["supplier"],
            row["cost"]
        )


if __name__ == "__main__":
    run_inventory_analysis()