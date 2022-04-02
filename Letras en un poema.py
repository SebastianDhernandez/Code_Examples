# Programa que cuenta las vocales y las consonantes de un poema

print("Enter the number of lines of the poem")  # Esta vez decidi escribir el codigo en ingles para variar
lines = int(input())
poem= ""
vowels = 0
consonants = 0

for i in range(lines):
    print("Please enter poem line number #", i+1)
    line_aux = str(input())
    poem = poem + "\n" + line_aux

print(poem, "\n")
poem = poem.lower()
a = int(poem.count("a"))
e = int(poem.count("e"))
i = int(poem.count("i"))
o = int(poem.count("o"))
u = int(poem.count("u"))

vowels = a + e + i + o + u

listOfConsonants = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "z", "w"]

for i in listOfConsonants:
    consonants += poem.count(i)

print("Number of vowels = ", vowels)
print("Number of consonants = ", consonants)