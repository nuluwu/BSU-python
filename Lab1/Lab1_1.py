def InvincibleRabbits(n, k):
    
    ## Одна пара в первый и второй месяц
    m1, m2 = 1, 1

    ## Определяем количество кроликов для указанного пользователем числа месяцев
    for i in range(3, n + 1):
        m1, m2 = m2, m2 + k * m1

    return m2


## Test 1
print(InvincibleRabbits(5, 3))

## Test 2
print(InvincibleRabbits(6, 3))

## Test 3
print(InvincibleRabbits(5, 5))

## Test 4
print(InvincibleRabbits(12, 1))

## Test 5
print(InvincibleRabbits(100, 3))

## Test 6
print(InvincibleRabbits(20, 2))

## Test 7
print(InvincibleRabbits(33, 2))
