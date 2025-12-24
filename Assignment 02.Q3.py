def count_f(arr,f=None):
    if f is None:
        f = {}
    for i in arr:
        if type(i) == list:
            count_f(i,f)
        else:
            f[i] = f.get(i,0) + 1
    return f
