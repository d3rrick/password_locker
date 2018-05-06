# Password Locker Application

## The password locker App allows a user to register his/her credentials and to create multiple accounts for various accounts.
#### By **Derrick** created on, May 5th 2018 

## Description
## This Application is python based and runs on terminal, it allows a user to register his/her credentials and to create multiple accounts eg for facebook,twitter github etc etc, by giving your account name and email and specifying how long you would like your password to be. Afterwards the user can manage all his accounts, creating new ones,deleting,searching and even deleting multiple accounts.

## Behaviour of the application
+ The user run the main file on the terminal >python3 main.py
+ The user is prompted to either, login, register or quite.
+ Based on response, either the user exits the app, or after successful login or registration redirected to accounts management area.
+ While on the account area, the user can choose to either, create a new account, view all the accounts, delete an account or logout.
+ The app exits on users choice to logout.

## Development
### The development cycle of the password locker app.
+ The password locker app is a python terminal based application.
+ Two classes, namely User and Credential are created to create a user and Credential instances.
+ Tests to see the behaviour of these classes is done to ensure they function as expected.
+ The main file ensures the graphical interface logic is maintained and to communicate to the classes via class methods and properties.

### Important packages used in app development.
- **sys** module to allow termination of the app.
- **time** module to allow some time delay before some other action.
- **string** module to have access to all string, numbers and alphanumerics, to allow generation of passwords.
- **random** to allow genration of random passwords.

## Technology Used
+ Python3.6

## Test Driven Development
Testing was done using python inbuild test tool called **unittest**

## Bugs and Development.
### Some additional features to be included in future.
+ Use encryption algorithims to hash passwords rather than randomly generating them.
+ Store user credentials in a database.

## Further help
To get Further help you can visit the official [python](https://www.python.org/) documentation.

## Licence
MIT (c) 2017 [muriithi derrick](https://github.com/muriithiderro)