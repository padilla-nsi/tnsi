def conv_bin(n):
    tab_bin = []
    bits = 0
    while n > 0:
        b = n % 2
        n = n // 2
        bits += 1
        tab_bin.append(b)
    tab_bin.reverse()
    return (tab_bin, bits)


assert conv_bin(9) == ([1, 0, 0, 1], 4)