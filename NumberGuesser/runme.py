import stages


def difficulty():
    print('Please select a difficulty')

    try:
        diff = int(input(
            'Type \'1\' for Easy.\n\'2\' for Casual.\n\'3\' for Hard.\n\'4\' for Very Hard.\n\'5\' for Impossible.\n'))
        if diff == 1:
            stages.easy()
        elif diff == 2:
            stages.casual()
        elif diff == 3:
            stages.hard()
        elif diff == 4:
            stages.vhard()
        elif diff == 5:
            stages.impossible()
        else:
            print('Please input a valid number')
            difficulty()
    except ValueError:
        print('Please input a  valid number')
        difficulty()


difficulty()