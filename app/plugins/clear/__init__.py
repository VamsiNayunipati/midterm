import sys
from app.commands import Command
from app.history import History
import logging


class ClearCommand(Command):
    def execute(self):
        dataHistory = History()
        dataHistory.clear()
        print('History is cleared.')
        logging.info('History of the calculator is cleared.')
