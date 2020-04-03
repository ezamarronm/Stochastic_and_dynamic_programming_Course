class Field:
    def __init__(self):
        self.drunk_guys_coordinates = {}
    
    def add_drunk_guy(self, drunkGuy, coordinate):
        self.drunk_guys_coordinates[drunkGuy] = coordinate #'DrunkGuy' is the key and 'coordinate' the value
    def move_drunk_guy(self, drunkGuy):
         delta_x, delta_y = drunkGuy.walk()
         current_coordinate = self.drunk_guys_coordinates[drunkGuy]
         new_coordinate = current_coordinate.move(delta_x, delta_y)

         self.drunk_guys_coordinates[drunkGuy] = new_coordinate

    def get_coordinate(self, drunkGuy):
        return self.drunk_guys_coordinates[drunkGuy]
              
