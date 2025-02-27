import numpy as np

count = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    allAnsvers = [x for x in range(1, 101)]
    a = int(len(allAnsvers) / 2) - 1
    predict = allAnsvers[a]
    tempList = allAnsvers
    while number != predict:
        count += 1
        if predict > number:
            tempList = tempList[0: a]
            a = int(len(tempList) / 2) - 1
        elif predict < number:
            tempList = tempList[a:]
            a = int(len(tempList) / 2)
        predict = tempList[a]
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


# запускаем
score_game(game_core_v3)