from tiles import TilesNode
from queue import PriorityQueue


def heuristic(node: TilesNode) -> int:
    """
    Evaluate the heuristic value of the current node.
    This implementation simply counts the number of misplaced tiles.

    Returns
    -------
    heuristic_value : int
        The heuristic value of the current node.
    """
    dist =0

    for i in range(4):
        for j in range (4):
            t = node.state[i][j]
            if t==0: continue

            row_end=(t-1)//4
            col_end=(t-1)%4

            dist=dist+abs(i-row_end)+abs(j-col_end)
    return dist

def AStar(root, heuristic: callable) -> TilesNode or None:  # type: ignore
    unexplored = PriorityQueue()
    counter = 0
    unexplored.put((0, counter, root))
    # HINT: PriorityQueue.put() takes a tuple as input
    # To sort the queue items, it uses the first element of each tuple
    # If the first elements are equal, it uses the second element, and so on
    # You may implement a counter to resolve ties
    explored = set()
    g_score = {root: 0}
    f_score = {root: heuristic(root)}

    while not unexplored.empty():
        raise NotImplementedError(
            "Implement the rest of this function as part of the assignment."
        )

    return None  # return None if no path was found
