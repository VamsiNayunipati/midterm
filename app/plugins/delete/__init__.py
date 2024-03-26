import sys
from app.commands import Command
from app.history import History
import logging


class DeleteCommand(Command):
    def execute(self):
        operations_History = History()
        data_History = operations_History.fetch_data_frame()
        record_id = int(input('Enter the ID of the record to delete: '))
        updated_data = data_History[data_History['ID'] != record_id]
        logging.info(f'The History of ID {record_id} is deleted.')
        operations_History.data_input(updated_data.values.tolist())
        print('After delete operation, the history of the calculator is :\n', operations_History.fetch_data_frame().to_string(index=False))
