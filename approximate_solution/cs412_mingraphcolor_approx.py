"""
    Name: Christopher Simmons
"""


def dsatur(graph):
    """

    Pseudocode:

    1. Initialize a dictionary colors to store the color assigned to each vertex in the graph, where initially each vertex is uncolored
    2. Initialize a dictionary saturation_degrees to store the saturation degree of each vertex in the graph, where initially each vertex has saturation degree 0
    3. Define a helper function find_max_saturation_degree to find the vertex with the highest saturation degree that is uncolored
    4. Find the vertex with the maximum degree in the graph, and color it with color 1
    5. Update the saturation degrees of all neighbors of the vertex colored in step 4 to be 1
    6. While there are still uncolored vertices in the graph:
        a. Find the uncolored vertex with the highest saturation degree by calling the find_max_saturation_degree helper function
        b. Assign the smallest available color to the vertex found in step 6a, where available colors are those that are not used by any of the neighbors of the vertex
        c. Update the color assigned to the vertex found in step 6a to the color assigned in step 6b
        d. Update the saturation degrees of all neighbors of the vertex colored in step 6c to be 1
    7. Return the dictionary colors with the assigned colors for each vertex
    """
    # Initialize color and saturation degree dictionaries for each vertex
    colors = {vertex: None for vertex in graph}
    saturation_degrees = {vertex: 0 for vertex in graph}

    # Helper function to find the vertex with maximum saturation degree
    def find_max_saturation_degree():
        max_degree = -1
        max_saturation_degree = -1
        max_vertex = None
        for vertex, neighbors in graph.items():
            if colors[vertex] is None:
                saturation_degree = len(
                    {colors[neighbor] for neighbor in neighbors if colors[neighbor] is not None})
                if saturation_degree > max_saturation_degree or (saturation_degree == max_saturation_degree and len(neighbors) > max_degree):
                    max_degree = len(neighbors)
                    max_saturation_degree = saturation_degree
                    max_vertex = vertex
        return max_vertex

    # Color the vertex with maximum degree (step 4)
    max_degree_vertex = max(graph, key=lambda vertex: len(graph[vertex]))
    colors[max_degree_vertex] = 1

    # Update saturation degrees for all neighbors of the maximum degree vertex (step 6)
    for neighbor in graph[max_degree_vertex]:
        saturation_degrees[neighbor] += 1

    # Color the remaining vertices (step 7)
    while None in colors.values():
        # Find the uncolored vertex with maximum saturation degree (step 7a-7c)
        max_saturation_degree_vertex = find_max_saturation_degree()
        # Assign the smallest available color to the vertex (step 7c)
        available_colors = set(range(1, len(graph)+1)) - {
            colors[neighbor] for neighbor in graph[max_saturation_degree_vertex] if colors[neighbor] is not None}
        colors[max_saturation_degree_vertex] = min(available_colors)
        # Update saturation degrees for all neighbors of the newly colored vertex (step 7d)
        for neighbor in graph[max_saturation_degree_vertex]:
            saturation_degrees[neighbor] += 1

    return colors


def rlf():
    """
    Recursive Largest First

    Pseudocode:

    """
    pass


def rlf_random():
    """
    Recursive Largest First using random selection.

    Pseudocode:

    """
    pass


def main():
    """
    Driving code used to generate comparative examples between the two algorithms.
    """

    # TO-DO: Convert this patch main method to work with its own test cases like a shell script

    num_edges = int(input())
    graph = {}

    for _ in range(num_edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = set()

        if v not in graph:
            graph[v] = set()

        graph[u].add(v)
        graph[v].add(u)

    print(graph)
    print(dsatur(graph))


if __name__ == "__main__":
    main()
