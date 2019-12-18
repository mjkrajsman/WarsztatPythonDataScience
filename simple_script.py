# Napisać `skrypt` który zliczy ilość wystąpień parametrów z linii komend

# PS C:\work\conda\WarsztatPythonDataScience> python .\simple_script.py asdf asdf as as as
# {'asdf': 2, 'as': 3}

import sys

def zad1(txt):
    keys = list(set(txt))
    if __file__ in keys:
        keys.remove(__file__)
    values = [ txt.count(i) for i in keys]
    return dict(zip(keys,values))


# Napisać `skrypt` który zliczy ilość wystąpień znaków w parametrach z linii komend

# PS C:\work\conda\WarsztatPythonDataScience> python .\simple_script.py asdf asdf as as as
# {'a': 5, 's': 5, 'd': 2, 'f': 2, ' ': 4}

def zad2(txt):
    if __file__ in txt:
        txt.remove(__file__)
    chars = " ".join(txt)
    res = zad1(chars)
    return res

print("Zad1:")
print(zad1(sys.argv)) # sys.argv[1:]
print("Zad2:")
print(zad2(sys.argv)) # sys.argv[1:]

