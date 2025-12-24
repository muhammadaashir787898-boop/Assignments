def sumed(arr):

    total = 0

    for i in arr:

        if type(i) == list:

         total = total + sum

        else:
            total = total + i
    return total