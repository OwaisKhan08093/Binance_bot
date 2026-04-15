def validate_order(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET , LIMIT or STOP")

    if float(quantity) <= 0:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT":
        if price is None or float(price) <= 0:
            raise ValueError("LIMIT orders need price")
