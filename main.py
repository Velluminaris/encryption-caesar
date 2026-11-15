from config import (
    RUSSIAN_ALPHABET,
    LATIN_ALPHABET,
    RUSSIAN_LETTER_FREQUENCIES,
    ENGLISH_LETTER_FREQUENCIES,
)
from utils import clean_text, group_text, detect_alphabet, get_valid_key
from crypto import encrypt, decrypt
from cryptanalysis import brute_force


def print_menu():
    """Выводит главное меню программы."""
    print("\n" + "="*40)
    print("       ШИФР ЦЕЗАРЯ")
    print("="*40)
    print("1. Зашифровать текст")
    print("2. Расшифровать текст")
    print("3. Взломать шифр (без ключа)")
    print("0. Выход")
    print("="*40)


def handle_encrypt():
    """Обработка шифрования текста."""
    print("\n--- ШИФРОВАНИЕ ---")
    
    # Получаем текст от пользователя
    text = input("Введите текст для шифрования: ")
    
    # Очищаем текст (убираем пробелы, знаки препинания, заменяем Ё на Е)
    cleaned_text = clean_text(text)
    
    # Проверяем, что текст не пустой после очистки
    if not cleaned_text:
        print("Ошибка: текст не содержит букв!")
        return
    
    # Определяем алфавит (русский или английский)
    alphabet = detect_alphabet(cleaned_text)
    lang = "русский" if alphabet == RUSSIAN_ALPHABET else "английский"
    print(f"Определён язык: {lang}")
    
    # Запрашиваем ключ
    key = get_valid_key("Введите ключ сдвига: ")
    
    # Шифруем текст
    encrypted = encrypt(cleaned_text, key, alphabet)
    
    # Выводим результат группами по 5 символов
    print("\nЗашифрованный текст:")
    print(group_text(encrypted))


def handle_decrypt():
    """Обработка расшифровки текста."""
    print("\n--- РАСШИФРОВКА ---")
    
    # Получаем зашифрованный текст
    text = input("Введите зашифрованный текст: ")
    
    # Очищаем текст
    cleaned_text = clean_text(text)
    
    if not cleaned_text:
        print("Ошибка: текст не содержит букв!")
        return
    
    # Определяем алфавит
    alphabet = detect_alphabet(cleaned_text)
    lang = "русский" if alphabet == RUSSIAN_ALPHABET else "английский"
    print(f"Определён язык: {lang}")
    
    # Запрашиваем ключ
    key = get_valid_key("Введите ключ сдвига: ")
    
    # Расшифровываем текст
    decrypted = decrypt(cleaned_text, key, alphabet)
    
    # Выводим результат
    print("\nРасшифрованный текст:")
    print(decrypted)


def handle_break():
    """Обработка взлома шифра (без ключа)."""
    print("\n--- ВЗЛОМ ШИФРА ---")
    
    # Получаем зашифрованный текст
    text = input("Введите зашифрованный текст: ")
    
    # Очищаем текст
    cleaned_text = clean_text(text)
    
    if not cleaned_text:
        print("Ошибка: текст не содержит букв!")
        return
    
    # Определяем алфавит
    alphabet = detect_alphabet(cleaned_text)
    
    # Выбираем соответствующие частоты букв
    if alphabet == RUSSIAN_ALPHABET:
        expected_freq = RUSSIAN_LETTER_FREQUENCIES
        lang = "русский"
    else:
        expected_freq = ENGLISH_LETTER_FREQUENCIES
        lang = "английский"
    
    print(f"Определён язык: {lang}")
    print("Анализирую текст... (это может занять несколько секунд)")
    
    # Взламываем шифр
    found_key, decrypted_text = brute_force(cleaned_text, alphabet, expected_freq)
    
    # Выводим результаты
    print(f"\nНайденный ключ: {found_key}")
    print("Расшифрованный текст:")
    print(decrypted_text)


def main():
    """Главная функция программы."""
    print("Добро пожаловать в программу шифрования Цезаря!")
    
    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            handle_encrypt()
        elif choice == "2":
            handle_decrypt()
        elif choice == "3":
            handle_break()
        elif choice == "0":
            print("\nДо свидания!")
            break
        else:
            print("\nОшибка: неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()