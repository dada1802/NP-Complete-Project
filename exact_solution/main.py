"""
    name: David Nguyen
"""
# import time
import itertools

def check_independent_set(nums, graph):
    colors = len(nums) - 1
    return True


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
    
    n = 2
    num_colors = 1
    check = False
    graph = create_graph(n)
    print(graph)

    # while not check:
    #     nums = []
        
    #     for i in range(num_colors):
    #         nums.append(i)

    #     lst = itertools.product(nums, repeat=n)

    #     for val in lst:
    #         print(val)

    #     num_colors += 1

    # print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()