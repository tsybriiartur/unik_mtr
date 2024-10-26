import numpy as np
from scipy.optimize import minimize

# Дані
m = np.array([0.20, 0.40, 0.60])  # Сподівані норми прибутку
sigma = np.array([0.10, 0.18, 0.30])  # Середньоквадратичні відхилення
rho = np.array([[1, 1, -1],  # Кореляційна матриця
                [1, 1, -1],
                [-1, -1, 1]])

# Коваріаційна матриця
cov_matrix = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        cov_matrix[i, j] = sigma[i] * sigma[j] * rho[i, j]

# Функція для обчислення ризику портфеля
def portfolio_risk(x, cov_matrix):
    return np.sqrt(np.dot(x.T, np.dot(cov_matrix, x)))

# Умова рівності суми ваг до 1
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# Обмеження для ваг (ваги повинні бути в межах від 0 до 1)
bounds = tuple((0, 1) for _ in range(3))

# Початкові припущення для ваг
x0 = np.array([1/3, 1/3, 1/3])

# Максимізація сподіваної норми прибутку
def negative_expected_return(x, m):
    return -np.dot(x, m)

# Мінімізація ризику для портфелів з максимальним очікуваним прибутком
result_max_return = minimize(negative_expected_return, x0, args=(m,), method='SLSQP', bounds=bounds, constraints=constraints)

# Оптимальні ваги для максимального прибутку
optimal_weights_max_return = result_max_return.x

# Обчислення сподіваної норми прибутку для максимального прибутку
m_p_max_return = np.dot(optimal_weights_max_return, m)

# Обчислення ризику для максимального прибутку
sigma_p_max_return = portfolio_risk(optimal_weights_max_return, cov_matrix)

# Результати
print(optimal_weights_max_return, m_p_max_return, sigma_p_max_return)
