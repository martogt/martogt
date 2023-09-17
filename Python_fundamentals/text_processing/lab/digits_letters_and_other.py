symbols = input()

digits = ""
letters = ""
others = ""

for sym in symbols:
    if sym.isalnum():
        if sym.isdigit():
            digits += sym
        if sym.isalpha():
            letters += sym
    else:
        others += sym

print(f"{digits}\n{letters}\n{others}")
