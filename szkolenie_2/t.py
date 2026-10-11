# import this


test = {
    "Mon" : "poniedziałek",
    "test" : None,
    "Thu" : "czwartek",
    "Fri" : "piatek",
    "Fri" : "piatekkk"
}
test2 = {
    "test" : "Kinga"
}

test3 = {
    **test,
    **test2
}

print(test3.get("fdsfdsf"))