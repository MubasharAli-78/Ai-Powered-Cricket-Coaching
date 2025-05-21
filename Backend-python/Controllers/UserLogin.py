from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from config import Session
from Models.User import User


class UserLoginController:

    @staticmethod
    def sign_in():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"value": False, "message": "Username and password are required"}), 400

        session = Session()
        try:
            user = session.query(User).filter_by(username=username, password=password).first()

            if user:
                if user.role in ["manager", "coach", "player"]:
                    return jsonify({
                        "value": True,
                        "message": f"Login successful as {user.role}",
                        "role": user.role,
                        "id":user.id
                    }), 200
                else:
                    return jsonify({"value": False, "message": "Invalid role"}), 403
            else:
                return jsonify({"value": False, "message": "Invalid username or password"}), 401

        except SQLAlchemyError as e:
            return jsonify({"value": False, "error": str(e)}), 500

        finally:
            session.close()
