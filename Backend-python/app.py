from flask import Flask, request, jsonify
from Controllers.UserLogin import UserLoginController
from Controllers.ManagerController import ManagerController
from Controllers.CoachController import CoachController
from Controllers.PlayerController import PlayerController

app = Flask(__name__)





@app.route("/login", methods=["POST"])
def login():
    return UserLoginController.sign_in()


@app.route('/manager/add_coach', methods=['POST'])
def add_coach():
    return ManagerController.add_coach()

@app.route('/manager/appoint_coach', methods=['GET'])
def appoint_coach():
    return ManagerController.appoint_coaches()


@app.route('/manager/assign_player', methods=['GET'])
def assign_player():
    return ManagerController.assign_players()

@app.route('/manager/add_team', methods=['POST'])
def add_team():
    return ManagerController.add_team()

@app.route('/manager/add_player', methods=['POST'])
def add_player():
    return ManagerController.add_player()


@app.route('/manager/view_coaches', methods=['GET'])
def view_coaches():
    return ManagerController.view_coaches()


@app.route('/manager/view_teams', methods=['GET'])
def view_teams():
    return ManagerController.view_teams()

@app.route('/manager/view_players', methods=['GET'])
def view_players():
    return ManagerController.view_players()


@app.route('/manager/view_team/<int:manager_id>', methods=['GET'])
def view_team(manager_id):
    return ManagerController.view_team(manager_id)


@app.route('/manager/view_team_players/<int:team_id>', methods=['GET'])
def view_team_players(team_id):
    return ManagerController.view_team_players(team_id)






@app.route('/coach/arrange_session', methods=['POST'])
def arrange_session():
    return CoachController.arrange_session()

@app.route('/coach/view_arranged_sessions/<int:coach_id>', methods=['GET'])
def view_sessions(coach_id):
    return CoachController.view_arranged_sessions(coach_id)



@app.route('/coach/view_team/<int:coach_id>', methods=['GET'])
def view_team_coach(coach_id):
    return CoachController.view_team(coach_id)


@app.route('/coach/view_team_players/<int:coach_id>', methods=['GET'])
def view_coach_team_players(coach_id):
    return CoachController.view_team_players(coach_id)



@app.route('/player/view_joined_sessions/<int:player_id>', methods=['GET'])
def view_player_joined_sessions(player_id):
    return PlayerController.view_joined_sessions(player_id)



if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0" ,port=5000)
