# age = 40

# if age > 18:
#     print("fdsfsd")
#     print("dfdfd")


# score = 54

# if score >= 90:
#     print("bardzo dobry")
# elif score >=70:
#     print("dobry")
# elif score >=50:
#     print("zaliczone")
# else:
#     print("niezaliczone")

# age = 20
# sub = True
# blocked = False
# access = False

# if age > 18 and sub and not blocked:
#     access = True

# print("access: " + str(access))

def calc(price, ilos):
    print(price * ilos)

print(calc(100,10))
print(calc(200,14))

def get_category(score):
    if score >= 80:
        return "high"
    elif score >=50:
        return "medium"
    else:
        return "low"

