#!/bin/bash
# export DATABASE_URL='postgresql://mohammed.latif@localhost:5432/casting'
# export TEST_DATABASE_URL='postgresql://mohammed.latif@localhost:5432/casting_agency_test'
# export ENV='development'

# export FLASK_APP=app
# export FLASK_DEBUG=True

export AUTH0_DOMAIN='hassanlatif.uk.auth0.com'
export API_AUDIENCE='CastingAgencyAPI'
export ALGORITHMS=['RS256']
export FLASK_APP=app
export FLASK_ENV=development
export DATABASE_URL='postgres://mohammed.latif@localhost:5432/postgres'
export ASSISTANT_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNPMTlNbnJwT09YZWhwM0hBb0RfZCJ9.eyJpc3MiOiJodHRwczovL2hhc3NhbmxhdGlmLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGY2MmM4YmMxODU0MWM4NDJjNzJiODQiLCJhdWQiOiJDYXN0aW5nQWdlbmN5QVBJIiwiaWF0IjoxNjk0MDg2MDg0LCJleHAiOjE2OTQwOTMyODQsImF6cCI6Ijc3bmU4REpQSmJKZm9DR1dGc2ZLQWhBYW1Kck1rcDBkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.EIg4nbfZnJc8ZSt5MARSMy4Yrynl4n82NYlco8tPt0H_fOXPFu7Z5sG-ilBZKiw3EoZnC_PX7cqD0wsKLRK6L8P0F88mWAeZziODwbZ-bVP4N3ooRVHd-78x3YitvpCCsRCcgW8JsfLTT_B6NN0LbeBaZuNc9FN8DQcdp_A9IJWSIoa0nfyqxliGBdoFJ9UGW8F-NFX8P0-lN1XfqM-MWAL1Ke3gmjljRMhBpeArXj35p0li6gDdbha30IlkleL4KSXlUUa-n1CGC5Wjhj2sSrMjr4iqJHQGgOPofd68JrbMvVuaY-FA7E438bINQ1sxCbJbdqwQHv-Z2firvhU-1Q'
export PRODUCER_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNPMTlNbnJwT09YZWhwM0hBb0RfZCJ9.eyJpc3MiOiJodHRwczovL2hhc3NhbmxhdGlmLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGY2MmNkYzliNzRiMWVhNTJhMjNiYmEiLCJhdWQiOiJDYXN0aW5nQWdlbmN5QVBJIiwiaWF0IjoxNjk0MDg2MTg0LCJleHAiOjE2OTQwOTMzODQsImF6cCI6Ijc3bmU4REpQSmJKZm9DR1dGc2ZLQWhBYW1Kck1rcDBkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.DI_rbRzPIwncDkDamUT-KdoOq61TunO5YCCck6AgrzEu8a1ILUB7HTUJ8PTCgi0N3NMwf3e_ZgnBPCFdaSBcGDutXut4ZTBO2aWSZ71h3Z2uhtdec_pgmQ13yMM1e5DinOa3veq0GKz1Bf0VER7WawMoN1iGPDag3r0-WmpEcAIh0xrikmfWOzHO8_jdKqLrxAUq9u0reMsjmvL_qeZqnHUlkKjjSK8dKJPQS7ldnxQgnEMkrXBiGygXiD_QN8YcrurEYcRkqIvKuis6mNnEzFaX6x1GGTj1YcVmZs8od-QDIoem7zjBIUPaaVw1KKB697Nit8gUxKExGV8bD4ftsA'
export DIRECTOR_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNPMTlNbnJwT09YZWhwM0hBb0RfZCJ9.eyJpc3MiOiJodHRwczovL2hhc3NhbmxhdGlmLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGY2MmNjNDliNzRiMWVhNTJhMjNiYjkiLCJhdWQiOiJDYXN0aW5nQWdlbmN5QVBJIiwiaWF0IjoxNjk0MDg2MjUwLCJleHAiOjE2OTQwOTM0NTAsImF6cCI6Ijc3bmU4REpQSmJKZm9DR1dGc2ZLQWhBYW1Kck1rcDBkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.QOS0IBZRnGd8QddyhsshbA_6HYYX5YlXfSaPHWR9o9NMoGu4sC63wUHhaJu1MgTZ3Kn27MTtJ48gi7U0C-YFAogr0wz0ua9Uiw3Bzo2kATSTANFFEctUJ10Zi2SJ2a3tLyt9ZlnFV3iICT0h93Tf2fQC85ajBLUnkB3WQodAtA-bb40_Jwfp_KBNASeHmvlMZ3ZcS09-P3HTzI1__khlo3dXiaO5TCqYkQw0ceFpdEh58pA4AE8rG8NyY1d7B00-FYkAlSK-f9dnV3xfwidPutrXXyvIVhcjPXw1ECjXpaGgGm9I4ERn-ro0hTi0gxlG1yQ6dhFER9C7xNlEdzup5w'
echo "setup.sh script executed successfully!"