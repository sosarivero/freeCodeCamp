import copy
import random


class Hat:
    def __init__(self, **kwargs):
        # Creates a list to append all the balls.
        self.contents = []
        # Loop to append the balls. i.e {"red": 2} -> ["red", "red"]
        for key, value in kwargs.items():
            # Using '_' as it is an idiom that shows that we will not use the variable.
            for _ in range(value):
                self.contents.append(key)

    def draw(self, balls):
        # Returns all balls if the user tries to remove more than there are.
        if balls > len(self.contents):
            return self.contents
            # Creates a list of drawn balls.
        self.drawn_balls = []
        for _ in range(balls):
            # Randomly removes 'balls' balls from the contents of the hat and adds it to the other list.
            self.drawn_balls.append(self.contents.pop(
                random.randint(0, len(self.contents) - 1)))
        return self.drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    # Makes a dictionary out of the expected_balls argument.
    target = dict(expected_balls)

    for _ in range(num_experiments):
        # Uses a deepcopy to make an experimental hat within the loop iteration.
        experiment_hat = copy.deepcopy(hat)

        # Creates a dictionary of key, values from the drawn() output.
        experiment_drawn = dict()
        for ball in experiment_hat.draw(num_balls_drawn):
            if ball in experiment_drawn:
                experiment_drawn[ball] += 1
            else:
                experiment_drawn[ball] = 1

        target_drawn = True

        # Check if the balls drawn during the experiment satisfy the expected balls requisites.
        # Use .get(key) to be able to compare the values.
        for key in target:
            try:
                if experiment_drawn.get(key) < target.get(key):
                    target_drawn = False
                    break
            # Using except in case the key does not exist in the experimental drawn dictionary.
            # A bit hacky, there might be a better way to do this.
            except Exception:
                target_drawn = False
                break

        if target_drawn == True:
            success += 1

    return (success / num_experiments)
