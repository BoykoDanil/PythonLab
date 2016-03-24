def addWeight():
    """
    In this function you add your weight
    :return:weight
    """
    waight = input()
    return waight


def addHeight():
    """
    In this function you add your height
    :return:height
    """
    height = input()
    return height


def addAge():
    """
    In this function you add your age
    :return:age
    """
    age = input()
    return age


def chooseNumberOfT(number):
    """
    In this function you choose how often you do physical exercises
    :param number:Number of your week train
    :return:factor that depends on your week trains
    """
    if (number == 1):
        factor = 1.2
    elif (number == 2):
        factor = 1.375
    elif (number == 3):
        factor = 1.4625
    elif (number == 4):
        factor = 1.550
    elif (number == 5):
        factor = 1.6375
    elif (number == 6):
        factor = 1.725
    elif (number == 7):
        factor = 1

    return factor


def calculation(weight, height, age, factor):
    """

    :param weight:your weight
    :param height:your height
    :param age:your age
    :param factor:factor that depends on your week trains
    :return:callories that your must get every day
    """
    nCallories = (int)((10 * weight + 6.25 * height - 5 * age - 161) * factor)
    return nCallories
