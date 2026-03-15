# Inventory Decision Algorithm

## Step 1: Load Inventory Data

The system reads inventory data from a CSV or PDF report.

Each record includes:

- Product name
- Current stock
- Reorder level
- Daily sales rate
- Supplier information
- Product cost
- Supplier delivery time

---

## Step 2: Identify Low Stock Products

For each product:

Stock Gap = Reorder Level - Current Stock

If the stock gap is greater than zero, the product is considered **low in stock**.

---

## Step 3: Estimate Remaining Days of Inventory

Remaining Days = Current Stock / Daily Sales Rate

This estimates how long the current inventory will last.

---

## Step 4: Determine Reorder Urgency

If:

Remaining Days < Supplier Delivery Time

Then the product is marked as **urgent reorder**.

---

## Step 5: Supplier Evaluation

Suppliers are compared based on:

- Product cost
- Delivery speed

The system recommends the **optimal supplier**.

---

## Step 6: Generate Reorder Recommendation

The AI agent generates insights such as:

- Products requiring reorder
- Suggested reorder quantities
- Recommended suppliers

---

## Step 7: Generate Reorder Invoice

If a reorder is recommended, the system automatically generates a **reorder invoice** containing:

- Supplier name
- Product details
- Order quantity
- Estimated delivery time
- Total cost
