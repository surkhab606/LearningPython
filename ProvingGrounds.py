def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")


shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St", apt="100", city="Detroit", state="MI")
