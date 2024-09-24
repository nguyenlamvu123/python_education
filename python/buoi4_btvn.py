# khuyến khích làm bài tập sau trên jupyter notebook
import numpy as np

# Tạo mảng
a = np.array([1,2,3])
print("1D array")
print(a)

# yêu cầu: Xác định kiểu của mảng và in ra màn hình

# Tạo mảng 2 chiều (ma trận)
b = np.array([[1,2,3],
              [4,5,6]])
print("2D array")
print(b)

# Tạo mảng 3 chiều (tensor)
c = np.array([[[1,2,3], [4,5,6]], 
              [[7,8,9], [10,11,12]]])
print("3D array")
print(c)

# Mảng 2 chiều chứa 1 dòng, nhưng không phải mảng 1 chiều
d = np.array(
    [
        [1, 2, 3]
    ]
)  # d = np.array([[1,2,3]])

# yêu cầu: In ra kích thước các mảng

# Các ma trận khác
print("Matrix of ones")  # yêu cầu: tạo ma trận các phần tử đều là 1 kích thước (2, 2)  # np.ones()
print("Matrix of zeros")  # yêu cầu: tạo ma trận các phần tử đều là 0 kích thước (2, 2)  # np.zeros()
print("Identity matrix")  # yêu cầu: tạo ma trận đơn vị 3 chiều  # np.eye()
print("Random matrix")  # yêu cầu: tạo ma trận ngẫu nhiên các phần tử nằm trong khoảng (0, 1) kích thước (3, 3)  # np.random.rand()
# Các toán tử cơ bản
a = np.array([[1,0,2],
              [2,3,0]])
b = np.array([[2,1,-1],
              [2,1,2]])

# yêu cầu: in ra màn hình a + b
# yêu cầu: in ra màn hình a - b
# yêu cầu: in ra màn hình a * b
# yêu cầu: in ra màn hình a / b

# Broadcasting
a = np.array([[1,0,2],
              [2,3,0]])
b = np.array([[1,2,1]])
c = np.array([[1],
              [2]])
print("Broadcasting")  # cho phép NumPy mở rộng kích thước của một hoặc nhiều mảng để phù hợp với kích thước của các mảng khác trong phép toán
# yêu cầu: in ra màn hình a - 1
# yêu cầu: in ra màn hình a - b
# yêu cầu: in ra màn hình a - c
# Chuyển vị ma trận
b = np.array([[2,1,-1],
              [2,1,2]])
print("b: ", b)
# yêu cầu: chuyển vị ma trận b  # b.T

# Nhân ma trận
# yêu cầu: nhân ma trận a với b chuyển vị  # np.matmul()

# Truy cập mảng
a = np.array([[1,0,2],
              [2,3,0]])
# yêu cầu: truy cập phần tử 1, 0
# yêu cầu: truy cập phần tử 1  # 1, :
# yêu cầu: truy cập phần tử vị trí 1 của mỗi phần tử  # :, 1
# yêu cầu: truy cập từ đầu đến vị trí 2 của mỗi phần tử 1  # :2, :2

# Masking
a = np.array([[1,0,2],
              [2,3,0]])
mask = a>=2
# yêu cầu: giải thích đầu ra sau
print(a[mask])

# Thay đổi phần tử trong mảng
a = np.array([[1,0,2],
              [2,3,0]])
print("Changed (0,1)")
# yêu cầu: thay đổi vị trí (0, 1) là 5
print(a)
# yêu cầu: giải thích đầu ra sau
a[:,0] = np.zeros((2,))
print(a)

# Thay đổi kích thước mảng
a = np.array([[1,0,2],
              [2,3,0]])
# yêu cầu: giải thích đầu ra sau
print(a.reshape((3,2)))
# yêu cầu: giải thích đầu ra sau
print(a.reshape((1,-1)))
