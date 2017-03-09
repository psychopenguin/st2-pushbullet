from st2actions.runners.pythonrunner import Action
from pushbullet import Pushbullet


class BaseAction(Action):
	def __init__(self, config):
		super(BaseAction, self).__init__(config)
		self._apikey = self.config['apikey']
		pb = Pushbullet(self._apikey)

