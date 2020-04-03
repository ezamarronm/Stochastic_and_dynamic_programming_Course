from drunkGuy import TypicalDrunkGuy
from coordinate import Coordinate
from field import Field
from bokeh.plotting import figure,  show

def main(walking_distances, tries, type_of_DrunkGuy):
    average_distance_per_walk = []
    for steps in walking_distances:
        distances = simulate_walking(steps, tries, type_of_DrunkGuy)
        average_distance = round(sum(distances) / len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)
        average_distance_per_walk.append(average_distance)
        print(f"{type_of_DrunkGuy.__name__} had a random walk of: {steps} steps ")
        print(f"Average distance: {average_distance}")
        print(f"Max distance: {max_distance}")
        print(f"Min distance: {min_distance}")
    toPlot(walking_distances, average_distance_per_walk)

def simulate_walking(steps, tries, type_of_DrunkGuy):
    drunkGuy = type_of_DrunkGuy(name = 'Angel')
    origin = Coordinate(0,0)
    distances = []

    for item in range(tries):
        field = Field()
        field.add_drunk_guy(drunkGuy, origin)
        simulation_of_the_walking = take_a_walk(field, drunkGuy, steps)
        distances.append(round(simulation_of_the_walking, 1))
    return distances

def take_a_walk(field, drunkGuy, steps):
    origin = field.get_coordinate(drunkGuy)
    
    for step in range(steps):
        field.move_drunk_guy(drunkGuy)
    return origin.distance(field.get_coordinate(drunkGuy))

def toPlot(x,y):
    graph = figure(title = 'Random Walk', x_axis_label='steps', y_axis_label='distance')
    #graph.line = (x,y, legend='Medium distance')
    print(x,y)
    #graph.line(x,y, line_width = 2, legend='Medium distance')
    graph.line(x,y, line_width = 2, legend='Medium distance')
    show(graph)

if __name__ == '__main__':
    walking_distances = [10,100,1000, 10000]
    tries = 100

    main(walking_distances, tries, TypicalDrunkGuy) #Sending the class and not an instance of it.
