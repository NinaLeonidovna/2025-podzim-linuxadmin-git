# task_38_matrix_transpose.py

def matrix_transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Vrátí transponovanou matici.
    """
    if matrix == []:
        return []
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix
