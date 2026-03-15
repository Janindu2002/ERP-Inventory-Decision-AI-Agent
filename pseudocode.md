# Pseudocode

START

Load inventory dataset

FOR each product in inventory

    IF current_stock < reorder_level
        mark product as LOW_STOCK

    calculate daily sales rate

    calculate remaining_days = current_stock / daily_sales_rate

    IF remaining_days < supplier_delivery_time
        mark product as URGENT_REORDER

END FOR

FOR each low_stock product

    select best supplier based on:
        lowest cost
        fastest delivery

    generate reorder recommendation

    generate reorder invoice

END FOR

Display AI insights to the user

END
