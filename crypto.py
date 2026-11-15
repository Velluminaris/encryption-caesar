# Приводим ключ к диапазону и определяем сдвиг
def normalize_key(key: int, alphabet_size: int) -> int:
    return key % alphabet_size

# Шифрование Цезаря
def encrypt(text: str, key: int, alphabet: str) -> str:
    
    # Сначала нормализуем ключ
    key = normalize_key(key, len(alphabet))
    
    # Если ключ 0, текст не меняется
    if key == 0:
        return text
    
    # Проходимся по каждой букве
    result = []
    for char in text:
        # Находим позицию буквы в алфавите
        position = alphabet.index(char)
        
        # Сдвигаем на key позиций вперёд (с зацикливанием)
        new_position = (position + key) % len(alphabet)
        
        # Берём новую букву
        result.append(alphabet[new_position])
    
    return ''.join(result)

# Дешифрование Цезаря
def decrypt(text: str, key: int, alphabet: str) -> str:

    # Если шифровали с ключом 5, то расшифровываем с ключом (32 - 5) = 27
    reverse_key = len(alphabet) - key
    
    # Используем функцию encrypt, но с обратным ключом
    return encrypt(text, reverse_key, alphabet)