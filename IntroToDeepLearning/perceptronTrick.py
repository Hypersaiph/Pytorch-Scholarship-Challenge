epochs = 100
w1 = 3.0
w2 = 4.0
b = -10.0

learning_rate = 0.1

x1 = 1.0
x2 = 1.0

# print((w1 + (x1 * learning_rate)))
# print((w2 + (x2 * learning_rate)))

for i in range(1, epochs):
    z = (w1 + (x1 * learning_rate)) + (w2 + (x2 * learning_rate)) + (b + (1 * learning_rate))
    print(z, learning_rate)
    learning_rate += 0.1
    if z >= 0:
        break
