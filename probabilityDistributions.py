import random
def mean(X):
    return sum(X) / len(X)

def variance(X):
    mu = mean(X)
    accumulator = 0
    for x in X:
        accumulator += (x - mu) **2
    #return accumulator / len(X)
    return sum ( [ (x-mu) ** 2 for x in X ] ) / len(X)

def standard_deviation(X):
    return variance(X) ** 0.5
if __name__ == '__main__': 
    len_x = 20
    X = [ random.randint(9,12) for i in range(len_x) ] 
    mu = mean(X)
    Var = variance(X)
    sigma = standard_deviation(X)
    #print(X)
    print(f"Average of X = {mu}")
    print(f"Variation of X = {Var}")
    print(f"Standard deviation of X = {sigma}")
