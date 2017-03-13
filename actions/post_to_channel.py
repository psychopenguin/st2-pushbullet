from st2actions.runners.pythonrunner import Action
from pushbullet import Pushbullet


class PostToChannel(Action):
    def run(self):
        pb = Pushbullet('API-KEY')
        channel = pb.channels[1]
        return channel.push_note('hello from st2', 'hi there, this message came from st2. thanks')

