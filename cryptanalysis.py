from crypto import decrypt


def calculate_frequencies(text: str, alphabet: str) -> dict:

    # Если текст пустой, возвращаем словарь с нулями, чтобы не делить на ноль
    if not text:
        return {char: 0.0 for char in alphabet}
        
    frequencies = {char: 0 for char in alphabet}
    total_chars = len(text)
    
    # Считаем, сколько раз встречается каждая буква
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
            
    # Превращаем количество в долю (делим на общее количество букв)
    for char in alphabet:
        frequencies[char] /= total_chars
        
    return frequencies


def calculate_score(observed_freq: dict, expected_freq: dict) -> float:

    score = 0.0
    for char in expected_freq:
        # Берем частоту из текста. Если буквы нет вообще, считаем её частоту как 0
        obs = observed_freq.get(char, 0.0)
        exp = expected_freq[char]
        
        # Считаем квадрат разности и добавляем к общей сумме
        score += (obs - exp) ** 2
        
    return score


def brute_force(text: str, alphabet: str, expected_freq: dict) -> tuple[int, str]:
   
    best_key = 0
    min_score = float('inf')  # Начинаем с бесконечно большого числа
    best_decrypted_text = ""
    
    # Перебираем все возможные ключи (от 0 до размера алфавита - 1)
    for key in range(len(alphabet)):
        # 1. Пробуем расшифровать текст с текущим ключом
        decrypted_text = decrypt(text, key, alphabet)
        
        # 2. Считаем частоты букв в этом варианте расшифровки
        observed_freq = calculate_frequencies(decrypted_text, alphabet)
        
        # 3. Считаем, насколько этот вариант отличается от эталона
        score = calculate_score(observed_freq, expected_freq)
        
        # 4. Если это лучший результат на данный момент — запоминаем его
        if score < min_score:
            min_score = score
            best_key = key
            best_decrypted_text = decrypted_text
            
    return best_key, best_decrypted_text