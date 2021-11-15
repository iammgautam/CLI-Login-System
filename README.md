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

    
## LICENSE



Copyright 2021 Mithilesh Gautam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
