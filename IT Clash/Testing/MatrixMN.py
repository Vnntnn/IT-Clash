"""Matrix M*N"""

def multiply_matrix(p: int, q: int, r: int, mA: list[int], mB: list[int]) -> list[str]:
    """Matrix M*N function"""
    result = [[0 for _ in range(r)] for _ in range(p)]
    
    for i in range(p):
        for j in range(r):
            for k in range(q):
                result[i][j] += mA[i][k] * mB[k][j]

    return [list(map(str, row)) for row in result]

def main():
    """Main function"""
    # Input dimensions
    p, q, r = int(input()), int(input()), int(input())
    
    # Input Matrix A
    mA = [[int(input()) for _ in range(q)] for _ in range(p)]
    
    # Input Matrix B
    mB = [[int(input()) for _ in range(r)] for _ in range(q)]
    
    result = multiply_matrix(p, q, r, mA, mB)
    
    for row in result:
        print(" ".join(row))

main()
