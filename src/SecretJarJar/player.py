class Player:
    """
    Class that describes a player in secret jarjar
    """
    def __init__(self, name):
        """
        Constructor for players for secret jarjar
        :param name: name of the player
        """
        self.name = name
        self.role = ''
        self.team = ''
        self.master = False
        self.apprentice = False

    def get_name(self):
        """
        Gets the name of the player
        :return:
        """
        return self.name

    def set_name(self, name):
        """
        Sets the name of the player
        :param name: name to set the player's name to
        """
        self.name = name

    def get_role(self):
        """
        Gets the role of the player
        :return:
        """
        return self.role

    def set_role(self, role):
        """
        Sets the role of the player
        :param role: role to set the player's role to
        """
        self.role = role

    def get_team(self):
        """
        Gets the team of the player
        :return:
        """
        return self.team

    def set_team(self, team):
        """
        Sets the team of the player
        :param team: team to set the player's team to
        """
        self.team = team

    def set_master(self, master):
        """
        Sets the master of the player
        :param master: master to set the player's master to
        """
        self.master = master

    def set_apprentice(self, apprentice):
        """
        Sets the apprentice of the player
        :param apprentice: apprentice to set the player's apprentice to
        """
        self.apprentice = apprentice
