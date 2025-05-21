from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from config import Session
from Models.User import User
from Models.Session import Session as TrainingSession
from Models.SessionPlayer import SessionPlayer
from datetime import time, timedelta, datetime



class PlayerController:

    @staticmethod
    def view_joined_sessions(player_id):
        """
        Fetch all TrainingSession entries joined by `player_id`
        and return them in JSON with formatted start/end times.
        """
        db = Session()
        try:
            sessions = (
                db.query(TrainingSession)
                .join(SessionPlayer, SessionPlayer.session_id == TrainingSession.id)
                .filter(SessionPlayer.player_id == player_id)
                .all()
            )

            if not sessions:
                return jsonify({
                    "value": False,
                    "message": "No sessions found for this player"
                }), 404

            session_list = []
            for ts in sessions:
                # assume ts.start_time and ts.end_time are stored as "HH:MM:SS" or similar
                # if they're Python time objects, convert; if strings, pass through
                def fmt(t):
                    if isinstance(t, datetime):
                        return t.strftime("%H:%M:%S")
                    return str(t)

                session_list.append({
                    "session_type": ts.name,
                    "date": ts.date.strftime("%Y-%m-%d") if hasattr(ts.date, "strftime") else str(ts.date),
                    "start_time": fmt(ts.start_time),
                    "end_time": fmt(ts.end_time),
                    "venue": ts.venue
                })

            return jsonify({
                "value": True,
                "sessions": session_list
            }), 200

        except SQLAlchemyError as e:
            return jsonify({
                "value": False,
                "error": str(e)
            }), 500

        finally:
            db.close()
