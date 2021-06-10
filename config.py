from huey import RedisHuey,crontab


huey = RedisHuey('demo', host='127.0.0.1', port=6379, max_connections=5)

class Record:
  def __init__(self, userId, count,state):
    self.userId = userId
    self.count = count
    self.state = state
