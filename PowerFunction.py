def userPow(base, exponent, modulo):
    if exponent == 0:
        return 1

    p = userPow(base, exponent // 2, modulo)

    if exponent & 1:
        return (p * p * base) % modulo
    else:
        return (p * p) % modulo


if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())

    print(userPow(A, B, C))
