models = {"CLE53": "AMG",
          "CLE63": "AMG",
          "CLE300": "Base",
          "CLE450": "AMG-line"}

models.update({"CLE63S": "AMG Performance"})
models.pop("CLE63S")

for key, value in models.items():
    print(f"{key}:{value}")

