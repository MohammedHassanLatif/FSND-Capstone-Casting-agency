import os
import json
import jwt
from jose import jwt
from collections.abc import Mapping
from werkzeug.datastructures import ImmutableMultiDict
from flask import Flask, render_template, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import exc

from auth import AuthError, requires_auth
from models import db_drop_and_create_all, setup_db, Movie, Actor


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = 'SECRET'
    setup_db(app)
    CORS(app, resources={"/": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PATCH, PUT, POST,DELETE, OPTIONS')
        return response

    # db_drop_and_create_all()

    # Home
    @app.route('/')
    def index():
        return render_template('index.html')

    # Movie endpoints
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            movies = Movie.query.all()
            return jsonify({
                'success': True,
                'movies': [movie.format() for movie in movies]
            }), 200
        except Exception:
            abort(500)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload):
        data = request.get_json()
        movie = Movie(
            title=data['title'],
            release_date=data['release_date']
        )
        if movie.title == '' or movie.release_date == '':
            abort(422)

        try:
            movie.insert()

            return jsonify({
                'success': True,
                'movie': movie.format()
            }), 200
        except Exception as e:
            print(e)
            abort(500)

    @app.route('/movies/<int:id>', methods=['GET', 'PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, id):
        new_info = request.get_json()
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if movie:
            movie.title = (new_info['title'] if new_info['title']
                           else movie.title)
            movie.release_date = (new_info['release_date'] if
                                  new_info['release_date'] else
                                  movie.release_date)
        else:
            abort(404)
        try:
            movie.update()

            return jsonify({
                'success': True,
                'movie': [movie.format()]
            }), 200
        except Exception:
            abort(500)

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if movie:
            try:
                movie.delete()
                return jsonify({
                    'success': True,
                    'delete': id
                }), 200
            except Exception:
                db.session.rollback()
                abort(500)
        else:
            abort(404)

    # Actor endpoints
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors = Actor.query.all()
            return jsonify({
                'success': True,
                'actors': [actor.format() for actor in actors]
            }), 200
        except Exception:
            abort(500)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload):
        data = request.get_json()
        actor = Actor(
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            movie_id=data['movie_id']
        )
        if actor.name == '' or actor.age == '' or actor.gender == '':
            abort(422)
        try:
            actor.insert()

            return jsonify({
                'success': True,
                'actor': actor.format()
            }), 200
        except Exception:
            abort(500)

    @app.route('/actors/<int:id>', methods=['GET', 'PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, id):
        new_info = request.get_json()
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if actor:
            actor.name = (new_info['name'] if new_info['name']
                          else Actor.name)
            actor.age = (new_info['age'] if new_info['age']
                         else actor.age)
            actor.gender = (new_info['gender'] if new_info['gender']
                            else actor.gender)
            actor.movie_id = (new_info['movie_id'] if new_info['movie_id']
                              else actor.movie_id)
            try:
                actor.update()
                return jsonify({
                    'success': True,
                    'actor': [actor.format()]
                }), 200
            except Exception:
                abort(500)
        else:
            abort(404)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if actor:
            try:
                actor.delete()
                return jsonify({
                    'success': True,
                    'delete': id
                }), 200
            except Exception:
                db.session.rollback()
                abort(500)
        else:
            abort(404)

    # Error Handling
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request, please check your inputs"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found."
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Sorry, there's a problem on our end."
        }), 500

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable. Check your input.'
        }), 422

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "You are not allowed to access this resource",
        }), 403

    @app.errorhandler(AuthError)
    def auth_error(ex):
        res = jsonify(ex.error)
        res.status_code = ex.status_code
        return res

    return app


app = create_app()


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)
