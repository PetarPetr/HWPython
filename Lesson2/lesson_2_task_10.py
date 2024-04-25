def bank(X, Y):
    balance = X
    for _ in range(Y):
        balance = balance * 1.1
        return balance