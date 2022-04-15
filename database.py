
from replit import db
from json import dumps

def my_keys():

  print(db.keys())

def add_new_user(user, pwd):

  db[user] = pwd

  return print('New user added.')

def data():

  print(
    db['data'].value
  )

my_keys()

# add_new_user(user = 'otheruser', pwd = 'notadmin1234')

data()
