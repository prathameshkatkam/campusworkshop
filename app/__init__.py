"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa3de7avj5o488n2sg-a.oregon-postgres.render.com",
        database="todo_z1s0",
        user="todo_z1s0_user",
        password="FLommZSKwr3eVrfkgVlRAMWYkt031qUQ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
