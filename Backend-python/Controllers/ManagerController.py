# from flask import jsonify,request
# from sqlalchemy.exc import SQLAlchemyError
# from config import Session
# from Models.Team import Team
# from Models.TeamManager import TeamManager
# from Models.TeamPlayer import TeamPlayer
# from Models.TeamCoach import TeamCoach
# from Models.User import User
#
# class ManagerController:
#
#     @staticmethod
#     def view_team(manager_id):
#         session = Session()
#         try:
#             team_manager = session.query(TeamManager).filter_by(manager_id=manager_id).first()
#
#             if not team_manager:
#                 return jsonify({"value": False, "message": "No team found for this manager"}), 404
#
#             team = team_manager.team
#
#
#             player_count = session.query(TeamPlayer).filter_by(team_id=team.id).count()
#
#
#             coach = session.query(TeamCoach).filter_by(team_id=team.id).first()
#             coach_name = coach.user.name if coach else None
#
#             team_info = {
#                 "team_name": team.name,
#                 "number_of_players": player_count,
#                 "coach": coach_name
#             }
#
#             return jsonify({
#                 "value": True,
#                 "team": team_info
#             }), 200
#
#         except SQLAlchemyError as e:
#             return jsonify({"value": False, "error": str(e)}), 500
#
#         finally:
#             session.close()
#
#     @staticmethod
#     def view_team_players(team_id):
#         session = Session()
#         try:
#             team_players = session.query(TeamPlayer).filter_by(team_id=team_id).all()
#
#             if not team_players:
#                 return jsonify({"value": False, "message": "No players found for this team"}), 404
#
#             player_list = []
#             for team_player in team_players:
#                 player = session.query(User).filter_by(id=team_player.user_id, role='player').first()
#                 if player:
#                     player_info = {
#                         "name": player.name,
#                         "age": player.age,
#                         "experience": player.experience,
#                         "type": player.type,
#                         "status": player.status
#                     }
#                     player_list.append(player_info)
#
#             return jsonify({
#                 "value": True,
#                 "players": player_list
#             }), 200
#
#         except SQLAlchemyError as e:
#             return jsonify({"value": False, "error": str(e)}), 500
#
#         finally:
#             session.close()
#
#     @staticmethod
#     def appoint_coach():
#         session = Session()
#         try:
#             data = request.json
#             team_id = data.get('team_id')
#             coach_id = data.get('coach_id')
#
#             if not team_id or not coach_id:
#                 return jsonify({"value": False, "message": "Team ID and Coach ID are required"}), 400
#
#             existing_coach = session.query(TeamCoach).filter_by(coach_id=coach_id).first()
#             if existing_coach:
#                 return jsonify({"value": False, "message": "Coach is already assigned to another team"}), 400
#
#             coach = session.query(User).filter_by(id=coach_id, role='coach').first()
#             if not coach:
#                 return jsonify({"value": False, "message": "Coach not found"}), 404
#
#             new_appointment = TeamCoach(team_id=team_id, coach_id=coach_id)
#             session.add(new_appointment)
#             session.commit()
#
#             return jsonify({"value": True, "message": "Coach successfully appointed to the team"}), 200
#
#         except SQLAlchemyError as e:
#             session.rollback()
#             return jsonify({"value": False, "error": str(e)}), 500
#
#         finally:
#             session.close()



#################################################



from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from Models.TeamCoach import TeamCoach
from config import Session
from Models.User import User
from Models.Team import Team
from Models.TeamPlayer import TeamPlayer
from Models.TeamManager import TeamManager


class ManagerController:

    @staticmethod
    def add_coach():
        data = request.get_json()

        name = data.get('name')
        date_of_birth = data.get('date_of_birth')
        experience = data.get('experience')
        contact_no = data.get('contact_no')
        username = data.get('username')
        password = data.get('password')

        if not name or not date_of_birth or not experience or not contact_no or not username or not password:
            return jsonify({"value": False, "message": "All fields are required"}), 400

        if not isinstance(experience, int):
            return jsonify({"value": False, "message": "experience must be integers"}), 400

        session = Session()
        try:
            # Check if the coach already exists
            existing_coach = session.query(User).filter_by(username=username, role='coach').first()
            if existing_coach:
                return jsonify({"value": False, "message": "Coach already exists"}), 400

            new_coach = User(
                name=name,
                role='coach',
                date_of_birth=date_of_birth,
                experience=experience,
                contact_no=contact_no,
                username=username,
                password=password
            )

            session.add(new_coach)
            session.commit()

            return jsonify({
                "value": True,
                "message": "Coach added successfully",
                "coach_id": new_coach.id
            }), 201

        except SQLAlchemyError as e:
            session.rollback()
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()

    # @staticmethod
    # def add_team():
    #     data = request.get_json()
    #     team_name = data.get('name').strip() if data.get('name') else None
    #     coach_identifier = data.get('coach').strip() if data.get('coach') else None
    #     players_list = data.get('player')  # expecting a list of player names
    #
    #     # Validate required fields and number of players in request
    #     if not team_name:
    #         return jsonify({"value": False, "message": "Team name is required"}), 400
    #     if not coach_identifier:
    #         return jsonify({"value": False, "message": "A coach must be appointed"}), 400
    #     if not players_list or len(players_list) < 1:
    #         return jsonify({"value": False, "message": "At least one player is required"}), 400
    #     if len(players_list) > 15:
    #         return jsonify({"value": False, "message": "A maximum of 15 players is allowed"}), 400
    #
    #     session = Session()
    #     try:
    #         # Check if team already exists
    #         existing_team = session.query(Team).filter_by(name=team_name).first()
    #
    #         # Branch if team exists: add players to existing team
    #         if existing_team:
    #             team = existing_team
    #
    #             # Validate each player's existence and build a list of player objects
    #             player_objects = []
    #             for player_name in players_list:
    #                 player_name = player_name.strip()
    #                 player = session.query(User).filter_by(name=player_name, role='player').first()
    #                 if not player:
    #                     return jsonify({"value": False, "message": f"Player '{player_name}' not found"}), 400
    #                 player_objects.append(player)
    #
    #             # Check how many players are already assigned to this team
    #             current_player_count = session.query(TeamPlayer).filter_by(team_id=team.id).count()
    #             new_players = []
    #             for player in player_objects:
    #                 # Add only if the player is not already in the team
    #                 if not session.query(TeamPlayer).filter_by(team_id=team.id, user_id=player.id).first():
    #                     new_players.append(player)
    #
    #             if current_player_count + len(new_players) > 15:
    #                 return jsonify({"value": False,
    #                                 "message": "Adding these players exceeds the maximum limit of 15 players"}), 400
    #
    #             # Process each new player
    #             for player in new_players:
    #                 team_player = TeamPlayer(team_id=team.id, user_id=player.id)
    #                 session.add(team_player)
    #                 player.status = 'active'
    #             session.commit()
    #
    #             return jsonify({
    #                 "value": True,
    #                 "message": "More players are added to the team successfully",
    #                 "team_id": team.id,
    #                 "players": players_list
    #             }), 200
    #
    #         # Else branch: Team does not exist, so create a new team along with coach and players.
    #         else:
    #             # Validate coach existence using ID (frontend sends coach ID)
    #             try:
    #                 coach_name = coach_identifier
    #             except ValueError:
    #                 return jsonify({"value": False, "message": "Invalid coach identifier"}), 400
    #
    #             coach = session.query(User).filter_by(name=coach_name, role='coach').first()
    #             if not coach:
    #                 return jsonify({"value": False, "message": "Coach not found"}), 400
    #
    #             # Validate each player's existence and build a list of player objects
    #             player_objects = []
    #             for player_name in players_list:
    #                 player_name = player_name.strip()
    #                 player = session.query(User).filter_by(name=player_name, role='player').first()
    #                 if not player:
    #                     return jsonify({"value": False, "message": f"Player '{player_name}' not found"}), 400
    #                 player_objects.append(player)
    #
    #             # Create new team record
    #             new_team = Team(name=team_name)
    #             session.add(new_team)
    #             session.flush()  # Flush to get new_team.id before associations
    #
    #             # Associate the coach with the team
    #             existing_coach = session.query(TeamCoach).filter_by(coach_id=coach.id).first()
    #             if not existing_coach:
    #                 team_coach = TeamCoach(team_id=new_team.id, coach_id=coach.id)
    #                 session.add(team_coach)
    #             coach.status = 'active'
    #
    #             # Process each player
    #             for player in player_objects:
    #                 existing_team_player = session.query(TeamPlayer).filter_by(user_id=player.id).first()
    #                 if not existing_team_player:
    #                     team_player = TeamPlayer(team_id=new_team.id, user_id=player.id)
    #                     session.add(team_player)
    #                 player.status = 'active'
    #
    #             session.commit()
    #
    #             return jsonify({
    #                 "value": True,
    #                 "message": "Team, coach, and players updated successfully",
    #                 "team_id": new_team.id,
    #                 "coach_id": coach.id,
    #                 "players": players_list
    #             }), 201
    #
    #     except SQLAlchemyError as e:
    #         session.rollback()
    #         return jsonify({"value": False, "error": str(e)}), 500
    #
    #     finally:
    #         session.close()

    @staticmethod
    def add_team():
        data = request.get_json()
        team_name = data.get('name').strip() if data.get('name') else None
        coach_identifier = data.get('coach').strip() if data.get('coach') else None
        players_list = data.get('player')  # expecting a list of player names

        # Validate required fields and number of players in request
        if not team_name:
            return jsonify({"value": False, "message": "Team name is required"}), 400
        if not coach_identifier:
            return jsonify({"value": False, "message": "A coach must be appointed"}), 400
        if not players_list or len(players_list) < 1:
            return jsonify({"value": False, "message": "At least one player is required"}), 400
        if len(players_list) > 15:
            return jsonify({"value": False, "message": "A maximum of 15 players is allowed"}), 400

        session = Session()
        try:
            # Check if team already exists
            existing_team = session.query(Team).filter_by(name=team_name).first()

            # Branch if team exists: add players to existing team
            if existing_team:
                team = existing_team

                # Validate each player's existence and build a list of player objects
                player_objects = []
                for player_name in players_list:
                    player_name = player_name.strip()
                    player = session.query(User).filter_by(name=player_name, role='player').first()
                    if not player:
                        return jsonify({"value": False, "message": f"Player '{player_name}' not found"}), 400
                    player_objects.append(player)

                # Check how many players are already assigned to this team
                current_player_count = session.query(TeamPlayer).filter_by(team_id=team.id).count()
                new_players = []
                for player in player_objects:
                    # Add only if the player is not already in the team
                    if not session.query(TeamPlayer).filter_by(team_id=team.id, user_id=player.id).first():
                        new_players.append(player)

                if current_player_count + len(new_players) > 15:
                    return jsonify({"value": False,
                                    "message": "Adding these players exceeds the maximum limit of 15 players"}), 400

                # Process each new player
                for player in new_players:
                    team_player = TeamPlayer(team_id=team.id, user_id=player.id)
                    session.add(team_player)
                    player.is_active = '1'
                    player.is_team_assigned='1'
                session.commit()

                return jsonify({
                    "value": True,
                    "message": "More players are added to the team successfully",
                    "team_id": team.id,
                    "players": players_list
                }), 200

            # Else branch: Team does not exist, so create a new team along with coach and players.
            else:
                # Validate coach existence using ID (frontend sends coach ID)
                try:
                    coach_name = coach_identifier
                except ValueError:
                    return jsonify({"value": False, "message": "Invalid coach identifier"}), 400

                coach = session.query(User).filter_by(name=coach_name, role='coach').first()
                print(coach)
                if not coach:
                    return jsonify({"value": False, "message": "Coach not found"}), 400

                if coach.is_team_assigned == '1':
                    return jsonify({"value": False, "message": "Coach is already assigned to a team"}), 400

                # Validate each player's existence and build a list of player objects
                player_objects = []
                for player_name in players_list:
                    player_name = player_name.strip()
                    player = session.query(User).filter_by(name=player_name, role='player').first()
                    if not player:
                        return jsonify({"value": False, "message": f"Player '{player_name}' not found"}), 400
                    player_objects.append(player)

                # Create new team record
                new_team = Team(name=team_name)
                session.add(new_team)
                session.flush()  # Flush to get new_team.id before associations

                # Associate the coach with the team
                team_coach = TeamCoach(team_id=new_team.id, coach_id=coach.id)
                session.add(team_coach)
                coach.is_active ='1'
                coach.is_team_assigned = '1'

                # Process each player
                for player in player_objects:
                    existing_team_player = session.query(TeamPlayer).filter_by(player_id=player.id).first()
                    if not existing_team_player:
                        team_player = TeamPlayer(team_id=new_team.id, player_id=player.id)
                        session.add(team_player)
                    player.is_active = '1'
                    player.is_team_assigned='1'

                session.commit()

                return jsonify({
                    "value": True,
                    "message": "Team, coach, and players updated successfully",
                    "team_id": new_team.id,
                    "coach_id": coach.id,
                    "players": players_list
                }), 201

        except SQLAlchemyError as e:
            session.rollback()
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()
    @staticmethod
    def add_player():
        data = request.get_json()
        name = data.get('name')
        date_of_birth = data.get('date_of_birth')
        experience = data.get('experience')
        contact_no = data.get('contact_no')
        type_ = data.get('type')
        username = data.get('username')
        password = data.get('password')

        if not all([name, date_of_birth, experience, contact_no, type_, username, password]):
            return jsonify({"value": False, "message": "All fields are required"}), 400

        session = Session()
        try:
            # Check if the player already exists
            existing_player = session.query(User).filter_by(username=username, role="player").first()
            if existing_player:
                return jsonify({
                    "value": False,
                    "message": "Player already exists"
                }), 400

            new_player = User(
                name=name,
                date_of_birth=date_of_birth,
                experience=experience,
                contact_no=contact_no,
                type=type_,
                username=username,
                password=password,
                role="player"
            )
            session.add(new_player)
            session.commit()

            return jsonify({
                "value": True,
                "message": "Player created and added to the Pool",
                "player_id": new_player.id
            }), 201

        except SQLAlchemyError as e:
            session.rollback()
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()

    @staticmethod
    def view_coaches():
        session = Session()
        try:
            coaches = session.query(User).filter_by(role='coach').all()

            if not coaches:
                return jsonify({"value": False, "message": "No coaches found"}), 404

            coach_list = []
            for coach in coaches:
                coach_info ={
                    "name": coach.name,
                    "date_of_birth": coach.date_of_birth,
                    "experience": coach.experience,
                    "contact_no":coach.contact_no
                     }
                coach_list.append(coach_info)

            return jsonify({
                "value": True,
                "coaches": coach_list
            }), 200

        except Exception as e:
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()

    @staticmethod
    def view_teams():
        session = Session()
        try:
            teams = session.query(Team).all()

            if not teams:
                return jsonify({"value": False, "message": "No teams found"}), 404

            team_list = []
            for team in teams:
                team_info = {
                    "team_name": team.name,
                    "number_of_players": len(team.team_Player),
                }

                team_coach = session.query(TeamCoach).filter_by(team_id=team.id).first()
                if team_coach:
                    team_coach = session.query(User).filter_by(id=team_coach.coach_id).first()
                    team_info["coach"] = team_coach.name if team_coach else "No coach"

                team_list.append(team_info)

            return jsonify({
                "value": True,
                "teams": team_list
            }), 200

        except Exception as e:
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()

    @staticmethod
    def view_players():
        session = Session()
        try:
            players = session.query(User).filter_by(role='player').all()

            if not players:
                return jsonify({"value": False, "message": "No players found"}), 404

            player_list = []
            for player in players:
                player_info = {
                    "name": player.name,
                    "date_of_birth": player.date_of_birth,
                    "experience": player.experience,
                    "type": player.type,
                    "status": player.status
                }
                player_list.append(player_info)

            return jsonify({
                "value": True,
                "players": player_list
            }), 200

        except Exception as e:
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()

    @staticmethod
    def appoint_coaches():
        session = Session()
        try:
            # Get all coaches from the User table
            all_coaches = session.query(User).filter(User.role == "coach").all()

            # Get assigned coaches from the TeamCoach table
            assigned_coaches = session.query(TeamCoach.coach_id).distinct().all()
            assigned_coach_ids = {coach.coach_id for coach in assigned_coaches}

            # Filter unappointed coaches
            unappointed_coaches = [coach for coach in all_coaches if coach.id not in assigned_coach_ids]

            return jsonify({
                "value": True,
                "message": "Unappointed coaches retrieved successfully",
                "coaches": [{"id": coach.id, "name": coach.name} for coach in unappointed_coaches]
            }), 200
        except SQLAlchemyError as e:
            session.rollback()
            return jsonify({"value": False, "error": str(e)}), 500
        finally:
            session.close()

    @staticmethod
    def assign_players():
        session = Session()
        try:
            # Get all players from the User table
            all_players = session.query(User).filter(User.role == "player").all()

            # Get assigned players from the TeamPlayer table
            assigned_players = session.query(TeamPlayer.player_id).distinct().all()
            assigned_player_ids = {player.player_id for player in assigned_players}

            # Filter unassigned players
            unassigned_players = [player for player in all_players if player.id not in assigned_player_ids]

            return jsonify({
                "value": True,
                "message": "Unassigned players retrieved successfully",
                "players": [{"id": player.id, "name": player.name} for player in unassigned_players]
            }), 200
        except SQLAlchemyError as e:
            session.rollback()
            return jsonify({"value": False, "error": str(e)}), 500
        finally:
            session.close()
