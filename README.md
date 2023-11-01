# ✓  User Authentication System - Documentation

## Introduction

This Python program is a simple user authentication system that allows users to create credentials (login and password) and later use them for login purposes. The program stores the user's credentials in a file named "belle.txt" using a simple text-based format.

## How to Use

1. Run the program in your preferred Python environment.
2. The program will prompt you to choose between "Cadastro" (sign up) and "Loguin" (login).

### Sign Up (Cadastro)

1. Select option 1 or enter "Cadastro" (case-insensitive).
2. Enter a unique "Loguin" (login) and "Senha" (password).
3. Confirm the password by entering it again. If the passwords do not match, you will be asked to re-enter the password until they match.
4. The program will store the credentials in the "belle.txt" file and display the created credentials.

### Login (Loguin)

1. Select option 2 or enter "Loguin" (case-insensitive).
2. Enter your registered "Loguin" and "Senha" (password).
3. If the provided credentials match any previously registered credentials, the program will display a login confirmation message.
4. If the credentials do not match any stored credentials, the program will prompt you to try again or proceed to the sign-up process.

## Program Logic

- The program consists of several functions:
  1. `menu()`: This function displays the main menu with options to retry or exit the program after login or sign-up.
  2. `cad()`: This function handles the user sign-up process by taking user inputs for login and password, confirming the password, and storing the credentials in the "belle.txt" file.
  3. `log()`: This function handles the user login process by taking user inputs for login and password, checking if the provided credentials match any registered credentials, and displaying appropriate messages.
  4. `add(log, pess)`: This function appends new user credentials (login and password) to the "belle.txt" file.
  5. `read(ind_log, ind_pess)`: This function reads the "belle.txt" file and checks if the provided login and password match any stored credentials.
  6. `main()`: This is the main function that controls the flow of the program. It prompts the user to choose between sign-up and login, calls the corresponding functions, and then displays the main menu.

## File Format

The user credentials are stored in a text file named "belle.txt" in the following format:

```
Login:{user_login}
Senha:{user_password}
```

## Example Usage

```
O que deseja fazer?
1-Cadastro
2-Login
1
Loguin:belle
Senha:123
Confirme a senha:
123

Suas credenciais são:['belle', '123']
O que quer fazer agora?
1-Tentar Novamente
2-Sair
```

## Note

- This is a simple demonstration of a user authentication system for educational purposes and may not have robust security features.
- The password is displayed in plain text when you create credentials for demonstration purposes only. In a real-world scenario, passwords should be stored securely, such as through encryption and hashing.
- The program does not have additional features such as password strength validation or account recovery mechanisms. In a real-world application, those would be important considerations.
