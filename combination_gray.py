import math


def genB0(l, n, k):
    res = [-1]
    for i in range(0, k):
        res.append(1)
    for i in range(0, n - k):
        res.append(0)

    def print_res():

        ans = [l[index] for index, i in enumerate(res[1:]) if i == 1]
        print(ans, res[1:])

    def genB(n, k):
        if k > 0 and k < n:
            genB(n - 1, k)
            if k == 1:
                swap(n, n - 1)
            else:
                swap(n, k - 1)
            negB(n - 1, k - 1)

    def negB(n, k):
        if k > 0 and k < n:
            genB(n - 1, k - 1)
            if k == 1:
                swap(n, n - 1)
            else:
                swap(n, k - 1)
            negB(n - 1, k)

    def swap(i, j):
        res[i], res[j] = res[j], res[i]
        print_res()

    print_res()
    genB(n, k)


def gen5_6(l, n, k):
    res = [None for i in range(n+2)]
    res[k+1] = n + 1
    K = k
    total = 0

    def print_res():
        print(res[1: k + 1])

    def genA(n):
        nonlocal total
        if n == 0:
            total += 1
            print_res()
            return
        if n % 2 == 1:
            for j in range(n, res[n + 1]):
                res[n] = j
                genA(n - 1)
        else:
            for j in range(res[n + 1] - 1, n-1, -1):
                res[n] = j
                genA(n - 1)

    genA(k)
    print(total)



def C(n, k):
    return math.comb(n, k)



def unrank(k, r):
    # there is no n here
    res = [None for i in range(k+1)]
    for i in range(k, 0, -1):
        p = i - 1
        while True:
            p = p + 1
            if C(p, i) > r:
                break
        r = r - C(p-1, i)
        res[i] = p

    print(res[1: k+1])


def unrank_colex(k, r):
    res = [None for i in range(k+1)]
    i = k - 1
    # the item from 0 1 2 3
    # not start at 1 

    while i >= 0:
        l = i
        while C(l, i + 1) <= r:
            l = l + 1
        res[i] = l
        r = r - C(l-1, i+1)
        i = i - 1
    print(res[0:k])


def unrank_lex(n, k, m):
    # understand different alg how to start rank from 0
    # understand different how to treat res start from 0 from from 1
    # https://computationalcombinatorics.wordpress.com/2012/09/10/ranking-and-unranking-of-combinations-and-permutations/
    res = [k for i in range(k+1)]
    i = 0
    t = 0
    while i < k:
        v = C(n-1-t, k-i-1)
        if v <= m:
            m = m - v
        else:
            res[i] = t + 1
            i = i + 1
        t = t + 1
    print(res[:k])


def trans_inter5_7(n, k):
    res = [i for i in range(n+2)]
    res[k+1] = n + 1
    j = k
    total = 0  # I need rank
    N = n

    def print_res():
        nonlocal total
        total += 1
        print(res[1:N + 1])

    while True:

        if total >= C(n, k):
            break
        print_res()
        if j < 1:
            res[1] = res[1] - 1
            if res[1] == 1:
                j = j + 2
        else:
            if res[j+1] == res[j] + 1:
                res[j+1], res[j] = res[j] , j
                if res[j+1] == res[j] + 1:
                    j = j + 2
            else:
                res[j] = res[j] + 1
                if j > 1:
                    res[j-1] = res[j] - 1
                    j = j - 2
    print(total)


def gen5_8(l, n, k):
    res = [-1]
    K = k
    for i in range(0, k):
        res.append(1)
    for i in range(0, n - k):
        res.append(0)

    result = set()
    def print_res(k, n):

        ans = [l[index] for index, i in enumerate(res[1:]) if i == 1]
        result.add(tuple(res[:]))
        print(ans, res[1:])

    def gen(n, k):

        if k > 1 and k < n:
            gen(n-1, k)
            swap(n, n-1, k, n)
            neg(n-2, k-1)
            swap(k-1, n-1, k, n)
            gen(n-2, k-2)

        else:
            
            if k == 1:
                for i in range(1, n):
                    swap(i, i +1, k, n)


    def neg(n, k):
        if k > 1 and k < n:
            neg(n-2, k-2)
            swap(k-1, n-1, k, n)
            gen(n-2, k-1)
            swap(n-1, n, k, n)
            neg(n-1, k)

        else:
            
            if k == 1:
                for i in range(1, n):
                    swap(i+1, i, k, n)


    def swap(i, j, k, n):
        res[i], res[j] = res[j], res[i]
        print_res(k, n)

    print_res(k, n)
    gen(n, k)
    print(len(result))



def gen5_9(l, n, k):
    # 5.9
    res = [None]
    # P131
    for i in range(n-k-1, 0, -1):
        res.append(0)
    for i in range(0, k):
        res.append(1)
    res.append(0)

    result = set()
    def swap(i, j):
        res[i], res[j] = res[j], res[i]
        print_res(k, n)



    def print_res(k, n):
        ans = [l[index] for index, i in enumerate(res[1:]) if i == 1]
        result.add(tuple(res[:]))
        print(ans, res[1:])

    def gen(n, k, p):  
        if p == 1:
            if k == n - 1:
                for i in range(n-1, 0, -1):
                    swap(i, i+1)
            else:
                if k > 0 and k < n - 1:
                    neg(n-1, k, 1) 
                    swap(n-2, n)  
                    gen(n-1, k-1, 0)
        else:
            if 0 < k and k < n - 1:
                gen(n-1, k, 1)
                swap(n-1, n)
                gen(n-1, k-1, 1)

    def neg(n, k, p):
        if p == 1:
            if k == n - 1: 
                for i in range(1, n):
                    swap(i, i+1)
            else:
                if k > 0 and k < n - 1:
                    neg(n-1, k-1, 0) 
                    swap(n-2, n)
                    gen(n-1, k, 1)
        else:
            if 0 < k and k < n - 1:
                neg(n-1, k-1, 1)
                swap(n-1, n)
                neg(n-1, k, 1)

    print_res(k, res[1:n+1])
    gen(n, k, 1)
    print(len(result))


if __name__ == "__main__":
    l = list(range(1, 11))


    # print('-------')
    for i in range(10):
        unrank(3, i)  # This is from index = 0
    print("------")
    
    for i in range(10):
        unrank_colex(3, i)  # This is from index = 
    print("------")
    for i in range(10):
        unrank_lex(5, 3, i)  # This is from index = 
    print("------")


    genB0(l, 6, 3)  # is ok
    print('-------')
    # print('-------')
    trans_inter5_7(6, 3)
    print('gen5_8 --------------')
    gen5_8(l, 8, 3)
    print('gen5_9 --------------')
    gen5_9(l, 8, 3)
