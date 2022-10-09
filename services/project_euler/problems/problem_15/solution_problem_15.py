def problem_15():
    grid_size = 20

    # paths = [[0 for i in range(grid_size+1)] for j in range(grid_size+1)]
    # paths[grid_size][grid_size] = 1

    # queue = [(grid_size, grid_size)]

    # while queue:
    #     current = queue.pop(0)

    #     if current[0] - 1 >= 0:
    #         if (current[0] - 1, current[1]) not in queue:
    #             queue.append((current[0] - 1, current[1]))
    #         paths[current[0] - 1][current[1]] += paths[current[0]][current[1]]

    #     if current[1] - 1 >= 0:
    #         if (current[0], current[1] - 1) not in queue:
    #             queue.append((current[0], current[1] - 1))
    #         paths[current[0]][current[1] - 1] += paths[current[0]][current[1]]

    # return paths[0][0]

    n = grid_size * 2
    k = grid_size

    import math

    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))