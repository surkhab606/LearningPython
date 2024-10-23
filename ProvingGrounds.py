def camaro(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print(camaro(Z28 = "5.7L", RallySport = "5.0L", Berlinetta = "5.0L", TypeLT = "4.6L"))