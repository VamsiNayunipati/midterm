import sys
from app.commands import Command
from app.history import History
import logging


class FetchCommand(Command):
    def execute(self):
        operations_History = History()
        calculator_data = operations_History.fetch_data_frame().to_string(index=False)
        print('Calculator history data:\n', calculator_data)
        logging.info('Calculator history is fetched: \n%s', calculator_data)
