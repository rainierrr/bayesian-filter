import numpy as np
from fractions import Fraction
x = np.array([4, 15, 30, 100])
y = np.array([-17, -4, -7, 50])
# x = np.array([50, 60, 70, 80, 90])
# y = np.array([40, 70, 90, 60, 100])
n = len(x)

avg_x = Fraction(sum(x), n)
avg_y = Fraction(sum(y), n)
print("平均x: {}, 平均y: {}\n".format(avg_x, avg_y))
deviation_list = []
x_deviation_list = []
for i in range(n):
    x_deviation = x[i]-avg_x
    y_deviation = y[i]-avg_y
    product_deviation = x_deviation * y_deviation
    x_deviation_list.append(x_deviation)
    deviation_list.append(product_deviation)
    print("idx: {}, 偏差x: {}, 偏差y: {}, 偏差の積: {}".format(
        i, x_deviation, y_deviation, product_deviation))
print()

# xの分散
x_covariance = sum(list(map(lambda x: x**2, x_deviation_list))) / n

# 分散
covariance = sum(deviation_list) / n
print("xの分散: {}, 共分散: {}".format(x_covariance, covariance))

a = covariance / x_covariance
b = avg_y - a*avg_x
print("a: {}, b: {}".format(a, b))
print("float a: {}, b: {}".format(float(a), float(b)))
