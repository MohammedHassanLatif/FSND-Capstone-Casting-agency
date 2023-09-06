import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, db


assistant_token = os.environ.get('ASSISTANT_TOKEN')
director_token = os.environ.get('DIRECTOR_TOKEN')
producer_token = os.environ.get('PRODUCER_TOKEN')


class MainTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    One test for success behavior of each endpoint
    One test for error behavior of each endpoint
    """

    # MOVIES
    def test_home_page(self):
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

    def test_post_movie(self):
        new_movie = {
            'title': 'The Dark Knight',
            'release_date': '2008-07-24'
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(producer_token)
        }
        res = self.client().post('/movies', json=new_movie, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_missing_post_movie_info(self):
        new_movie = {
            'title': '',
            'release_date': '2017-01-01'
        }
        auth = {
            'Authorization': "Bearer {}".format(producer_token)
        }
        res = self.client().post('/movies', json=new_movie, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_patch_movie(self):
        edit_movie = {
            'title': '',
            'release_date': '2020-11-01'
        }
        auth = {
            'Authorization': "Bearer {}".format(director_token)
        }
        res = self.client().patch('/movies/3', json=edit_movie,
                                  headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_404_patch_movie_not_found(self):
        edit_movie = {
            'title': 'testing',
            'release_date': '2020-11-01'
        }
        auth = {
            'Authorization': "Bearer {}".format(director_token) 
        }
        res = self.client().patch('/movies/100', json=edit_movie, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_movies(self):
        auth = {
            'Authorization': "Bearer {}".format(assistant_token)
        }
        res = self.client().get('/movies', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_401_unauth_get_movies(self):
        res = self.client().get('/movies', headers='')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

    def test_delete_movie(self):
        auth = {
            'Authorization': "Bearer {}".format(producer_token)
        }
        res = self.client().delete('/movies/2', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 2)

    def test_404_delete_movie_not_found(self):
        auth = {
            'Authorization': "Bearer {}".format(producer_token)
        }
        res = self.client().delete('/movies/100', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    # Actors
    def test_post_actor(self):
        new_actor = {
            'name': 'Timothée Chalamet',
            'age': 24,
            'gender': 'M',
            'movie_id': 6
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(director_token)
        }
        res = self.client().post('/actors', json=new_actor, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_missing_post_actor_info(self):
        new_actor = {
            'name': 'TEST',
            'age': '',
            'gender': 'M',
            'movie_id': 1
        }
        auth = {
            'Authorization': "Bearer {}".format(director_token)
        }
        res = self.client().post('/actors', json=new_actor, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_patch_actor(self):
        edit_actor = {
            'name': '',
            'age': 88,
            'gender': '',
            'movie_id': ''
        }
        auth = {
            'Authorization': "Bearer {}".format(director_token)
        }
        res = self.client().patch('/actors/3', json=edit_actor,
                                  headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_404_patch_actor_not_found(self):
        edit_actor = {
            'name': '',
            'age': 88,
            'gender': '',
            'movie_id': ''
        }
        auth = {
            'Authorization': "Bearer {}".format(director_token)
        }
        res = self.client().patch('/actors/1000', json=edit_actor,
                                  headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_actors(self):
        auth = {
            'Authorization': "Bearer {}".format(assistant_token)
        }
        res = self.client().get('/actors', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_401_unauth_get_actors(self):
        res = self.client().get('/actors', headers='')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

    def test_delete_actor(self):
        auth = {
            'Authorization': "Bearer {}".format(director_token)
        }
        res = self.client().delete('/actors/2', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 2)

    def test_404_delete_actor_not_found(self):
        auth = {
            'Authorization': "Bearer {}".format(director_token)
        }
        res = self.client().delete('/actors/1000', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    # AUTH Test Cases
    def test_401_invalid_header_view_movie(self):
        auth = {
            'Authorization': "Token {}".format(assistant_token)
        }
        res = self.client().get('/actors', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'invalid_header')

    def test_401_invalid_token_view_actor(self):
        auth = {
            'Authorization': "Bearer{}".format(assistant_token)
        }
        res = self.client().get('/actors', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'invalid_header')

    def test_403_unauth_add_actor(self):
        new_actor = {
            'name': 'Linda Chen',
            'age': 24,
            'gender': 'F',
            'movie_id': 1
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(assistant_token)
        }
        res = self.client().post('/actors', json=new_actor, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['message'],
                         'You are not allowed to access this resource')

    def test_403_unauth_modify_movie(self):
        edit_movie = {
            'title': '',
            'release_date': '2020-11-11'
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(assistant_token)
        }
        res = self.client().patch('/movies/4', json=edit_movie,
                                  headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['message'],
                         'You are not allowed to access this resource')

    def test_403_unauth_delete_movie(self):
        auth = {
            'Authorization': "Bearer {}".format(director_token)
            }
        res = self.client().delete('/movies/6', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['message'],
                         'You are not allowed to access this resource')

    def test_403_unauth_add_movie(self):
        new_movie = {
            'title': 'To test',
            'release_date': '2017-10-20'
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(director_token)
            }
        res = self.client().post('/movies', json=new_movie, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['message'],
                         'You are not allowed to access this resource')