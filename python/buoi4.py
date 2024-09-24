# # i = 0
# # ii = 5
# #
# # if i == 0:
# #     if ii == 5:
# #         print('đúng rồi')
# #
# # if i == 0 and ii == 5:
# #     print('đúng rồi')
# #
# # if all([
# #     i == 0,
# #     ii == 5,
# # ]):  # pythonic
# #     print('đúng rồi')
# #
# # if i == 1 or ii == 5:
# #     print('toán tử or')
# #
# # if any([
# #     i == 1,  # False
# #     ii == 5,  # True
# # ]):  # pythonic  # True
# #     print('ttttttttttttttttoán tử or')
import numpy as np
# from numpy import log
#
# arr = np.array([
#     [1, 2, 3, 4, 5],
#     [10, 2, 30, 4, 50]
# ])
arr = np.array([
    [
        [4, 8, 5, 7],
        [6, 5, 6, 7],
        [4, 3, 4, 3],
    ],
    [
        [2, 9, 2, 2],
        [3, 2, 2, 3],
        [6, 8, 3, 2],
    ],
])
# print(arr)
print(arr.shape)
# print(arr.dtype)
# print(arr.reshape((5, 2)))
# print(arr[1, 3])
# print(arr[1][3])
# print(arr[1][2:-2])
#
# log = np.log(arr)
# np.save('np.npy', log)
log = np.load('np.npy')
print(log)