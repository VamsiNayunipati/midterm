# Midterm Exam - Calculator Project
### Instructions:
1. Create a new git repository.
2. Clone that repository to the local, add all the reequired files and install the dependecncies:  
``` pip3 install requirements.txt```
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


### Design Patterns used


### Environment variables

### Logging

### "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP)


### Demonstration video: [Click here]()
