import numpy
from matplotlib import pyplot as plt
x = numpy.loadtxt(fname='/home/jang/github/language/2017-02-18_pythonpractice/inflammation-01.csv', delimiter=',')
print("최대값 =", x.max())
print("최소값 =", x.min())
print("평균값 =", x.mean())
plt.figure()
plt.plot(x[0:5])
plt.show()
