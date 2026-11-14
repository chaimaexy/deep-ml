def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    lines = len(a)
    columns = len(a[0])
    result = []
    
    for j in range(0,columns,1):
        d = []
        for i in range(0,lines,1):
            d.append(a[i][j])
        result.append(d)

    return result
    
