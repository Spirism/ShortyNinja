import sqlite3
from flask import Flask, request, flash, redirect, url_for
from flask_restx import Api, Resource, reqparse
from hashids import Hashids
import datetime

from models import *
from db_commands import *


# connects to the database
def get_db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    return conn


# initialises the Flask app
app = Flask(__name__)
# sets the app's secret key for a layer of security
app.config['SECRET_KEY'] = 'fy3g47fgyegfey'
# initialises the api from the Flask app
api = Api(app, doc=False)
# makes hashes with  the secret key as salt
hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])


# api route to shorten urls
@api.route('/api/shorten')
class Shorten(Resource):
    def post(self):
        conn = get_db_conn()

        # creates the 'url' parameter for the post request
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True)
        args = parser.parse_args()

        # gets the url from the request
        url = args['url']

        db_data = insert_url(conn, url)

        url_id = db_data.lastrowid
        hash_id = hashids.encode(url_id)

        short_url = request.host_url + hash_id
        date = str(datetime.datetime.now())

        return shorten_model(short_url, url, date)


# api route to get the stats of a shortened url
@api.route('/api/stats/<id>')
class Stats(Resource):
    def get(self, id):
        conn = get_db_conn()


        url = request.host_url + id

        # gets data from an url
        url_data = get_url_data(conn, id, hashids)

        # gets the json format of the url's data
        stats = stats_model(url, url_data[3], url_data[1], url_data[2])

        return stats


@app.route('/<id>')
def redirect_route(id):
    conn = get_db_conn()
    old_url = find_old_url(conn, id, hashids)

    update_clicks(conn, id, hashids)

    return redirect(old_url)


if __name__ == '__main__':
    app.run(debug=True)
