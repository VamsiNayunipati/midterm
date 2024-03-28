# Midterm Exam - Calculator Project
### Instructions:
1. Create a new git repository.
2. Clone that repository to the local, add all the reequired files and install the dependecncies:  
```pip3 install -r requirements.txt```
3. Create a **.env** file for the environment variable and the path with the name of the file as a key - value pair.
4. Run the **main.py** file using ```python3 main.py```
5. After the successful compilation, we will see option to enter the command which we want to execute. Here we are using arithmetic commands like **Addition, Subtraction, Multiplication and Division** operations.
    ### Sample output(s):
    #### Addition
        >>> addition
        Enter the 1st value: 2
        Enter the 2nd value: 3
        The Operation result is  5.0
        2024-03-27 20:02:29,404 - root - INFO - Addition operation is successful
        >>> addition
        Enter the 1st value: 2
        Enter the 2nd value: e
        please Enter a valid value
        2024-03-27 20:02:36,396 - root - INFO - Operation failed
    #### Subtraction
        >>> subtraction
        Enter the 1st value: 4
        Enter the 2nd value: 4
        The Operation result is  0.0
        2024-03-27 20:02:43,276 - root - INFO - Subtract operation is successful
        >>> subtraction
        Enter the 1st value: 4
        Enter the 2nd value: e
        please Enter a valid value
        2024-03-27 20:02:52,424 - root - INFO - Operation failed
    #### Multiplication
        >>> multiplication
        Enter the 1st value: 7
        Enter the 2nd value: 5
        The Operation result is:  35.0
        2024-03-27 20:03:02,435 - root - INFO - Multiplication operation is successful
        >>> multiplication
        Enter the 1st value: e
        please Enter a valid value
        2024-03-27 20:03:08,729 - root - INFO - Operation failed

    #### Division
        >>> division
        Enter the 1st value: 2
        Enter the 2nd value: 6
        The Operation result is:  0.3333333333333333
        2024-03-27 20:03:14,106 - root - INFO - Division operation is successful
        >>> division
        Enter the 1st value: w
        please Enter a valid value
        2024-03-27 20:03:20,419 - root - INFO - Operation failed

6. Also, there are some other commads like Menu, Fetch, Delete, Clear.
    ### Sample output(s): 
    **Menu** (to see the available commands): 
    ###### 
        >>> menu
        Menu options are: ['addition', 'clear', 'delete', 'division', 'fetch', 'menu', 'multiplication', 'subtraction']

    **Fetch** (to get the previously performed operations history):  
    ######
        >>> fetch
        Calculator history data:
        ID Action Performed  input1  input2
        1         Addition     2.0     3.0
        2      Subtraction     4.0     4.0
        3   Multiplication     7.0     5.0
        4         Division     2.0     6.0
        2024-03-27 20:11:52,117 - root - INFO - Calculator history is fetched: 
        ID Action Performed  input1  input2
        1         Addition     2.0     3.0
        2      Subtraction     4.0     4.0
        3   Multiplication     7.0     5.0
        4         Division     2.0     6.0 
    
    **Delete** (to delete the desired row using rowID): 
    ###### 
        >>> delete
        Enter the ID of the record to delete: 3
        2024-03-27 20:14:50,410 - root - INFO - The History of ID 3 is deleted.
        After delete operation, the history of the calculator is :
        ID Action Performed  input1  input2
        1         Addition     2.0     3.0
        2      Subtraction     4.0     4.0
        3         Division     2.0     6.0  

    **Clear** (to clear all the data):  
    ######
        >>> clear
        History is cleared.
        2024-03-27 20:15:13,154 - root - INFO - History of the calculator is cleared.


### Design Patterns used:
1. **Facade Design Pattern:**  
The _Facade design pattern_ is a structural pattern in software design that provides a simplified interface to a complex subsystem.  

    This [code](https://github.com/VamsiNayunipati/midterm/blob/master/app/history/__init__.py) implements the Facade design pattern by providing a simplified interface to the CSV file. The History class hides the complexity of managing file paths, handling file I/O operations. It provides methods like data_input, fetch_list, fetch_data_frame, and clear that allows users an interface for managing history data, hiding the technical aspects of how it's stored.
2. **Command Design Pattern:**  
The command pattern is a behavioral design pattern in which an object is used to encapsulate all information needed to perform an action or trigger an event. 

    This [code](https://github.com/VamsiNayunipati/midterm/blob/master/app/plugins/addition/__init__.py) implements the Command design pattern by encapsulating the logic for performing an addition operation and storing the history in a separate class - AdditionCommand.
3. **Plugin Design Pattern:**
The Plugin Pattern is a design pattern that allows for the dynamic extension of functionalities within an application without modifying the core code.

    This [code](https://github.com/VamsiNayunipati/midterm/blob/master/app/__init__.py) implements the Plugin pattern to achieve dynamic extension through plugins that provide functionalities implemented as Command subclasses.
4. **Singleton Design Pattern:**
The Singleton pattern is a design pattern that restricts the instantiation of a class to a single object. It ensures that only one instance of a class exists throughout the application, and it provides a global access point to that instance.  

    This [code](https://github.com/VamsiNayunipati/midterm/blob/master/app/__init__.py) implements 
    the singleton design pattern as  
    ```if __name__ == "__main__":``` block, a single instance of the App class is created: ```app = App()```.  
    This instance is then used throughout the application without any attempt to create other instances, ensuring a single instance for core functionalities.

### Environment variables:
Create a **.env** file under the main directory and save the location as a key-value pair.  
> CALCULATOR_PATH = './data/history_of_calculations.csv'


### Logging:

### Easier to Ask for Forgiveness than Permission (EAFP):



### Demonstration video: [Click here]()
