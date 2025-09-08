# import matplotlib.pyplot as plt
# import numpy as np

# n = np.linspace(1, 5)

# f1 = 2*n - 1
# f2 = 4*n + 1
# f3 = (3/2)*(n**2) + (3/2)*n + 1

# # 시각화
# plt.figure(figsize=(10,6))
# plt.plot(n, f1, label=r'$2n - 1$')
# plt.plot(n, f2, label=r'$4n + 1$')
# plt.plot(n, f3, label=r'$\frac{3}{2}n^2 + \frac{3}{2}n + 1$')

# # 그래프 설정
# plt.xlabel("n", fontsize=12)
# plt.ylabel("T(n)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()

def number_of_bits(n):
    cnt = 0
    while n > 0:
        n = n // 2
        cnt += 1
    return cnt
print(number_of_bits(8))