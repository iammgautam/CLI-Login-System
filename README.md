[![Python version](https://img.shields.io/badge/Python-3.8-green?style=flat&logo=python)](https://docs.python.org/3.8/)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/zengboi/CLI-Login-System/blob/main/LICENSE)

# CLI Login System

A Command Line Interface Login System in Python. 


## Description

Enter your username and password to register or login to account. 
Automatically stores the entered account in its textfile. 
The account details stored in the textfile are encrypted format and
the given input password is hidden from the terminal for security purpose.
When you want to login again, you can enter without any problems. 
If you try to login when you don't have an account, it will give you an error message. 
If you already have an account, it will give a successfully login message.

## Libraries

- Bcrypt
- Getpass

## Deployment

To deploy this project run

```bash
 git clone https://github.com/zengboi/CLI-Login-System.git
 cd CLI-Login-System
 python3 -m venv your_virtualenv_name
 source ./your_virtualenv_name/bin/activate
 pip install -r requirements.txt
 python3 login.py
```
