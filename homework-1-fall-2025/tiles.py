from copy import deepcopy


class TilesNode:
    """A class to represent a node in the Fifteen-Tile Puzzle.

    Parameters
    ----------
    state: list[list[int]]
        An array (list of list) of ints representing the initial state of the puzzle.
        This array should contain integers from 0 to 15 separated by spaces.
        The integer 0 represents the empty space in the puzzle.

    parent : Node, optional
        The parent node of the current node. The default is None.
    """

    def __init__(
        self,
        state,
        parent=None,
    ):
        self.state = state
        self.parent = parent

    def is_goal(self) -> bool:
        goalState=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        #since it was mentioned that self.state is "list of list", two dimensional array,
        #you can just write own array that mimics end goal array.
        return self.state==goalState

    def find_empty_space(self) -> tuple[int, int]:
        """Helper function to find the empty space in the current state.

        You don't need to use this function, but it may be helpful.

        Returns
        -------
        empty_row : int
            The row index of the empty space.

        empty_col : int
            The column index of the empty space.
        """
        for i, row in enumerate(self.state):
            for j, col in enumerate(row):
                if col == 0:
                    return i, j

    def swap_tiles(self, row1, col1, row2, col2):
        """
        Helper function to swap two tiles in the current state.

        You don't need to use this function, but it may be helpful.

        """
        new_state = deepcopy(self.state)
        new_state[row1][col1], new_state[row2][col2] = (
            new_state[row2][col2],
            new_state[row1][col1],
        )
        return new_state

    def get_children(self) -> list["TilesNode"]:
    #used to find other possible moves from the current state
        possible_child=[] #list to store all possible next moves
        Erow,Ecol = self.find_empty_space() #row and space to find the empty(0) tile

        move=[(-1,0),(1,0),(0,-1),(0,1)]#lists all potential moves that can be taken

        for r, c in move: #moving along tiles to try all sorts of moves
            Nrow= Erow+r #new row of the empty space
            Ncol= Ecol+c #new col of the empty space

            if 0<=Nrow<4:#ensures that row/col do not go out of bounds
                if 0<=Ncol<4:
                    Nstate=self.swap_tiles(Erow, Ecol, Nrow, Ncol)
                    #new state = swap new empty coordinates with older ones
                    child_node=TilesNode(Nstate, parent=self)
                    #want to create the new TilesNode obj that knows this new state
                    possible_child.append(child_node)
                    #add to the possible_child list, to recheck the process
        return possible_child



    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.state)

    def __repr__(self) -> str:
        return self.__str__()

    def get_path(self) -> list["TilesNode"]:
        """
        Once a goal node is found, this function can be used to backtrack.

        Be sure to set .parent correctly when creating child nodes for this to work.

        You don't need to use this function, but it may be helpful.
        """
        path = []
        current_node = self
        while current_node:
            path.append(current_node)
            current_node = current_node.parent
        return path[::-1]

    def __eq__(self, other):
        if isinstance(other, TilesNode):
            return self.state == other.state
        return False

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))
