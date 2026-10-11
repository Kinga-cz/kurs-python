# -----------------------------------------------------------------------------
# ZADANIE 1 – LICZBA DODATNIA, UJEMNA CZY ZERO
# -----------------------------------------------------------------------------
#
# Dana jest liczba:
#
# number = -10
#
# Napisz instrukcję if / elif / else.
#
# Program powinien wyświetlić:
#
# "Liczba jest dodatnia"
#
# jeśli number > 0
#
#
# "Liczba jest równa zero"
#
# jeśli number == 0
#
#
# "Liczba jest ujemna"
#
# w pozostałych przypadkach.



number = -10


# Napisz kod tutaj:

def chek_number(number):
    if number > 0:
        print("liczba dodatnia")
    elif number == 0:
        print("liczba równa zeru")
    else:
        print("liczba ujemna")

chek_number(number)


# -----------------------------------------------------------------------------
# ZADANIE 2 – DARMOWA DOSTAWA
# -----------------------------------------------------------------------------
#
# Klient otrzymuje darmową dostawę, jeżeli:
#
# wartość zamówienia wynosi co najmniej 200 PLN
#
# LUB
#
# klient jest klientem premium.
#
#
# Jeśli warunek jest spełniony:
#
# "Darmowa dostawa"
#
#
# W przeciwnym przypadku:
#
# "Koszt dostawy: 15 PLN"



order_value = 150
is_premium = True

# Napisz kod tutaj:

def freeDelivery(order, ispremium):
    if order > 200 and is_premium:
        print("darmowa dostawa")
    else:
        print("koszt dostawy: 15 pln")

freeDelivery(order_value, is_premium)