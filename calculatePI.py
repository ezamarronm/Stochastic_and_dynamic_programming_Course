import random
from probabilityDistributions import standard_deviation, mean
def throw_needles(number_of_needles):
    in_the_circle = 0

    for _ in range(number_of_needles):
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])
        distance_from_the_center = (x**2 + y**2) ** 0.5

        if distance_from_the_center <= 1:
            in_the_circle += 1
    return (4* in_the_circle) / number_of_needles

def estimate(number_of_needles, number_of_simulations):
    estimations = []

    for _ in range(number_of_simulations):
        pi_estimated = throw_needles(number_of_needles)
        estimations.append(pi_estimated)
    mean_of_estimations = mean(estimations)
    sigma = standard_deviation(estimations)
    print(f'Estimate of pi = {round(mean_of_estimations,5)}, sigma = {round(sigma,5)}, needles = {number_of_needles}')
    return (mean_of_estimations, sigma)

def estimate_pi(precision, number_of_simulations):
    number_of_needles = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        mymean, sigma = estimate(number_of_needles, number_of_simulations)
        number_of_needles *=2
    return mymean
if __name__ == '__main__':
    estimate_pi(0.01, 30)