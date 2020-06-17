__author__ = "DGOAT"

from menu import Menu
from models.blog import Blog
from database import Database

Database.initialize()

menu = Menu()

menu.run_menu()