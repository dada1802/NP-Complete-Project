"""
    name: David Nguyen
"""
import time
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

def create_complete_graph(num_vertices):
    graph = {}

    for i in range(num_vertices):
        graph[i] = set()

    for u in graph:
        for v in graph:
            if u != v:
                graph[u].add(v)
                graph[v].add(u)

    return graph

def main():
    start_time = time.time()
    num_vertices = int(input())
    num_colors = 1
    graph = create_complete_graph(num_vertices)
    check = False
    colors = {}

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

    print(max(nums) + 1)
    for node in colors:
        print(f"{node} {colors[node]}")

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()