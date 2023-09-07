# Full Stack Casting Agency API Backend

## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Motivation for project

This is the capstone project of Udacity fullstack nanodegree program, which demonstrate the skillset of using Flask, SQLAlchemy, Auth0, gunicorn and heroku to develop and deploy a RESTful API. 

## Getting Started

### Installing Dependencies

#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
psql casting_agency<casting_agency.psql
```

more info here:
https://www.linode.com/docs/databases/postgresql/how-to-back-up-your-postgresql-database/#:~:text=PostgreSQL%20provides%20the%20pg_dump%20utility,you%20intend%20to%20back%20up.&text=Dump%20the%20contents%20of%20a,database%20to%20be%20backed%20up.

## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```zsh
. ./setup.sh
flask run
```

#### Flask run tests the token headers set for the enviroment. If they have expired, you need to login using the crededntials below and replace them in setup.sh and run setup.sh again

setup.sh has all the environment variables needed for the project. The app may fail if they are not set properly. If that happens just copy paste lines from setup.sh on you CLI.

# Project deployed at
https://udacitycapstone-casting-131b527c73e3.herokuapp.com/

###### To test live APIs the only way right now to do this is curl requests. Add Auth token headers from logins below to test.

OATH login url. There are three logins atm, JWTs for these appear in the url after successfull login. Those tokens are needed to test the different APIs.

https://hassanlatif.uk.auth0.com/authorize?audience=CastingAgencyAPI&response_type=token&client_id=77ne8DJPJbJfoCGWFsfKAhAamJrMkp0d&redirect_uri=http://localhost:8080/

casting Assistant token castingassistant@udacity.com udacity123!

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNPMTlNbnJwT09YZWhwM0hBb0RfZCJ9.eyJpc3MiOiJodHRwczovL2hhc3NhbmxhdGlmLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGY2MmM4YmMxODU0MWM4NDJjNzJiODQiLCJhdWQiOiJDYXN0aW5nQWdlbmN5QVBJIiwiaWF0IjoxNjk0MDAwNjUwLCJleHAiOjE2OTQwMDc4NTAsImF6cCI6Ijc3bmU4REpQSmJKZm9DR1dGc2ZLQWhBYW1Kck1rcDBkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.XFdHW15vZa5V1zPNyMeLun5W_RTaWZKbKVY69r-8xQG6Wxm1sK3lF35VeInrA7dAuXdiy8G5r0X0sc_2RN7cLPO9bWE-SaAmXs_iEpZmG_zo1mVrhhYLbYO4gHBVP1-25XGR7ExwDI_NtHSsROau0nIxUyK4xo-v7Ayp7eNF61ABD-sauEcxFrDYNMZsFf69a0q8PV5JrQhilM2DtC7RypSUz5P6Li2X-2WqeGb10Pyjog3i04JP4wfWliS88H6WcfKUaddnUNkZasR2z5YSz0FQYB2XiqPdxEhYyCiqayhmdSLu8gFBJGmoLS_Ke1_j4ZOtVYZxtv4CDM5bfXv0cg

```

Casting director token castingdirector@udacity.com udacity123!

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNPMTlNbnJwT09YZWhwM0hBb0RfZCJ9.eyJpc3MiOiJodHRwczovL2hhc3NhbmxhdGlmLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGY2MmNjNDliNzRiMWVhNTJhMjNiYjkiLCJhdWQiOiJDYXN0aW5nQWdlbmN5QVBJIiwiaWF0IjoxNjk0MDAwODI5LCJleHAiOjE2OTQwMDgwMjksImF6cCI6Ijc3bmU4REpQSmJKZm9DR1dGc2ZLQWhBYW1Kck1rcDBkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.KnlPhyXrkxAFAL8bHISxXAtolE6RhI_fA9iGkPd6NUeQovePUYNA9nEDgmxdD1gzku_DKcAete1K4dt7In5m71daQ2pV9VKGtckw6qgyjkDCa821CuE_ZtmEwUCXFMbdMNeX-Nx5OpCGD51qCW-eOLD4cJ6rgrM4YHNrBlga3Zb2jJe1AF9COwhjyL8aYI6mbGO7XfCSwW4ICzkMizFO9M1CUmzBKdrVyXui8LNmcrZrf4m1WTSNFavb8gmT9R0eE63M64dhUnwzCgidpCOiwrt88hsyweCHfklwFpvpA4B2gqfBhfL8dQeub-WBNsQvKtOKBRByhkwhGazR1kpVZw

```

Executive Producer executiveproducer@udacity.com udacity123!

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJWRXNSUnYwWUZRUDdtU3g5VGJ0TSJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYzM0eTlscS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyMjRkNGQ1Yzg0OGYwMDM3YzQxNzFkIiwiYXVkIjoiQ2FzdGluZ0FnZW5jeUFQSSIsImlhdCI6MTU5NjE0MTUwNCwiZXhwIjoxNTk2MjI3OTAzLCJhenAiOiJYZXF3T3U2UHNBZUMwYndtMmRkNmdpTlAwSkphYXhJZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImFkZDptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.BgIe6xAaR5YqxM7j0NFjjLLctZnAKIp2x_q93sZPH8rBkCp3HjSDRLlqmz0KyeEwPyBMjLxQabbr3InJQk8OTq8S7rjoepgPs_zHF3mJrjUqZ3V3JaRX5_IvDf5J_-PfV-I6vxz42q1Mb1wMTBOHxOxj7MvtZ0JSycNGy3aRg1h0RsslV1Zyrcsx5cWk6xstpBylBEhaOTwbqHQTWZklWDE2eRnRAC3YYWrHpIy_xepcn8HNxfBoIFWr11SYxGMkYXEMqRDbQ8UqnUcUpOzxqMJXG913cf9YZegljhEiyZwPtsdlW92KNLNYKkLEPbTPXBwEQl_UmsD769fKc_egvA
```

## Testing

To run the tests, run

```
dropdb casting_agency_test
createdb casting_agency_test
psql casting_agency_test<casting_agency.psql
python3 test_flaskr.py
```

The tests print data returned from the APIs along with API logs.

#### The rests also use the Auth token set in env variables and will give an error if the tokens are expired.

## API Reference

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}

```

### Endpoints

GET '/actors'
POST '/actors'
PATCH '/actors/<actor_id>'
DELETE '/actors/<actor_id>'
GET '/movies'
GET '/actors'
POST '/actors'
PATCH '/actors/<actor_id>'
DELETE '/actors/<actor_id>'

GET '/movies'
Fetches an array of movies
Required URL Arguments: None
Required Data Arguments: None
Returns: Returns Json data about movies
Success Response:

```
{
   "movies":[
      {
         "id":3,
         "release_date":"2008-07-24",
         "title":"he Dark Knight"
      },
      {
         "id":6,
         "title":"The Dark Knight"
         "release_date":"2008-07-24",
      }
   ],
   "success":True
}
```

GET '/actors'
Fetches an array of actors
Required Data Arguments: None
Returns: Json data about actors
Success Response:

```
  {
   "actors":[
      {
         "id":3,
         "name":"Timothée Chalamet"
         "age":24,
         "gender":'M',
         "movie_id": 6,
      }
   ],
   "success":True
}
```

DELETE '/movies/<int:movie_id>'
Deletes the movie_id of movie
Required URL Arguments: movie_id: movie_id_integer
Required Data Arguments: None
Returns: deleted movie's ID
Success Response:

```
{'deleted': 3, 'success': True}
```

DELETE '/actors/<int:actor_id>'
Deletes the actor_id of actor
Required URL Arguments: actor_id: actor_id_integer
Required Data Arguments: None
Returns:the deleted actor's ID
Success Response:

```
{'deleted': 6, 'success': True}
```

POST '/movies'
Post a new movie in a database.
Required URL Arguments: None
Required Data Arguments: Json data
Success Response:

```
{'movie_id': 21, 'success': True}
```

POST '/actors'
Post a new actor in a database.

Required URL Arguments: None

Required Data Arguments: Json data

Success Response:

```
{'actor_id': 7, 'success': True}
```

PATCH '/movies/<int:movie_id>'
Updates the movie_id of movie
Required URL Arguments: movie_id: movie_id_integer
Required Data Arguments: None
Returns: Json data about the updated movie
Success Response:

```
{
   "movie":{
      "id":5,
      "title":"The Dark Knight Rises"
      "release_date":"2012-07-20",
   },
   "success":True
}
```

PATCH '/actors/<int:actor_id>'
Updates the actor_id of actor
Required URL Arguments: actor_id: actor_id_integer
Required Data Arguments: None
Returns: Json data about the modified actor's ID
Success Response:

```
{
   "actor":{
      "id":4,
      "name":"Christian Bale",
      "age":49,
      "gender":"M",
      "movie_id": 6
   },
   "success":True
}
```

## Authors

Hassan Latif and The udacity team that made the starter code and Project tasks.

The image of the homepage used in this project is contributed to Alex Litvin on Unsplash
