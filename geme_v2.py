"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        
    Returns:
        int: Число попыток
    """
    count = 0
    lower_border = 1  # задаем нижнюю границу чисел
    upper_border = 101 # задаем верхнюю границу чисел
    predict_number = np.random.randint(1,101)
    
    while number != predict_number:
        count += 1
    
        if number > predict_number:
            lower_border = predict_number # нижний диапазон
        
        elif number < predict_number:     
            upper_border = predict_number # верхний диапазон
        
        predict_number = (lower_border+upper_border)//2

        
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм
    
    Args:
        random_predict ([type]): функция угадывания
        
    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # фиксируем сид для воспроизводимости кода
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(10000)) # загадываем список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    
    
    