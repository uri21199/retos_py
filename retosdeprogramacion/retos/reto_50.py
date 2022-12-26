#Crea una función que sea capaz de encriptar y desencriptar texto utilizando el algoritmo de encriptación de Karaca.

def encrypt(text):
    
    list_text = "".join(list(text[::-1]))
    final_text = []
    r_text = list_text.maketrans("aeiou", "01223")
    replaced_text = list_text.translate(r_text)
    
    list_text_replaced = replaced_text.split()
    for word in list_text_replaced:
        final_text.append(word + 'aca')
    final_text = " ".join(final_text)
    print(final_text)

def decrypt(text):

    lista_text = text.split()
    list_less_aca = [elem[:-3] for elem in lista_text]
    list_less_aca = " ".join(list_less_aca)

    r_text = list_less_aca.maketrans("01223", "aeiou")
    replaced_text = list_less_aca.translate(r_text)

    print(replaced_text[::-1])


if __name__ == "__main__":
    text = input("Introduzca un texto para encriptar")
    encrypt(text)
    decrypt(text)