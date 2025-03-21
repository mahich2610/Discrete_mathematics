def sort_combinations(combinations):
    filtered_combinations = [combo for combo in combinations if combo != '1']
    sorted_combinations = sorted(filtered_combinations, key=lambda x: (len(x), x))
    if '1' in combinations:
        sorted_combinations.insert(0, '1')
    return sorted_combinations
def binary_to_combinations(binary_array):
    num_variables = len(binary_array[0]) - 1
    letters = [chr(97 + i) for i in range(num_variables)]
    result = []
    for row in binary_array:
        combination = ''
        for i in range(num_variables):
            if row[i] == 1:
                combination += letters[i]
        result.append(combination if combination else '1')
    return result
def zhegalkin_polynomial(truth_table):
    values = [row[-1] for row in truth_table]
    coefficients = []
    while values:
        coefficients.append(values[0])
        values = [values[i] ^ values[i + 1] for i in range(len(values) - 1)]
    letters = binary_to_combinations(truth_table)
    result_terms = [letters[i] for i, coefficient in enumerate(coefficients) if
                    coefficient == 1]
    return '1' if result_terms == ['1'] else '+'.join(sort_combinations(result_terms))
n = int(input('Введите количество переменных: '))
print(f'Введите таблицу истинности (по {n + 1} чисел в строке, 0 или 1):')
truth_table = []
for _ in range(2 ** n):
    row = list(map(int, input().split()))
    truth_table.append(row)
result = zhegalkin_polynomial(truth_table)
print('Полином Жегалкина:', result)