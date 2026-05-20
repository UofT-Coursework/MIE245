import numpy as np
from typing import List

# ASSUME ALL MATRICES ARE n x n, s.t. n = 2^x

def strassen_matmul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Compute C = A @ B using Strassen's algorithm.

    Inputs:
        A (np.ndarray): n x n matrix
        B (np.ndarray): n x n matrix

    Output:
        C (np.ndarray): n x n matrix product of A and B
    """
    n = A.shape[0]
    C = np.zeros((n, n))
    
    # Justin Case 
    if n == 1:
        C = A * B
        return C

    # Partition A / B into quadrants
    A_parts = partition_matrix(A)  # [A11, A12, A21, A22]
    B_parts = partition_matrix(B)  # [B11, B12, B21, B22]

    # Compute 10 Strassen sum matrices
    S = calculate_sum_matrices(A_parts, B_parts) # S1..S10

    # Compute 7 Strassen product matrices 
    P = calculate_product_matrices(A_parts, B_parts, S) # P1..P7

    # Compute C quadrants from product matrices
    C_parts = calculate_C_partitions(P) # [C11, C12, C21, C22]

    # Combine C quadrants
    C = combine_C_partitions(C, C_parts)

    return C

def partition_matrix(M: np.ndarray) -> List[np.ndarray]:
    """
    Partition a square matrix into four quadrants.

    Input:
        M (np.ndarray): n x n matrix

    Output:
        List[np.ndarray]: [M11, M12, M21, M22],
                          each of size (n/2) x (n/2)
    """
    half = int(M.shape[0] / 2)
    M11 = M[:half, :half]     # top left
    M12 = M[:half, half:]    # top right
    M21 = M[half:, :half]  # bottom left
    M22 = M[half:, half:] # bottom right
    return [M11, M12, M21, M22]

def calculate_sum_matrices(
        A_parts: List[np.ndarray],
        B_parts: List[np.ndarray]
    ) -> List[np.ndarray]:
    """
    Compute the 10 Strassen sum matrices S1..S10.

    Inputs:
        A_parts (List[np.ndarray]): [A11, A12, A21, A22]
        B_parts (List[np.ndarray]): [B11, B12, B21, B22]

    Output:
        List[np.ndarray]: [S1, S2, ..., S10],
                          each of size (n/2) x (n/2)
    """
    S1 = B_parts[1] - B_parts[3]   # S1 = B12 - B22
    S2 = A_parts[0] + A_parts[1]   # S2 = A11 + A12
    S3 = A_parts[2] + A_parts[3]   # S3 = A21 + A22
    S4 = B_parts[2] - B_parts[0]   # S4 = B21 - B11
    S5 = A_parts[0] + A_parts[3]   # S5 = A11 + A22
    S6 = B_parts[0] + B_parts[3]   # S6 = B11 + B22
    S7 = A_parts[1] - A_parts[3]   # S7 = A12 - A22
    S8 = B_parts[2] + B_parts[3]   # S8 = B21 + B22
    S9 = A_parts[0] - A_parts[2]   # S9 = A11 - A21
    S10 = B_parts[0] + B_parts[1] # S10 = B11 + B12
    return [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]


def calculate_product_matrices(
    A_parts: List[np.ndarray],
    B_parts: List[np.ndarray],
    S: List[np.ndarray]
) -> List[np.ndarray]:
    """
    Compute the 7 Strassen product matrices P1..P7 recursively.

    Inputs:
        A_parts (List[np.ndarray]): [A11, A12, A21, A22]
        B_parts (List[np.ndarray]): [B11, B12, B21, B22]
        S (List[np.ndarray]): [S1, S2, ..., S10]

    Output:
        List[np.ndarray]: [P1, P2, ..., P7],
                          each of size (n/2) x (n/2)
    """
    P1 = strassen_matmul(A_parts[0], S[0]) # P1 = A11 @ S1
    P2 = strassen_matmul(S[1], B_parts[3]) # P2 = S2 @ B22
    P3 = strassen_matmul(S[2], B_parts[0]) # P3 = S3 @ B11
    P4 = strassen_matmul(A_parts[3], S[3]) # P4 = A22 @ S4
    P5 = strassen_matmul(S[4], S[5])        # P5 = S5 @ S6
    P6 = strassen_matmul(S[6], S[7])        # P6 = S7 @ S8
    P7 = strassen_matmul(S[8], S[9])       # P7 = S9 @ S10
    return [P1, P2, P3, P4, P5, P6, P7]


def calculate_C_partitions(P: List[np.ndarray]) -> List[np.ndarray]:
    """
    Compute the four quadrants of C from Strassen products.

    Input:
        P (List[np.ndarray]): [P1, P2, ..., P7]

    Output:
        List[np.ndarray]: [C11, C12, C21, C22],
                          each of size (n/2) x (n/2)
    """
    C11 = P[4] + P[3] - P[1] + P[5] # C11 = P5 + P4 - P2 + P6
    C12 = P[0] + P[1]                         # C12 = P1 + P2
    C21 = P[2] + P[3]                         # C21 = P3 + P4
    C22 = P[4] + P[0] - P[2] - P[6] # C22 = P5 + P1 - P3 - P7
    return [C11, C12, C21, C22]


def combine_C_partitions(
    C: np.ndarray,
    C_parts: List[np.ndarray]
) -> np.ndarray:
    """
    Combine four quadrants into the full matrix C.

    Inputs:
        C (np.ndarray): n x n zero matrix
        C_parts (List[np.ndarray]): [C11, C12, C21, C22]

    Output:
        np.ndarray: Completed n x n matrix C
    """
    half = C.shape[0] // 2
    C[:half, :half] = C_parts[0]     # top left
    C[:half, half:] = C_parts[1]    # top right
    C[half:, :half] = C_parts[2]  # bottom left
    C[half:, half:] = C_parts[3] # bottom right
    return C    


# import random

# # Reproducible randomness
# RNG = random.Random(245)
# NP_RNG = np.random.default_rng(245)

# # Define test cases once
# # Each test case is (name, n, kind)
# TEST_CASES = [
#     ("n1_basic", 1, "int_small"),
#     ("n2_basic", 2, "int_small"),
#     ("n4_negative", 4, "int_negative"),
#     ("n4_identity", 4, "identity"),
#     ("n8_zeros", 8, "zeros"),
#     ("n8_random", 8, "int_medium"),
#     ("n16_random", 16, "int_medium"),
#     ("n8_float", 8, "float"),
# ]

# def make_case(n, kind):
#     """Create (A,B) for a given test kind."""
#     if kind == "int_small":
#         A = NP_RNG.integers(-5, 6, size=(n, n), dtype=np.int64)
#         B = NP_RNG.integers(-5, 6, size=(n, n), dtype=np.int64)
#         return A, B
#     if kind == "int_negative":
#         A = NP_RNG.integers(-30, 1, size=(n, n), dtype=np.int64)
#         B = NP_RNG.integers(-30, 1, size=(n, n), dtype=np.int64)
#         return A, B
#     if kind == "int_medium":
#         A = NP_RNG.integers(-100, 101, size=(n, n), dtype=np.int64)
#         B = NP_RNG.integers(-100, 101, size=(n, n), dtype=np.int64)
#         return A, B
#     if kind == "identity":
#         A = NP_RNG.integers(-20, 21, size=(n, n), dtype=np.int64)
#         B = np.eye(n, dtype=np.int64)
#         return A, B
#     if kind == "zeros":
#         A = np.zeros((n, n), dtype=np.int64)
#         B = NP_RNG.integers(-10, 11, size=(n, n), dtype=np.int64)
#         return A, B
#     if kind == "float":
#         A = NP_RNG.normal(loc=0.0, scale=2.0, size=(n, n)).astype(np.float64)
#         B = NP_RNG.normal(loc=0.0, scale=2.0, size=(n, n)).astype(np.float64)
#         return A, B

#     # Fallback
#     A = NP_RNG.integers(-5, 6, size=(n, n), dtype=np.int64)
#     B = NP_RNG.integers(-5, 6, size=(n, n), dtype=np.int64)
#     return A, B


# def run_strassen_tests():
#     """
#     Run all test cases for strassen_matmul.

#     Returns:
#         List of test results (1 for pass, 0 for fail)
#     """
#     results = []

#     for test_name, n, kind in TEST_CASES:
#         try:
#             A, B = make_case(n, kind)

#             ground_truth = A @ B
#             candidate_result = strassen_matmul(A, B)

#             # Basic shape check
#             if not isinstance(candidate_result, np.ndarray):
#                 results.append(0)
#                 continue
#             if candidate_result.shape != (n, n):
#                 results.append(0)
#                 continue

#             # Correctness check
#             # Use allclose so float test passes; also safe for ints.
#             if np.allclose(candidate_result, ground_truth, atol=1e-8, rtol=1e-6):
#                 results.append(1)
#             else:
#                 results.append(0)

#         except Exception as e:
#             # print(f"Debug - strassen_matmul {test_name} Error: {e}")
#             results.append(0)

#     return results

# print(run_strassen_tests())