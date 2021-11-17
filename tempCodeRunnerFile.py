    dict = {}
    total = 0
    single = False
    for letter in str:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    for value in dict.values():
        if value % 2 == 0:
            total += value
        else:
            if not single:
                total += 1
                single = True