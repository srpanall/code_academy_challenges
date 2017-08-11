import math
from pprint import pprint


##ball_order = [0] * num_balls
##
##print(ball_order)
##
##all_orders = [ball_order] * num_balls
##
##for ball_index in range(num_balls):
##    all_orders[ball_index][ball_index] = 1



##def scaleOfTruth():

##print(ball_order)
##
##pprint(all_orders)

##num_balls = 8
##all_orders =[[0 if weight != ball_index else 1 for weight in range(num_balls)] for ball_index in range(num_balls)]

##pprint(all_orders)

def scaleOfTruthN1(num_balls):
##    num_balls = 8
##def scaleOfTruthN(num_balls):
    all_orders =[
                 [0 if ball != ball_index else 1 for ball in range(num_balls)]
                 for ball_index in range(num_balls)
                 ]
    num_tries = []

    for ball_order in all_orders:
        tries = 0
        temp_slice = [x for x in ball_order]
        test_val = num_balls
        while True:
            tries += 1
            slice_start, slice_end = test_val // 2, math.ceil(test_val / 2)
            if slice_start != slice_end and temp_slice[slice_start] == 1:
                num_tries += [tries]
                break
            if sum(temp_slice[:slice_start]) == 1:
                temp_slice = [x for x in temp_slice[:slice_start]]
            else:
                temp_slice = [x for x in temp_slice[slice_end:]]
            test_val = len(temp_slice)
            if test_val == 1:
                num_tries += [tries]
                break
    return num_tries


##print(scaleOfTruthN(15))


def compare_tries(n_balls):
    t_val = math.floor(math.log2(n_balls))
    e_val = max(scaleOfTruthN(n_balls))
    if t_val != e_val:
        print('breakdown for n = %s' % n_balls)
    elif n_balls % 50 == 0:
        print('relationship holds for n = %s' % n_balls)

##for n in range(3, 600):
##    compare_tries(n)



def scaleOfTruthN(num_balls):
    if num_balls % 2 == 1:
        return 1

    log_balls = math.log2(num_balls)
    int_log_balls = int(log_balls)

    if log_balls == int_log_balls:
        return int_log_balls

    for tries in range(1, int_log_balls+1):
        if num_balls % 2 ** tries != 0:
            return tries

##for n in range(3,41):
##    weighings = scaleOfTruthN(n)
##    word_case = 'weighing'
##    if weighings != 1:
##        word_case += 's'
##
##    print(n, 'balls require at least %s %s.' % (weighings, word_case))



def compare_tries_2(n_balls):
    t_val = scaleOfTruthN(n_balls)
    e_val = min(scaleOfTruthN1(n_balls))
    if t_val != e_val:
        print('breakdown for n = %s' % n_balls)
    elif n_balls % 50 == 0:
        print('relationship holds for n = %s' % n_balls)


for n in range(3, 20):
##    compare_tries_2(n)

