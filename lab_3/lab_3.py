import math

# Гроші, які є у кожного студента
money = 50

# Ймовірність програшу/виграшу
p_loss = 0.5
p_win = 0.5

# Виграш у співвідношенні 1:3
win_multiplier = 3

# Функція корисності для першого студента (лінійна)
def utility_1(x):
    return 1.3 * x

# Функція корисності для другого студента (корінь квадратний)
def utility_2(x):
    return 1.4 * math.sqrt(x)

# Сподівана корисність для варіанту з ризиком (ставка)
def expected_utility_risk(utility_func, money, p_win, p_loss, win_multiplier):
    u_loss = utility_func(0)  # Корисність при програші
    u_win = utility_func(money * win_multiplier)  # Корисність при виграші

    # Сподівана корисність
    expected_utility = p_loss * u_loss + p_win * u_win
    return expected_utility

# Основна функція для порівняння рішень студентів
def main():
    # Корисність для першого студента
    no_risk_utility_1 = utility_1(money)  # Якщо не ризикує і залишає 50 грн
    risk_utility_1 = expected_utility_risk(utility_1, money, p_win, p_loss, win_multiplier)  # Якщо робить ставку

    print(f"Корисність для першого студента без ризику: {no_risk_utility_1:.2f}")
    print(f"Сподівана корисність для першого студента з ризиком: {risk_utility_1:.2f}")

    # Корисність для другого студента
    no_risk_utility_2 = utility_2(money)  # Якщо не ризикує і залишає 50 грн
    risk_utility_2 = expected_utility_risk(utility_2, money, p_win, p_loss, win_multiplier)  # Якщо робить ставку

    print(f"Корисність для другого студента без ризику: {no_risk_utility_2:.2f}")
    print(f"Сподівана корисність для другого студента з ризиком: {risk_utility_2:.2f}")

    # Рішення першого студента
    if risk_utility_1 > no_risk_utility_1:
        print("Перший студент обере зробити ставку.")
    else:
        print("Перший студент обере не ризикувати.")

    # Рішення другого студента
    if risk_utility_2 > no_risk_utility_2:
        print("Другий студент обере зробити ставку.")
    else:
        print("Другий студент обере не ризикувати.")

main()
