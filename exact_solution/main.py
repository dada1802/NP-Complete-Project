"""
    name: David Nguyen
"""
# import time
import itertools

def check_independent_set(nums, graph):
    pair = zip(graph, nums)
    colors = {}

    for x in pair:
        colors[x[0]] = x[1]

    for u in graph:
        for v in graph[u]:
            if colors[u] == colors[v]:
                return False, colors, nums
    
    return True, colors, nums

    # for u in graph:
    #     colors[u] = set()
    #     colors[u].add(0)

    # for u in graph:
    #     for v in graph[u]:
    #         highest_u = max(colors[u])
    #         highest_v = max(colors[v])
    #         if highest_u == highest_v:
    #             if (highest_v + 1) <= max(nums):
    #                 colors[v].add(highest_v + 1)

    #                 if (highest_v + 1) not in total_color:
    #                     total_color.add(highest_v + 1)

    #             else:
    #                 return False, colors, total_color

    # return True, colors, total_color

def main():
    # start_time = time.time()
    num_edges = int(input())
    num_colors = 1
    graph = {}
    check = False
    colors = {}
    
    for _ in range(num_edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = set()
        
        if v not in graph:
            graph[v] = set()

        graph[u].add(v)
        graph[v].add(u)

    while not check:
        nums = []
        
        for i in range(num_colors):
            nums.append(i)

        lst = itertools.product(nums, repeat=len(graph))

        for val in lst:
            check, colors, nums = check_independent_set(val, graph)
            if check:
                break

        num_colors += 1

    print()
    print(max(nums) + 1)
    for node in colors:
        print(f"{node} {colors[node]}")

    # print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()