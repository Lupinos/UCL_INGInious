def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)

1
    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    # TODO
    dim = len(adj_mat)
    adj_list = []
    for index in range(0, dim):
        curNodeVisited = [];
        curNodeTargets = adj_mat[index];
        for target in range(0, dim):
            if curNodeTargets[target] == 1:
                curNodeVisited.append(target);
        adj_list.append(curNodeVisited);
    return adj_list

def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    # I think it's pretty easy with a BFS
    nodeVisited = set(adj_list[start_node])
    nodeToBeIterated = list(adj_list[start_node])

    curIteratedIndex = 0;
    while curIteratedIndex < len(nodeToBeIterated):
        curNode = nodeToBeIterated[curIteratedIndex];
        curNodeTargets = adj_list[curNode]
        if len(curNodeTargets) > 0:
            for node in curNodeTargets:
                if node not in nodeVisited:
                    nodeVisited.add(node)
                    nodeToBeIterated.append(node)
        curIteratedIndex += 1
    return nodeVisited