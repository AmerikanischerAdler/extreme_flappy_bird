# Extreme Flappy Bird

## Description

A Flappy Bird game with levels and missions

### Stack:

| Type  | Structure | Style | Elements   | Routes  | Database |
| :---: | :-------: | :---: | :--------: | :-----: | :------: |
| Flask | HTML5     | CSS3  | JavaScript | Python3 | MYSQL    |

## Installation

1) Open Terminal and Clone Repository:

```bash
git clone https://github.com/AmerikanischerAdler/extreme_flappy_bird
```

2) Install Python:

If python3 is not installed on your machine, run:

**MacOS:**

```bash
brew update 
brew install python3
``` 

**TIP**: For MacOS, be sure that homebrew is installed on your machine. If not, visit https://brew.sh to install.

**Ubuntu:**

```bash
sudo apt update 
sudo apt install python3
```

3) Set Up Virtual Environment:

```bash
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
```

4) Install Dependencies:

```bash
pip install -r requirements.txt
```

5) Terminate Virtual Environment:

```bash 
deactivate
```

6) Set Up MYSQL Environment Variable:

Once you have created your MYSQL account, run this command in the terminal, substituting your own password for "my_password":

```bash
echo 'export MYSQLPW="my_password"' >> ~/.bashrc
```

Do the same to set up your own secret key, substituting its value for "my_secret_key":

```bash
echo 'export SECRET_KEY="my_secret_key"' >> ~/.bashrc
```

**TIP**: This implies that you are using bash as your current shell. If not, run
the command, substituting your own shell config file for ".bashrc"

7) Create MYSQL Database and Tables:

Once you are logged into your MYSQL environment, run the following commands:

*Create ExFlappyBird Database:*

```mysql
CREATE DATABASE ExFlappyBird;
```

*Create Users Table:*

```mysql
USE ExFlappyBird;
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT, 
    email VARCHAR(255), 
    username VARCHAR(255), 
    password VARCHAR(255)
);
```

## Usage 

Coming Soon!

## Inspiration

Coming Soon!

