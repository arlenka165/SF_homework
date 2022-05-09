import numpy as np

def random_predict(number: int = 1, step = 10) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    '''Последовательно увеличиваем predict на значение step=10. Если
    значение predict становится больше загаданного number, то уменьшаем
    predict на единицу, пока predict не станет равен number. Функция
    принимает загаданное число и шаг, а возвращает число попыток'''
    
    count = 0 #счетчик попыток 
    predict = 0 #предполагаемое число
    while number != predict:
        count+=1
        if number > predict:
            predict+=step
        else:
            predict-=1
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

        score = int(np.mean(count_ls))
        print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
        return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
