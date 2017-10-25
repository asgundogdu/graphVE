import grapher
import time


# coding=utf-8
# f_name = "input.txt"
f_name = "input.txt"  # Name of the file to be processed


# noinspection PyPep8Naming
def control_input(inputList):
    # noinspection PyBroadException
    try:
        inputList = [tuple(map(str, i)) for i in inputList]  # convert to integer
    except Exception:
        raise ValueError('Parameter should be string')
    return inputList


def reverse_graph(inputs, unique_names):
    new_nodes = [e[::-1] for e in inputs]  # get each edge and reverse direction
    G = grapher.Graph()
    G.add_vertices(unique_names)
    G.add_edges(new_nodes)
    return G


def main():
    # noinspection PyBroadException
    try:
        with open(f_name) as f:
            content = f.readlines()
        # remove whitespace characters like `\n` at the end of each line and split from backspace
        content = [x.strip().split() for x in content]
        content = content[1:]  # To remove 1st line in input file
    except:
        print "File is not exist!"

    edge_list = control_input(content)

    all_v = [(i[0]) for i in content] + [(i[1]) for i in content]
    unique_names = sorted(set(all_v))

    # Introduce graph G
    g = grapher.Graph()
    g.add_vertices(unique_names)
    g.add_edges(edge_list)

    # [g.control_add_edge(x) for x in content]    # O(V+E)
    print "nodes added to G!"

    # Introduce graph G_reverse
    g_reverse = reverse_graph(content, unique_names)  # O(V+E)
    print "G-reverse was introduced!"

    print "------- Function get_finishTimes too see the order -------"

    # Strongly Connected Component
    start_time_ = time.time()
    visited_nodes = []
    finishes = []
    g.get_finishTimes(visited_nodes, finishes)  # O(V+E)
    # print "Visited Nodes: " + str(visited_nodes)

    print "------- Strongly Connected Component get_scc ------------"
    visited_nodes = []
    scc = []
    g_reverse.get_scc(visited_nodes, finishes, scc)
    print("------- %s seconds for the Algorithm -----" % (time.time() - start_time_))

    # Writing to the file
    with open('components.txt', 'w') as f:
        for c in scc:
            f.write("Component" + '\n')
            for _string in c:
                f.write(str(_string) + '\n')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("------- %s seconds for whole processes -----" % (time.time() - start_time))




