# Edge Cases

The system must handle the following scenarios.

---

## Missing Data

Some inventory reports may contain missing values.

Example:

- Missing reorder level
- Missing supplier information

Solution:
Validate input data before analysis.

---

## Negative Stock Values

A system error may produce negative inventory numbers.

Solution:
Flag invalid values and notify the user.

---

## Zero Sales Rate

If daily sales rate is zero:

Remaining Days = Infinite

Solution:
Mark the product as **low demand**.

---

## Multiple Suppliers

Some products may have several suppliers.

Solution:
Compare suppliers using cost and delivery time.

---

## Sudden Demand Spike

Sales may increase unexpectedly.

Solution:
Use moving average sales rate instead of a single day value.

---

## Duplicate Product Records

Inventory reports may contain duplicated product entries.

Solution:
Aggregate duplicate entries before analysis.

---

## Extremely Large Inventory Files

Large ERP exports may contain thousands of records.

Solution:
Use efficient data processing libraries such as **Pandas**.
