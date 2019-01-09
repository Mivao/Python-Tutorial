

def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """

    return n1 + n2


sum1 = sum_nums(2, 8)

sum2 = sum_nums(3, 3)

print(sum1)


def is_metro(city):

    """
    Tells us if a city is in our list of metros
    :param city:
    :return:
    """

    metros = ['sfo', 'nyc', 'la']

    if city in metros:
        return True
    else:
        return False


x = is_metro('boston')
print(x)

