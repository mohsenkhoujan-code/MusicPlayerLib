import Listener # type: ignore
from Music_Light_Class import Provider,Events # type: ignore

class music_player():
    provider = Provider()
    events = Events()
    path = ""
    event = 0
    occupation = False

    def play(self,path):
        self.path = path
        self.occupation = True
        self.event = self.provider.AttrebDisplay(self.path)
        self.occupation = False
        return self

    def check_error(self):
        if self.provider.is_error():
           return self.provider.error
        else:
            return None 
    def if_event_close(self):
        if(self.event == self.events.close()):
            return True
        return False

    def if_event_next(self):
        if(self.event == self.events.next()):
            return True
        return False

    def if_event_prev(self):
        if(self.event == self.events.prev()):
            return True
        return False

    def if_event_end(self):
        if(self.event == self.events.end()):
            return True
        return False
