from pages.main_menu import mainmenu
from backend.classes.Repository import Repository
from pages.login import *
from pages.register import *
from pages.search import *
from utils.cursors import CursorON

repository = Repository()

CursorON(False)
print('\033[48;5;233m')
mainmenu(repository)