def concatenate(*args, **kwargs):
    con_text = ""

    for el in args:
        con_text += el


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
