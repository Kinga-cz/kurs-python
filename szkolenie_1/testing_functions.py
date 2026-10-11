def print_name(name):
    print(name)

def return_name(name):
    return name
CUSTOMER_PREMIUM = "premium"
CUSTOMER_STANDARD = "standard"


def calculate_final_price(price, customer_type):
    if customer_type == CUSTOMER_PREMIUM:
        return price - price * 0.20
    elif customer_type == CUSTOMER_STANDARD:
        return price - price * 0.10
    else:
        return price