"""
    name: David Nguyen
"""
# import time
import itertools

def check_independent_set(nums, graph):
    check = True
    colors = {}

    for u in graph:
        colors[u] = None
        if u == 0:
            colors[u] = 0

    for u in graph:
        for v in graph[u]:
            if len(nums) < 2:
                return False, colors

    return check, colors


def create_graph(n):
    graph = {}

    for i in range(n):
        graph[i] = set()

    for u in range(n):
        for v in range(n):
            if u != v:
                graph[u].add(v)

    return graph

def main():
    # start_time = time.time()
    # num_vertices = int(input())

    # for i in range(num_vertices):
    #     graph[i] = set()

    # for _ in range(num_vertices):
    #     x = input().split()
    #     for i in range(1, len(x)):
    #         graph[int(x[i])].add(int(x[0]))
    #         graph[int(x[0])].add(int(x[i]))

    n = 3
    num_colors = 1
    check = False
    graph = create_graph(n)
    print(graph)

    while not check:
        nums = []
        
        for i in range(num_colors):
            nums.append(i)

        lst = itertools.product(nums, repeat=n)

        for val in lst:
            print(val)
        
        num_colors += 1
        print()

        if num_colors == 3:
            check = True

    # print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()