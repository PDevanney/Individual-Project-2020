import random
from itertools import combinations

import numpy as np
from src.distances import populate_distance_table
from src.movement import find_optimal_node


class RandomTower:

    # ToDo Done? - Array of Unique Random Values?
    def initial_position(self, G, tower_count):
        return random.sample(G.nodes, tower_count)

        #tower_location = []
        #while len(tower_location) != tower_count:
        #    position = random.randrange(0, number_of_nodes)
        #    if position not in tower_location:
        #        tower_location.append(position)
        #return tower_location


class HeuristicTower:
    # ind = np.argpartition(a, -4)[-4:]
    def initial_position(self, G, tower_count):
        unique_distances = []
        for node in G.nodes:
            unique_distances.append(len(set((populate_distance_table(G, node)).values())))

        # optimal = []
        #while len(optimal) != tower_count:
        #    optimal_index = np.argmax(unique_distances)

        #    if optimal_index != target_location:
        #        optimal.append(optimal_index)
        #        unique_distances[optimal_index] = -1

        optimal = np.argpartition(unique_distances, -tower_count)[-tower_count:]
        return optimal


class OptimalTower:

    def initial_position(self, G, tower_count):
        tower_combinations = combinations(list(G.nodes), tower_count)

        optimal_tower = len(G.nodes) + 1

        for comb in list(tower_combinations):
            path_length = find_optimal_node(G, list(comb))[0]

            if path_length < optimal_tower:
                optimal_comb = list(comb)
                optimal_tower = path_length

        return optimal_comb
