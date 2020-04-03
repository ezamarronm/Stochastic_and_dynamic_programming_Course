import random
class Dice():
    def __init__(self):
        pass
    def throw_dice(self):
        return random.choice([1,2,3,4,5,6])

def throw_dices(dices):
    sum_of_dices = 0
    for dice in dices:
        dice_result = dice.throw_dice()
        sum_of_dices += dice_result
    return sum_of_dices

def simulate(number_of_times, dices):
    dice_results = []
    for _ in range(number_of_times):
        #dice_result = random.choice([1,2,3,4,5,6])
        sum_of_dices = throw_dices(dices)
        dice_results.append(sum_of_dices)
    return dice_results


def main(number_of_times, number_of_simulations,number_of_dices, number_expected):
    simulations_results = []
    dices = []
    for _ in range(number_of_dices):
        dices.append(Dice())
    
    for _ in range(number_of_simulations):
        dice_results = simulate(number_of_times, dices)
        simulations_results.append(dice_results)

    throwings_with_number_expected = 0
    for one_simulation in simulations_results:
        #if 1 in one_simulation:
        if number_expected in one_simulation:
            throwings_with_number_expected += 1
    throwings_with_1_probability = throwings_with_number_expected / number_of_simulations
    print(f'Probability of get at least a {number_expected} in {number_of_times} throwings with {number_of_dices} is: {throwings_with_1_probability}')
    
if __name__ == '__main__':
    number_of_dices = int(input('How many dices: '))
    number_of_times = int(input('How many times throw the dices: '))
    number_of_simulations = int(input('How many times run the simulation: '))
    number_expected = int(input('Number expecting to get: '))

    main(number_of_times, number_of_simulations, number_of_dices, number_expected)



    