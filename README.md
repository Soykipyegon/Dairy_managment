## DAIRY

### DAIRY MONITORING AND PRODUCTION SYSTEM

A complete record tracking and production for dairy industries. 

#### Install Instructions

1. Clone the repository:
```shell
git clone https://github.com/Soykipyegon
```

2. Install the requirements:
```shell
sudo pip3 install -r install.txt
```

3. Connecting to database:

In your dairy/settings.py
```shell
DATABASES = {
    'default': {
        'NAME':'my_database', ## This is your database name
        'HOST':' ' ##Hostname , default is '127.0.0.1',
        'USER':'username', ##name of user
        'PASSWORD':' ', 
        'ENGINE': 'django.db.backends.mysql',
    }
}



4. Finally goto the cloned directory and execute:
```shell
python3 manage.py runserver
```

#### Features
1. Record Keeping 
    - Milk Purchase Record
    - Stock Records
    - Product Sales Records
    - Operational Cost Records
2. Easier Report Analysis for desired period
    - Print Report 
    - Convert Report to Excel format

