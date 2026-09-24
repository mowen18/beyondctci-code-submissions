# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def matrix_multiplication(A, B):
    if not A or not B: return []
    if len(A[0]) != len(B): return []

    rows_a, cols_a = len(A), len(A[0])
    rows_b, cols_b = len(B), len(B[0])

    result = [[0] * cols_b for _ in range(rows_a)]

    for r in range(rows_a):
        for c in range(cols_b):
            for k in range(cols_a):
                result[r][c] += A[r][k] * B[k][c]
    return result



