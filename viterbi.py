# Андреев Никита и Киличева Дилфуза

"""
Алгоритм Витерби

Пример работы:
Введите кол-во состояний: 2
Введите кол-во возможных событий: 3
Введите вероятности переходов из стартового состояния в другие состояния: 
Вероятность (start) -> (0): 0.8
Вероятность (start) -> (1): 0.2
Введите матрицу вероятностей переходов из состояния в состояние:
Вероятность (0) -> (0): 0.0
Вероятность (0) -> (1): 0.3
Вероятность (1) -> (0): 0.5
Вероятность (1) -> (1): 0.0
Введите вероятности переходов в конечное состояние:
Вероятность (0) -> (end): 0.7
Вероятность (1) -> (end): 0.5
Введите матрицу вероятностей возникновения событий, где строки - номера состояний, а столбцы - номера событий:
Вероятность O0 в состоянии 0: 0.5
Вероятность O1 в состоянии 0: 0.25
Вероятность O2 в состоянии 0: 0.25
Вероятность O0 в состоянии 1: 0.7
Вероятность O1 в состоянии 1: 0.15
Вероятность O2 в состоянии 1: 0.15
Введите длину цепи Маркова: 3
Введите индексы событий:
0
1
2
Наиболее вероятная последовательность состояний: [0, 1, 0]; Вероятность: 0.0015749999999999998

Чистые данные для проверки:
2
3
0.8
0.2
0.0
0.3
0.5
0.0
0.7
0.5
0.5
0.25
0.25
0.7
0.15
0.15
3
0
1
2

"""

states_count = int(input("Введите кол-во состояний: "))
available_actions_count = int(input("Введите кол-во возможных событий: "))

# Инициализация модели Маркова

start_transitions = []
print("Введите вероятности переходов из стартового состояния в другие состояния: ")
for i in range(states_count):
    start_transitions.append(float(input(f"Вероятность (start) -> ({i}): ")))

transitions_matrix = []

print("Введите матрицу вероятностей переходов из состояния в состояние:")
for i in range(states_count):
    row = []
    transitions_matrix.append(row)
    for j in range(states_count):
        row.append(float(input(f"Вероятность ({i}) -> ({j}): ")))

finish_transitions = []
print("Введите вероятности переходов в конечное состояние: ")
for i in range(states_count):
    finish_transitions.append(float(input(f"Вероятность ({i}) -> (end): ")))

# Ввод матрицы возникновения событий

print(
    "Введите матрицу вероятностей возникновения событий, где строки - номера состояний, а столбцы - номера событий: "
)

actions_probabilities_matrix = []
for i in range(states_count):
    row = []
    for j in range(available_actions_count):
        row.append(float(input(f"Вероятность O{j} в состоянии {i}: ")))
    actions_probabilities_matrix.append(row)

# Ввод событий
actions_count = int(input("Введите длину цепи Маркова: "))

actions_chain = []

print("Введите индексы событий: ")
for action in range(actions_count):
    actions_chain.append(int(input()))


# Инициализация
# Трелис [номер события; вероятность возникновения события в i-том состоянии]
trelis = []

start_vector = []
for state_index in range(states_count):
    start_vector.append(
        (
            start_transitions[state_index]
            * actions_probabilities_matrix[state_index][actions_chain[0]],
            -1,
        )
    )
trelis.append(start_vector)

# Вычисление следующих ячеек трелиса
for action_index in range(1, len(actions_chain)):
    current_vector = []

    for state_index in range(states_count):
        max_probability = (-1, -1)
        for last_state_index in range(states_count):
            current_probability = (
                trelis[action_index - 1][last_state_index][0]
                * transitions_matrix[last_state_index][state_index]
                * actions_probabilities_matrix[state_index][actions_chain[action_index]]
            )
            if current_probability > max_probability[0]:
                max_probability = (current_probability, last_state_index)

        current_vector.append(max_probability)

    trelis.append(current_vector)

# Выбираем максимальную вероятность с учётом перехода в конечное состояние

max_probability = (-1, -1)
for state_index in range(states_count):
    current_probability = trelis[-1][state_index][0] * finish_transitions[state_index]
    if max_probability[0] < current_probability:
        max_probability = (current_probability, state_index)

# Находим наиболее вероятную последоавтельность состояний

max_probability_chain = []
max_probability_chain.append(max_probability[1])
counter = 1
while trelis[-counter][max_probability_chain[-1]][1] != -1:
    max_probability_chain.append(trelis[-counter][max_probability_chain[-1]][1])
    counter += 1

max_probability_chain.reverse()
print(
    f"Наиболее вероятная последовательность состояний: {max_probability_chain}; Вероятность: {max_probability[0]}"
)
