## Лабораторная работа 1, Вариант 4


def Function(n):

    ## Пустой список для вывода результата и список натуральных чисел нужной нам длины
    Result = []
    Numbers = list(range(1, n + 1))

    ## Генератор. Принимает список текущих и оставшихся значений
    def Generate(CurrentList, Remaining):

        ## Если список оставшихся значений пуст - добавляет получившийся список в результат
        if len(Remaining) == 0:
            Result.append(CurrentList)
            return
        
        for i in range(len(Remaining)):

            ## Выбираем число из списка оставшихся чисел под индексом i
            Chosen = Remaining[i]

            ## Создаем новый список, исключая число, которое уже использовано
            NewRemaining = Remaining[:i] + Remaining[i+1:]

            ## Функция запускается заново, но уже с нужным числом в первом списке
            Generate(CurrentList + [Chosen], NewRemaining)

    Generate([], Numbers)

    ## Вывод результатов (число всех последовательностей и сами последовательности через пробел)
    print(len(Result))
    for p in Result:
        print(*p)


## Тест
Function(3)
