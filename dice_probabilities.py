import random

def throw_dice(number_of_times):
    dice_results = []
    for _ in range(number_of_times):
        dice_result = random.choice([1,2,3,4,5,6])
        dice_results.append(dice_result)
    return dice_results

def main(number_of_times, number_of_simulations):
    simulations_results = []
    for _ in range(number_of_simulations):
        dice_results = throw_dice(number_of_times)
        simulations_results.append(dice_results)

    throwings_with_1 = 0
    for one_simulation in simulations_results:
        if 1 in one_simulation:
            throwings_with_1 += 1
    throwings_with_1_probability = throwings_with_1 / number_of_simulations
    print(f'Probability of get at least a "1" in {number_of_times} throwings = {throwings_with_1_probability}')
    
if __name__ == '__main__':
    number_of_times = int(input('How many times throw the dice: '))
    number_of_simulations = int(input('How many times run the simulation: '))

    main(number_of_times, number_of_simulations)