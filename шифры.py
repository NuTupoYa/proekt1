def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def binary_code(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def rot1(text):
    return caesar_cipher(text, 1)

def main():
    print("Выберите метод шифрования:")
    print("1. Шифр Цезаря")
    print("2. Двоичный код")
    print("3. ROT1")

    choice = input("Введите номер метода (1-3): ")

    if choice in ['1', '2', '3']:
        action = input("Вы хотите зашифровать (e) или дешифровать (d)? ").lower()
        text = input("Введите текст: ")

        if choice == '1':
            if action == 'e':
                shift = int(input("Введите сдвиг (целое число): "))
                result = caesar_cipher(text, shift)
                print(f"Зашифрованный текст: {result}")
            elif action == 'd':
                shift = int(input("Введите сдвиг (целое число): "))
                result = caesar_cipher(text, -shift)
                print(f"Дешифрованный текст: {result}")

        elif choice == '2':
            if action == 'e':
                result = binary_code(text)
                print(f"Двоичный код: {result}")
            elif action == 'd':
                print("Дешифровка двоичного кода не поддерживается в данной версии.")

        elif choice == '3':
            if action == 'e':
                result = rot1(text)
                print(f"Зашифрованный текст (ROT1): {result}")
            elif action == 'd':
                result = rot1(text)  # ROT1 является симметричным
                print(f"Дешифрованный текст (ROT1): {result}")
    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()
    
phrase = input()
print(phrase)