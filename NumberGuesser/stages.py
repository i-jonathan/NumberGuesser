import maingame


def easy():
    # easy difficulty. Number of tries
    a = 1
    b = 20
    tries = 7
    diff = 'Very Easy'
    # select random number
    maingame.maingame(a, b, tries, diff)


def casual():
    # Casual difficulty. Number of tries
    a = 1
    b = 30
    tries = 7
    diff = 'Casual'
    # select random number
    maingame.maingame(a, b, tries, diff)


def hard():
    # Hard difficulty. Number of tries
    a = 1
    b = 150
    tries = 7
    diff = 'Hard'
    # select random number
    maingame.maingame(a, b, tries, diff)


def vhard():
    # easy difficulty. Number of tries
    a = 1
    b = 250
    tries = 9
    diff = 'Very Hard'
    # select random number
    maingame.maingame(a, b, tries, diff)


def impossible():
    # easy difficulty. Number of tries
    a = 1
    b = 500
    tries = 10
    diff = 'Impossible'
    # select random number
    maingame.maingame(a, b, tries, diff)
