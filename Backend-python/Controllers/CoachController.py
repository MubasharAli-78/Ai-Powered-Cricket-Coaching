from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from config import Session
from Models.User import User
from Models.Session import Session as TrainingSession
from Models.SessionPlayer import SessionPlayer
from Models.TeamPlayer import TeamPlayer
from Models.TeamCoach import TeamCoach
from datetime import time, timedelta, datetime

class CoachController:




    # @staticmethod
    # def arrange_session():
    #     session = Session()
    #     try:
    #         data = request.json
    #         name = data.get('name')
    #         date = data.get('date')
    #         start_time = data.get('start_time')
    #         end_time = data.get('end_time')
    #         venue = data.get('venue')
    #         coach_id = data.get('coach_id')
    #         player_id = data.get('player_id')
    #
    #         if not all([name, date, start_time,end_time, venue, coach_id, player_id]):
    #             return jsonify({"value": False,
    #                             "message": "All fields (name, date, time, venue, coach_id, player_ids) are required"}), 400
    #
    #         coach = session.query(User).filter_by(id=coach_id, role='coach').first()
    #         if not coach:
    #             return jsonify({"value": False, "message": "Coach not found"}), 404
    #
    #         players = session.query(User).filter(User.id.in_(player_id), User.role == 'player').all()
    #         if len(players) != len(player_id):
    #             return jsonify({"value": False, "message": "One or more players not found"}), 404
    #
    #         existing_session = session.query(TrainingSession).filter_by(
    #             name=name, date=date, start_time=start_time,end_time=end_time, venue=venue, coach_id=coach_id
    #         ).first()
    #
    #         if existing_session:
    #             return jsonify({"value": False, "message": "Session already exists"}), 400
    #
    #         training_session = TrainingSession(name=name, date=date, start_time=start_time,end_time=end_time, venue=venue, coach_id=coach_id)
    #         session.add(training_session)
    #         session.commit()
    #
    #         for player_id in player_id:
    #             session_player = SessionPlayer(session_id=training_session.id, player_id=player_id)
    #             session.add(session_player)
    #
    #         session.commit()
    #
    #         return jsonify({"value": True, "message": "Session arranged successfully"}), 200
    #
    #     except SQLAlchemyError as e:
    #         session.rollback()
    #         return jsonify({"value": False, "error": str(e)}), 500
    #
    #     finally:
    #         session.close()
    @staticmethod
    def arrange_session():
        session = Session()
        try:
            data = request.json
            name = data.get('name')
            date = data.get('date')
            start_time = data.get('start_time')
            end_time = data.get('end_time')
            venue = data.get('venue')
            coach_id = data.get('coach_id')
            player_id = data.get('player_id')  # expecting a single player ID

            if not all([name, date, start_time, end_time, venue, coach_id, player_id]):
                return jsonify({"value": False,
                                "message": "All fields (name, date, time, venue, coach_id, player_id) are required"}), 400

            coach = session.query(User).filter_by(id=coach_id, role='coach').first()
            if not coach:
                return jsonify({"value": False, "message": "Coach not found"}), 404

            player = session.query(User).filter_by(id=player_id, role='player').first()
            if not player:
                return jsonify({"value": False, "message": "Player not found"}), 404

            existing_session = session.query(TrainingSession).filter_by(
                name=name, date=date, start_time=start_time, end_time=end_time, venue=venue, coach_id=coach_id).first()


            if existing_session:
                return jsonify({"value": False, "message": "Session already exists"}), 400

            training_session = TrainingSession(
                name=name,
                date=date,
                start_time=start_time,
                end_time=end_time,
                venue=venue,
                coach_id=coach_id
            )
            session.add(training_session)
            session.commit()

            session_player = SessionPlayer(session_id=training_session.id, player_id=player_id)
            session.add(session_player)
            session.commit()

            return jsonify({"value": True, "message": "Session arranged successfully"}), 200

        except SQLAlchemyError as e:
            session.rollback()
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()

    @staticmethod
    def view_arranged_sessions(coach_id):
        session = Session()
        try:
            # Fetch all training sessions arranged by the coach
            sessions = session.query(TrainingSession).filter_by(coach_id=coach_id).all()
            session_list = []

            for training_session in sessions:
                # Fetch the single associated player from SessionPlayer
                player_obj = session.query(User).join(SessionPlayer, SessionPlayer.player_id == User.id).filter(
                    SessionPlayer.session_id == training_session.id
                ).first()
                player_name = player_obj.name if player_obj else None

                session_list.append({
                    "session_type": training_session.name,
                    "date": training_session.date,  # Assuming date is stored as a string
                    "start_time": training_session.start_time,
                    "end_time": training_session.end_time,
                    "venue": training_session.venue,
                    "player": player_name
                })

            return jsonify({"value": True, "sessions": session_list}), 200

        except SQLAlchemyError as e:
            session.rollback()
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()



    @staticmethod
    def view_team(coach_id):
        session = Session()
        try:
            team_coach = session.query(TeamCoach).filter_by(coach_id=coach_id).first()

            if not team_coach:
                return jsonify({"value": False, "message": "No team found for this coach"}), 404

            team = team_coach.team


            player_count = session.query(TeamPlayer).filter_by(team_id=team.id).count()


            coach_name = team_coach.user.name

            team_info = {
                "team_name": team.name,
                "number_of_players": player_count,
                "coach": coach_name
            }

            return jsonify({
                "value": True,
                "team": team_info
            }), 200

        except SQLAlchemyError as e:
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()

    @staticmethod
    def view_team_players(coach_id):
        session = Session()
        try:
            # Check if coach exists in the User table with role 'coach'
            coach = session.query(User).filter_by(id=coach_id, role='coach').first()
            if not coach:
                return jsonify({"value": False, "message": "Coach not found"}), 404

            # Check if the coach has a team assigned (is_team_assigned should be '1')
            if coach.is_team_assigned == '0':
                return jsonify({"value": False, "message": "Coach does not have a team assigned"}), 400

            # Retrieve team details from TeamCoach table using the coach_id
            team_coach = session.query(TeamCoach).filter_by(coach_id=coach_id).first()
            if not team_coach:
                return jsonify({"value": False, "message": "No team associated with coach"}), 404

            team_id = team_coach.team_id

            # Retrieve players from TeamPlayer table for the given team
            team_players = session.query(TeamPlayer).filter_by(team_id=team_id).all()
            if not team_players:
                return jsonify({"value": False, "message": "No players found for this team"}), 404

            # Only return the list of player names
            player_list = []
            for team_player in team_players:
                # Fetch player details from User table, filtering by role 'player'
                player = session.query(User).filter_by(id=team_player.player_id, role='player').first()
                if player:
                    player_list.append({"id": player.id, "name": player.name,"date_of_birth": player.date_of_birth,"experience":player.experience, "type": player.type,"is_active": player.is_active})


            return jsonify({"value": True, "players": player_list}), 200

        except SQLAlchemyError as e:
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()