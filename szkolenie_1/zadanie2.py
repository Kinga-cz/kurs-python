# -----------------------------------------------------------------------------
# ZADANIE 5 – FUNKCJA + IF
# -----------------------------------------------------------------------------
#
# Napisz funkcję:
#
# get_score_category(score)
#
#
# Funkcja powinna zwracać:
#
# "high"
# jeśli score >= 70
#
#
# "medium"
# jeśli score >= 40
#
#
# "low"
# w pozostałych przypadkach.
#
#
# Sprawdź funkcję dla:
#
# 95
# 65
# 30



# Napisz kod tutaj:


def get_score_category(score):
    if score > 70:
        print("high")
    if score > 40:
        print("medium")
    else:
        print("low")

get_score_category(95)
get_score_category(65)
get_score_category(30)



# -----------------------------------------------------------------------------
# ZADANIE 6 – RABAT
# -----------------------------------------------------------------------------
#
# Napisz funkcję:
#
# calculate_final_price(price, customer_type)
#
#
# customer_type == "premium"
# -> rabat 20%
#
#
# customer_type == "standard"
# -> rabat 10%
#
#
# pozostałe wartości:
# -> brak rabatu
#
#
# Funkcja powinna ZWRACAĆ cenę po rabacie.
#
#
# Przykład:
#
# calculate_final_price(100, "premium")
#
# powinno zwrócić:
#
# 80.0

CUSTOMER_PREMIUM = "premium"
CUSTOMER_STANDARD = "standard"


def calculate_final_price(price, customer_type):
    if customer_type == CUSTOMER_PREMIUM:
        return price - price * 0.20
    elif customer_type == CUSTOMER_STANDARD:
        return price - price * 0.10
    else:
        return price

print(calculate_final_price(100, "premium"))
# Napisz kod tutaj: