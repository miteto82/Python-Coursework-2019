def is_leap(year):
    leap = False
    quard = int(year / 4)
    one_hund = int(year / 100)
    four_hund = float(year / 400)

    if year % quard == 0:
        leap = True
    if year % one_hund == 0:
        leap = False
    if year / 400 and four_hund % 1 == 0:
        leap = True

    return leap

