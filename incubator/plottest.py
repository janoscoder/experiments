import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.ion()
plt.show()
for i in range(1, 1000):
    plt.plot(1, i*0.01, 2, i*0.02)
    plt.draw()