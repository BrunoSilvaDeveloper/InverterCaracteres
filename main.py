def inverter_string(string):
    string_invertida = ""

    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida

if __name__ == "__main__":
    string_original = input("Digite uma string para inverter: ")
    string_invertida = inverter_string(string_original)
    print("A string invertida é:", string_invertida)