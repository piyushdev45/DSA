class FootballTeam:

    def __init__(self, name):
        self.name = name
        self.goals = 0

    def score_goal(self):
        self.goals += 1

    def show_score(self):
        print(self.name, "Goals:", self.goals)


team1 = FootballTeam("Barcelona")
team2 = FootballTeam("Real Madrid")

team1.score_goal()
team1.score_goal()
team2.score_goal()

team1.show_score()
team2.show_score()