def find_low_stock(data):
    """
    Identify products below reorder level
    """

    low_stock = data[data["current_stock"] < data["reorder_level"]]
    return low_stock


def calculate_days_remaining(data):
    """
    Calculate how long stock will last
    """

    data["days_remaining"] = data["current_stock"] / data["daily_sales"]

    return data


def urgent_reorder(data):
    """
    Identify urgent reorder items
    """

    urgent = data[data["days_remaining"] < data["delivery_days"]]

    return urgent