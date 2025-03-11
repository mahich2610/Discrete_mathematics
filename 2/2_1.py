def analyze_graph(edges_list, num_vertices):
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for start, end in edges_list:
        adjacency_matrix[start - 1][end - 1] = 1
    is_reflexive = True
    for i in range(num_vertices):
        if adjacency_matrix[i][i] == 0:
            is_reflexive = False
            break
    is_symmetric = True
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adjacency_matrix[i][j] == 1 and adjacency_matrix[j][i] == 0:
                is_symmetric = False
                break
    is_transitive = True
    for i in range(num_vertices):
        for j in range(num_vertices):
            for k in range(num_vertices):
                if adjacency_matrix[i][j] == 1 and adjacency_matrix[j][k] == 1 and adjacency_matrix[i][k] == 0:
                    is_transitive = False
                    break
    return is_reflexive, is_symmetric, is_transitive
print("Введите количество рёбер и вершин:")
edges_count, vertices_count = map(int, input().split())
edges = []
print("Введите рёбра (откуда и куда идёт связь):")
for _ in range(edges_count):
    from_vertex, to_vertex = map(int, input().split())
    edges.append((from_vertex, to_vertex))
reflexive, symmetric, transitive = analyze_graph(edges, vertices_count)
print("Граф рефлексивный" if reflexive else "Граф не рефлексивный")
print("Граф симметричный" if symmetric else "Граф антисимметричный")
print("Граф транзитивный" if transitive else "Граф не транзитивный")
