import logging
from app.commands import Command
from app.history import History

class MultiplicationCommand(Command):
    def execute(self):
        try:
            operations_History = History()
            first_input = float(input("Enter the 1st value: "))
            second_input = float(input("Enter the 2nd value: "))
            result = first_input * second_input
            print('The Operation result is: ', result)
            logging.info('Multiplication operation is successful')
            data = ['Multiplication', first_input, second_input]
            data_History = operations_History.fetch_list()
            data_History.append(data)
            operations_History.data_input(data_History)

        except ValueError:
                print("please Enter a valid value")
                logging.info('Operation failed')