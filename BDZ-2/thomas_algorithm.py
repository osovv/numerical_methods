n = 4
a = [0 ,-3 , -10, -5]
b = [0, -5, 8, 4]
c = [0, -9, -22, -10]
z = [0, 0.22, -0.4]
mu = [0, -0.44, -1]
f = [0, 1, -8, 3]



alpha = [0 for i in range(n+1)]
beta = [0 for i in range(n+1)]

y = [0 for i in range(n+1)]

alpha[1] = z[1]
beta[1] = mu[1]

for j in range(1, n):
    alpha[j+1] = b[j] / (c[j] - alpha[j] * a[j])
    beta[j+1] = (alpha[j]*beta[j] + f[j])/(c[j]-alpha[j]*a[j])

y[n] = (z[2]*beta[n] + mu[2])/(1-z[2]*alpha[n])

for j in range(n-1, -1, -1):
    y[j] = alpha[j+1]*y[j+1] + beta[j+1]

print(f"Alpha: {alpha[1:]}")
print(f"Beta: {beta[1:]}")
print(f"y: {y}")

