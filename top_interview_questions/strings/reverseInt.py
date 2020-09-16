def reverse(x):
    overflowInt = (2 ** 31) - 1
    sgnPos = True
    if x < 0:
        x *= -1
        sgnPos = False

    y = 0
    while x > 0:
        y = (y * 10) + (x % 10)
        if y > overflowInt:
            return 0
        x = int(x / 10)
    return y if sgnPos else y * -1
