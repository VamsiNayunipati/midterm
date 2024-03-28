import logging
from app.commands import Command
from app.history import History

class AdditionCommand(Command):
    def execute(self):
        try:
            operations_History = History()
            first_input = float(input("Enter the 1st value: "))
            second_input = float(input("Enter the 2nd value: "))
            result = first_input + second_input
            print('The Operation result is', result)
            logging.info('Addition operation is successful')
            data = ['Addition', first_input, second_input]
            data_History = operations_History.fetch_list()
            data_History.append(data)
            operations_History.data_input(data_History)

        except ValueError:
                print("please Enter a valid value")
                logging.info('Operation failed')
