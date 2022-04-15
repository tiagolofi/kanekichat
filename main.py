
from os import listdir
from json import dumps
from datetime import datetime
from sys import exit
from replit import db

class Annotation(object):
  def __init__(self, user, password):
    self.user = user
    self.password = password
  
  def auth_users(self):
    
    try:

      if db[self.user] == self.password:

        print('Logged as ' + self.user)
        
        return True

      else:

        return False
    
    except:

      return False      
  
  def delete_all_messages(self):

    file = []
    
    db['data'] = []
  
  def write_and_send_messages(self, text, to):

    file = db['data']

    file.append(
      {
        'timestamp': int(datetime.now().timestamp()),
        'from': self.user,
        'to': to,
        'text': text
      }
    )

    db['data'] = file

    return '\nData was saved successfully!\n'

  def my_messages(self):

    file = db['data']
    
    messages = [i.value for i in file if i['to'] == self.user]

    if len(messages) == 0:

      return 'No messages'

    else:
      
      return dumps(messages, indent = 2)

if __name__ == '__main__':
  
  user = str(input('User: '))
  password = str(input('Password: '))

  bdn = Annotation(user = user, password = password)
  
  auth = bdn.auth_users()

  while auth:
  
    command_line = str(input('W (type your message), L (list your messages), Q (quit chat): '))
    
    if command_line == 'W':

      text = str(input('Type your message: '))
      to = str(input('Send to? '))
    
      print(bdn.write_and_send_messages(text = text, to = to))

    elif command_line == 'L':

      print(bdn.my_messages())
    
    elif command_line == 'D':
      
      bdn.delete_all_messages()

    elif command_line == 'Q':

      exit()
    
    else:

      print('Command not found.')
