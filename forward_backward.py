states_count = int(input("Введите кол-во состояний: "))
available_actions_count = int(input("Введите кол-во возможных событий: "))

# Инициализация базовой модели Маркова

start_transitions = []
for i in range(states_count):
    start_transitions.append(1.0 / states_count)

# Заполнение матрицы вероятности переходов

transitions_matrix = []

for i in range(states_count):
    row = []
    for j in range(states_count):
        row.append(1.0 / states_count)
    transitions_matrix.append(row)

# Заполнение матрицы возникновения событий

actions_probabilities_matrix = []
for i in range(states_count):
    row = []
    for j in range(available_actions_count):
        row.append(1.0 / available_actions_count)
    actions_probabilities_matrix.append(row)

actions_chain = []

# Ввод событий
actions_count = int(input("Введите длину цепи Маркова: "))

actions_chain = []

print("Введите индексы событий: ")
for action in range(actions_count):
    actions_chain.append(int(input()))

iterations_counter = 0

while True:
    # Прямой ход

    # Инициализация
    # Трелис [номер события; вероятность возникновения события в i-том состоянии]
    trelis = []

    start_vector = []
    for state_index in range(states_count):
        start_vector.append(
            start_transitions[state_index]
            * actions_probabilities_matrix[state_index][actions_chain[0]]
        )
    trelis.append(start_vector)

    # Вычисление следующих ячеек трелиса
    for action_index in range(1, len(actions_chain)):
        current_vector = []

        for state_index in range(states_count):
            sum = 0.0
            for last_state_index in range(states_count):
                sum += (
                    trelis[action_index - 1][last_state_index]
                    * transitions_matrix[last_state_index][state_index]
                    * actions_probabilities_matrix[state_index][
                        actions_chain[action_index]
                    ]
                )

            current_vector.append(sum)

        trelis.append(current_vector)

    probability = 0.0
    for current_probability in trelis:
        probability += current_probability

    print(f"Итерация {iterations_counter}: {probability}")
    if probability >= 0.5:
        break

    # Обратный ход

    back_trelis = [None] * actions_count
    back_trelis[actions_count - 1] = 1

    for t in range(actions_count - 2, -1, -1):
        current_vector = []
        for i in range(states_count):
            sum = 0.0
            for j in range(states_count):
                sum += (
                    back_trelis[t + 1]
                    * transitions_matrix[i][j]
                    * actions_probabilities_matrix[j][t]
                )
            current_vector.append(sum)
        b.append(current_vector)

    gamma = []
    for t in range(actions_count):
        sum = 0
        for j in range(states_count):
            sum += trelis[j] * back_trelis[j]

        for i in range(states_count):
            gamma[t] = trelis[t][i] * back_trelis[t][i] / sum

    eps = []
    for t in range(actions_count - 1)
        current_matrix = []
        sum = 0.0
        for i in range(states_count):
            for j in range(states_count):
                sum += trelis[t][i] * transitions_matrix[i][j] * back_trelis[t + 1][j] * actions_probabilities_matrix[j][actions_chain[t + 1]]
        
        for i in range(states_count):
            current_row = []
            for j in range(states_count):
                current_row.append(trelis[t][i] * transitions_matrix[i][j] * back_trelis[t + 1] * actions_probabilities_matrix[j][actions_chain[t + 1]])
            current_matrix.append(current_row)

        eps.append(current_matrix)

    #Считаем новые вероятности переходов из стартового состояния
    for i in range(states_count):
        start_transitions[i] = gamma[1][i]

    for i in range(states_count):
        for j in range(states_count):
            sum1 = 0.0
            sum2 = 0.0
            for t in range(actions_count - 1):
                sum1 += eps[t][i][j]
                sum2 += gamma[t][i]

            transitions_matrix[i][j] = sum1 / sum2
    for i in range(states_count):
        for k in range(available_actions_count):
            sum1 = 0.0
            sum2 = 0.0
            for t in range(actions_count):
                sum1 += gamma[t][i]
                sum2 += gamma[t][i]

            actions_probabilities_matrix[i][k] = sum1 / sum2
    iterations_counter += 1