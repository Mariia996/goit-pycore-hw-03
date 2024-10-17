import random


# random.randint()
def get_numbers_ticket(min, max, quantity):
    try:
        number_lst = []
        if min < 1:
            return number_lst
        elif max > 1000:
            return number_lst
        elif min >= quantity or quantity >= max:
            return number_lst

        while len(number_lst) != quantity:
            random_number = random.randrange(min, max)
            d_lst = set(number_lst + [random_number])
            number_lst = list(d_lst)

        return sorted(number_lst)

    except TypeError:
        print("All provided arguments must be integer.")


lottery_numbers = get_numbers_ticket(min=1, max=49, quantity=6)
print("Ваші лотерейні числа:", lottery_numbers)
