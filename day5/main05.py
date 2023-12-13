import time

example_path = 'day5/example05.txt'
puzzle_path = 'day5/puzzle05.txt'

def extract_lines_from_file(file_path):
    # Return a list of lines from a file
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        return lines

def extract_seeds_and_maps(lines):
    seeds = []
    maps = []
    current_map = None

    for line in lines:
        line = line.strip()  # remove trailing and leading whitespace

        if line.startswith('seeds:'):
            # extract seed numbers
            seeds = [int(num) for num in line[7:].split()]
        elif line.endswith('map:'):
            # start a new map
            if current_map is not None:
                maps.append(current_map)
            current_map = []
        elif line == '':
            # end of a map
            if current_map is not None:
                maps.append(current_map)
                current_map = None
        elif current_map is not None:
            # add line to current map
            current_map.append([int(num) for num in line.split()])

    # add the last map if it wasn't added already
    if current_map is not None:
        maps.append(current_map)

    return seeds, maps

def map_seed(seed, map):
    # Return a new seed number
    new_seed = seed
    # check ranges of map
    for range in map:
        # check if seed is in range
        starting_number = int(range[1])
        ending_number = starting_number + int(range[2]) - 1
        if starting_number <= seed <= ending_number:
            # add the offset (linear mapping)
            # print(f' seed is in range {range}')
            offset = int(range[0]) - int(range[1])
            new_seed += offset
        else:
            # print(f' seed is not in range {range}')
            continue
    return new_seed

def lowest_item_dic(locations):
    # Return the key with the lowest value in a dictionary
    lowest_value = None
    lowest_key = None
    for key, value in locations.items():
        if lowest_value is None or value < lowest_value:
            lowest_value = value
            lowest_key = key
    return lowest_key, lowest_value

def process_seed_ranges(seeds, maps):
    seed_set = set()
    for i in range(0, len(seeds), 2):
        start_seed = seeds[i]
        seed_range = seeds[i+1]
        # This is too slow for the puzzle input
        for seed in range(start_seed, start_seed + seed_range):
            seed_set.add(seed)

    locations = {}
    for seed in seed_set:
        new_mapped_seed = seed
        for i, map in enumerate(maps):
            new_mapped_seed = map_seed(new_mapped_seed, map)
        locations[new_mapped_seed] = seed

    return locations

def apply_maps_to_seed(seed, maps):
    for map in maps:
        seed = map_seed(seed, map)
    return seed
    
def main05a(file_path):
    # Extract the lines from the file
    lines = extract_lines_from_file(file_path)
    seeds, maps = extract_seeds_and_maps(lines)
    # print(f'seeds: {seeds}')
    # for i, map in enumerate(maps):
        # print(f'--- map {i} --- {map}')
    
    # print('\n--- test ---')
    locations = {}
    for seed in seeds:
        # print(f'start seed: {seed}\n')
        new_mapped_seed = seed
        for i, map in enumerate(maps):
            # print(f'current map: {i}, {map}')
            # print(f'(current seed: {new_mapped_seed})\n-----')
            new_mapped_seed = map_seed(new_mapped_seed, map) 
            # print(f'--> new mapped seed: {new_mapped_seed}\n-----')
        locations[seed] = new_mapped_seed
    # print(f'locations: {locations}')
    lowest_seed, lowest_location = lowest_item_dic(locations)
    print(f'lowest seed: {lowest_seed} with corresponding location: {lowest_location}')

def main05b(file_path):
    lines = extract_lines_from_file(file_path)
    seeds, maps = extract_seeds_and_maps(lines)

    locations = process_seed_ranges(seeds, maps)
    lowest_seed, lowest_location = lowest_item_dic(locations)
    print(f'lowest seed: {lowest_seed} with corresponding location: {lowest_location}')

if __name__ == '__main__':
    print('\n--- example (a & b) ---')
    start_time = time.time()
    main05a(example_path)
    print(f'main05a executed in {round(time.time() - start_time, 5)} seconds')

    start_time = time.time()
    main05b(example_path)
    print(f'main05b executed in {round(time.time() - start_time, 5)} seconds')

    print('\n--- puzzle ---')
    start_time = time.time()
    main05a(puzzle_path)
    print(f'main05a executed in {round(time.time() - start_time, 5)} seconds')

    start_time = time.time()
    main05b(puzzle_path)
    print(f'main05b executed in {round(time.time() - start_time), 5} seconds')