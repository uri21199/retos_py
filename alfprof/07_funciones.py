### Funciones --> Link: https://aprendeconalf.es/docencia/python/ejercicios/funciones/7

#11
print("\1")

def saludo():
    print("Hola")

saludo()

#2
print("\n2")

def saludo2(nombre):
    print(f"Hola {nombre}")

saludo2("Hola")

#3
print("\n3)")

def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i + 1
    return tmp

print(factorial(2))

#4
print("\n4")

def factura(cantidad, iva = .21):
    factura_total = cantidad + cantidad * iva
    print(factura_total)

factura(100)
factura(100, .33)

#5
print("\n5")

def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    return area

print(area_of_circle(10))

def area_of_cilinder(r, h):
    return area_of_circle(r) * h

print(area_of_cilinder(10, 10))

#6
print("\n6")

def mean(sample):
    return sum(sample) / len(sample)

print(mean([1,2,3,4,5]))

#7
print("\n7")
def square(sample):
    list = []
    for i in sample:
        list.append(i**2)
    return list

print(square([1, 2, 3, 4, 5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

#8
print("\n8")

def statistics(sample):
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum((sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))

#8
print("\n9")

def mcd(n, m):
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))

#10
print("\n10")

def to_decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))

#11
print("\n11")

def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))