"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
from time import sleep


def random_predict(number: int = 1) -> int:
    """Угадываем число
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        
    Returns:
        int: Число попыток
    """
    count = 0
    lower_borber = 1
    upper_borber = 101
    predict_number = np.random.randint(1,101)

    while number != predict_number:
        count += 1
    
        if number > predict_number:
            lower_borber = predict_number
        
        elif number < predict_number:
            upper_borber = predict_number
        
        predict_number = (lower_borber+upper_borber)//2

        
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм
    
    Args:
        random_predict ([type]): функция угадывания
        
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    
    
    