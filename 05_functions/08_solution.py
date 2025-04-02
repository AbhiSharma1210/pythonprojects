def id_card(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

id_card(name = "Some name", age = 20, address = "220 Some house", phone = "1234")