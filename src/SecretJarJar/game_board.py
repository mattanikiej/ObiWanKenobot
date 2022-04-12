

class GameBoard:
    """
    Class that describes the game board
    """
    def __init__(self, num_players):
        """
        Constructor for the game board
        :param num_players: how many players are in the game
        """
        self.num_players = num_players
        # initialize board to start
        self.board = self.create_board()

    def __str__(self):
        """
        String representation of GameBoard
        :return: string of GameBoard
        """
        space_map = {-1: 'X', 0: ' ', 1: 'ACTION'}
        gb = f"""
        ```
        ---------------------------
        | {'JEDI':^10} | {'SITH':^10} |
        ---------------------------
        | {space_map[self.board[0][0]]:^10} | {space_map[self.board[1][0]]:^10} |
        | {space_map[self.board[0][1]]:^10} | {space_map[self.board[1][1]]:^10} |
        | {space_map[self.board[0][2]]:^10} | {space_map[self.board[1][2]]:^10} |
        | {space_map[self.board[0][3]]:^10} | {space_map[self.board[1][3]]:^10} |
        | {space_map[self.board[0][4]]:^10} | {space_map[self.board[1][4]]:^10} |
        ---------------------------
        | {space_map[self.board[0][5]]:^10} | {space_map[self.board[1][5]]:^10} |
        ---------------------------
        ```
        """
        return gb

    def create_board(self):
        """
        Makes the game board
        with 2 actions per team
        :param num_players: number of players in the game
        :return: empty game board
        """
        jedi_board = [0, 0, 0, 0, 0, 0]
        sith_board = [0, 0, 0, 0, 0, 0]
        if self.num_players < 6:
            # 2 actions per board
            jedi_board[3] = 1
            jedi_board[4] = 1

            sith_board[3] = 1
            sith_board[4] = 1

        elif self.num_players < 9:
            # 3 actions per board
            jedi_board[2] = 1
            jedi_board[3] = 1
            jedi_board[4] = 1

            sith_board[2] = 1
            sith_board[3] = 1
            sith_board[4] = 1

        else:
            # actions on every policy
            for i in range(5):
                jedi_board[i] = 1
                sith_board[i] = 1

        board = [jedi_board, sith_board]
        return board

    def add_policy(self, team):
        """
        Adds policy to the board
        :param team: team to add policy to
        :return: True if there is an action, false otherwise
        """
        t = 0
        if team.lower() == 'sith':
            t = 1

        action = False
        # loops until first empty spot is found
        for i in range(len(self.board[t])):
            if self.board[t][i] != -1:
                if self.board[t][i] == 1:
                    action = True
                self.board[t][i] = -1
                break

        return action
