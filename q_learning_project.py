from pprint import pprint
import numpy as np
import random
# constant values
GRID_WORLD_SIZE = 10
reward_mechanism = 0
possible_roads = ['right', 'left', 'up', 'down']
RIGHT_VALUE = 1
LEFT_VALUE = -1
UP_VALUE = -1
DOWN_VALUE = 1
#current_state = []
#goal_state = []
#rewards_dict = {}
#roads_dict = {}

starting_state = [0, 0]
loading_state = [9, 9]
unload_state = [0, 9]

minus_10_reward = [
    [0, 5], [0, 6], [0, 7],
    [1, 5], [1, 6], [1, 7]
]

cannot_pass_through_phases = [
    [2, 5], [2, 6], [2, 7],
    [3, 5], [3, 6], [3, 7],
    [4, 6], [4, 7],
    [6, 0], [7, 0], [7, 1],
    [8, 0], [8, 1], [8, 2],
    [9, 0], [9, 1], [9, 2], [9, 3]
]

possibility_pass = [
    [3, 1], [4, 2], [5, 3],
    [6, 4], [7, 5], [8, 6],
    [8, 7]
]

current_state = starting_state

grid_world = np.matrix(np.zeros(shape=(GRID_WORLD_SIZE, GRID_WORLD_SIZE)))
# print(grid_world)
#for i in range(0, GRID_WORLD_SIZE):
#    for j in range(0, GRID_WORLD_SIZE):
#        grid_world[(i, j)] = 0

indexes = np.argwhere(grid_world == -0.1)
print(grid_world)
# print(grid_world[(0, 9)])


def go_to_load_state(env, loading_state_for_func, discount_factor=1.0, alpha=0.6, epsilon=0.1):

    while not (current_state == loading_state_for_func):
        res = random.choice(possible_roads)
        # print(res)
        if res == "right":
            if current_state[1] + 1 >= 10:
                print('Bigger then 10. right')
            else:
                current_state[1] += 1
                if current_state == loading_state_for_func:
                    grid_world[(current_state[0],current_state[1])] = grid_world[(current_state[0],current_state[1])] + epsilon*(1000 + (discount_factor*0))
                else:
                    pass


        elif res == "left":
            if current_state[1] - 1 < 0:
                print('Negative. left')
            else:
                current_state[1] -= 1
                if current_state == loading_state_for_func:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))
                else:
                    pass


        elif res == "up":
            if current_state[0] - 1 < 0:
                print('Negative. up')
            else:
                current_state[0] -= 1
                if current_state == loading_state_for_func:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))
                else:
                    pass


        else:
            if current_state[0] + 1 >= 10:
                print('Bigger then 10. down')
            else:
                current_state[0] += 1
                if current_state == loading_state_for_func:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))
                else:
                    pass



def go_to_unload_state(env, unload_state_for_func, discount_factor=1.0, alpha=0.6, epsilon=0.1):
    while not (current_state == unload_state_for_func):
        res = random.choice(possible_roads)
        # print(res)
        if res == "right":
            if current_state[1] + 1 >= 10:
                print('Bigger then 10. right')
            else:
                current_state[1] += 1
                if current_state == unload_state_for_func:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))
                else:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))


        elif res == "left":
            if current_state[1] - 1 < 0:
                print('Negative. left')
            else:
                current_state[1] -= 1
                if current_state == unload_state_for_func:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))
                else:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))


        elif res == "up":
            if current_state[0] - 1 < 0:
                print('Negative. up')
            else:
                current_state[0] -= 1
                if current_state == unload_state_for_func:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))
                else:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))


        else:
            if current_state[0] + 1 >= 10:
                print('Bigger then 10. down')
            else:
                current_state[0] += 1
                if current_state == unload_state_for_func:
                    grid_world[(current_state[0], current_state[1])] = grid_world[(
                    current_state[0], current_state[1])] + epsilon * (1000 + (discount_factor * 0))
                else:
                    pass

def go_back_to_starting_state(env, starting_state_for_func, discount_factor=1.0, alpha=0.6, epsilon=0.1):
    pass


