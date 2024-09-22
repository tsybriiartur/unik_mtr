from math import sqrt

# Коєфіцієнти варіантів
variants = {
    "first": [[0.6, 8], [0.4, -0.5]],
    "second": [[0.7, 12], [0.3, -0.5]],
    "create": [[0.3, 25], [0.7, -1]]
}

# Функції для обчислень
def find_M(variant):
    """Обчислює сподівану чисту теперішню вартість (M)"""
    return variants[variant][0][0] * variants[variant][0][1] + variants[variant][1][0] * variants[variant][1][1]

def find_V(variant, M):
    """Обчислює дисперсію (V)"""
    return (variants[variant][0][1] - M)**2 * variants[variant][0][0] + (variants[variant][1][1] - M)**2 * variants[variant][1][0]

def find_om(V):
    """Обчислює середньоквадратичне відхилення (ω)"""
    return sqrt(V)

def find_CV(om, M):
    """Обчислює коефіцієнт варіації (CV)"""
    return om / M

def find_SSV(variant, M):
    """Обчислює семіквадратичне відхилення (SSV)"""
    return sqrt(variants[variant][1][0] * (variants[variant][1][1] - M) ** 2)

def find_CSV(ssv, M):
    """Обчислює коефіцієнт семіваріації (CSV)"""
    return ssv / M

def find_p(variant):
    """Обчислює ймовірність небажаної події (p)"""
    return variants[variant][1][0]

def find_Z(variant):
    """Обчислює сподівані збитки (Z)"""
    return variants[variant][1][0] * variants[variant][1][1]

# Виведення результатів для кожного показника
def print_results(label, values, corp_names):
    """Допоміжна функція для виведення результатів"""
    print(f"{label}:")
    for i in range(len(corp_names)):
        print(f"{corp_names[i]}: {values[i]}")
    print(f"Найбільше значення: {corp_names[values.index(max(values))]} - {max(values)}")
    print(f"Найменше значення: {corp_names[values.index(min(values))]} - {min(values)}")
    print()

# Основна функція
def main():
    corp_names = ['Перша корпорація', 'Друга корпорація', 'Створити асоціацію']
    
    # Сподівана чиста теперішня вартість (M)
    m = [find_M("first"), find_M("second"), find_M("create")]
    print_results("Сподівана чиста теперішня вартість", m, corp_names)
    
    # Дисперсія (V)
    v = [find_V("first", m[0]), find_V("second", m[1]), find_V("create", m[2])]
    print_results("Дисперсія", v, corp_names)
    
    # Середньоквадратичне відхилення (ω)
    om = [find_om(v[0]), find_om(v[1]), find_om(v[2])]
    print_results("Середньоквадратичне відхилення", om, corp_names)
    
    # Коефіцієнт варіації (CV)
    cv = [find_CV(om[0], m[0]), find_CV(om[1], m[1]), find_CV(om[2], m[2])]
    print_results("Коефіцієнт варіації", cv, corp_names)
    
    # Семіквадратичне відхилення (SSV)
    ssv = [find_SSV('first', m[0]), find_SSV('second', m[1]), find_SSV('create', m[2])]
    print_results("Семіквадратичне відхилення", ssv, corp_names)
    
    # Коефіцієнт семіваріації (CSV)
    csv = [find_CSV(ssv[0], m[0]), find_CSV(ssv[1], m[1]), find_CSV(ssv[2], m[2])]
    print_results("Коефіцієнт семіваріації", csv, corp_names)
    
    # Ймовірність небажаної події (p)
    p = [find_p('first'), find_p('second'), find_p('create')]
    print_results("Ймовірність небажаної події", p, corp_names)
    
    # Сподівані збитки (Z)
    z = [find_Z('first'), find_Z('second'), find_Z('create')]
    print_results("Сподівані збитки", z, corp_names)

# Виклик основної функції
main()
