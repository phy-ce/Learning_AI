import numpy as np

mat1 = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])
mat2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 3, 4])
arrone_at_arrtwo = arr1@arr2
arrone_star_arrtwo = arr1*arr2
mat1_at_mat2 = mat1@mat2
mat1_star_mat2 = mat1*mat2

print(f"{arr1=}")
print(f"{arr2=}")
print(f"{mat1=}")
print(f"{mat2=}")
print(f"{arrone_at_arrtwo=}")
print(f"{arrone_star_arrtwo=}")
print(f"{mat1_at_mat2=}")       #普通の行列積
print(f"{mat1_star_mat2=}")     #hadamard product