from search import table_data


def decrease(s):
    c, n, w, v = table_data(s)
    x, y = vw(c, n, w, v)
    for i in range(len(x)):
        for m in range(i):
            if x[i] > x[m]:
                t = x[i]
                x[i] = x[m]
                x[m] = t
                t = y[i]
                y[i] = y[m]
                y[m] = t
                t = w[i]
                w[i] = w[m]
                w[m] = t
                t = v[i]
                v[i] = y[m]
                v[m] = t
    print("背包容量：", c, "物品个数：", n)
    print("重量:", w)
    print("价值:", v)
    print("按单位价值递减排序得：", y)
    return c, n, w, v, x, y


def increase(s):
    c, n, w, v = table_data(s)
    print(c, n)
    print(w, v)
    x, y = vw(c, n, w, v)
    for i in range(len(x)):
        for m in range(i):
            if x[i] < x[m]:
                t = x[i]
                x[i] = x[m]
                x[m] = t
                t = y[i]
                y[i] = y[m]
                y[m] = t
                t = w[i]
                w[i] = w[m]
                w[m] = t
                t = v[i]
                v[i] = y[m]
                v[m] = t
    print("背包容量：", c, "物品个数：", n)
    print("重量:", w)
    print("价值:", v)
    print("按单位价值递增排序得：", y)
    return c, n, w, v, x, y


def vw(c, n, w, v):
    x = []
    y = []
    for i in range(n):
        x.append(v[i]/w[i])
        y.append(i+1)
    return x, y


# increase('beibao0.in')
# decrease('beibao0.in')