import numpy as np

# Матриця виручки
F = np.array([
    [6.0, 6.2, 5.5],
    [7.5, 7.1, 7.0],
    [7.4, 7.5, 8.0],
    [8.5, 8.7, 8.0]
])

# Ймовірності станів економічного середовища
P = np.array([0.3, 0.5, 0.2])

# Крок 1: Обчислення очікуваного значення для кожного варіанту
expected_values = F @ P

# Крок 2: Обчислення семіваріації (варіація з негативними відхиленнями)
# Вважаємо, що середнє значення — це еталон.
semivariance = np.sum(P * np.maximum(0, expected_values[:, np.newaxis] - F) ** 2, axis=1)

# Крок 3: Обчислення модифікованого коефіцієнта семіваріації (звичайна варіація)
variance = np.sum(P * (F - expected_values[:, np.newaxis]) ** 2, axis=1)

# Крок 4: Модифікований коефіцієнт семіваріації з модальним значенням та коефіцієнтом λ = 0.7
lambda_1 = 0.7
modal_value = np.median(F, axis=1)  # Використовуємо медіану як модальне значення
modified_criterion = lambda_1 * modal_value + (1 - lambda_1) * np.sqrt(variance)

# Крок 5: Критерій Ходжеса—Лемана з λ = 0.9
lambda_2 = 0.9
hodges_lehmann = lambda_2 * expected_values + (1 - lambda_2) * np.sqrt(variance)

# Виведення результатів
print("Очікувані значення для кожного варіанту:", expected_values)
print("Семіваріація для кожного варіанту:", semivariance)
print("Модифікований коефіцієнт семіваріації (звичайна варіація):", variance)
print("Модифікований коефіцієнт семіваріації з λ=0.7:", modified_criterion)
print("Критерій Ходжеса—Лемана з λ=0.9:", hodges_lehmann)

# Вибір найкращих варіантів для кожного критерію
best_semivariance_index = np.argmin(semivariance) + 1
best_modified_index = np.argmin(variance) + 1
best_modified_criterion_index = np.argmin(modified_criterion) + 1
best_hodges_lehmann_index = np.argmin(hodges_lehmann) + 1

print("Найкращий варіант за мінімальною семіваріацією:", best_semivariance_index)
print("Найкращий варіант за мінімальною модифікованою варіацією:", best_modified_index)
print("Найкращий варіант за модифікованим коефіцієнтом з λ=0.7:", best_modified_criterion_index)
print("Найкращий варіант за критерієм Ходжеса-Лемана з λ=0.9:", best_hodges_lehmann_index)
