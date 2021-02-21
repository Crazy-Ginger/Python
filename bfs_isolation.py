#!/usr/bin/env python3

def isolated(graph, root):
    visited = set()
    queue = [[root]]
    # to_visit = [root]

    while queue:
        current_path = queue.pop(0)
        current_node = current_path[-1]
        if current_node in visited:
            # print("continuing on: ", current_path, current_node)
            continue

        visited.add(current_node)

        print(current_node)
        print(current_path)
        print()

        if sum(x is None for x in graph[current_node]) == 5 and current_node != root:
            print("Returning on sum: ", current_node, current_path)
            return current_node, current_path

        to_return = True
        for child in graph[current_node]:
            if child and child not in visited:
                # and child not in to_visit
                to_return = False
                # to_visit.append(child)
                tmp_queue = current_path.copy()
                tmp_queue.append(child)
                queue.append(tmp_queue)


        if to_return:
            print("Returning on to_return: ", current_node, current_path)
            return current_node, current_path


def main():
    graph = {"n1": [None, "n4", "n2", "n9", None, None],
             "n2": ["n1", "n5", "n3", None, None, None],
             "n3": ["n2", "n6", None, None, None, None],
             "n4": [None, "n7", "n5", "n1", None, None],
             "n5": ["n4", "n8", "n6", "n2", None, None],
             "n6": ["n5", None, None, "n3", None, None],
             "n7": [None, None, "n8", "n4", None, None],
             "n8": ["n7", None, None, "n5", None, None],
             "n9": [None, "n1", None, None, None, None]}
    for key, val in graph.items():
        print(key, ": ", val)
    isolated(graph, "n9")

if __name__ == "__main__":
    main()
