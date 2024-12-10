# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

# Hi! Corbin here. Note the line below says GoslingUtils in the videos.
# DO NOT change the line below. It's no longer compatible with GoslingUtils so we renamed it.
# There are a few places like this where the code that you started with (the code you downloaded) might
# look different than the videos. THAT'S OK! Don't change it. We've made it better over time.
# Just follow along with the videos and it will all work the same.
class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        #set_intent tells the bot what it's trying to do
        if self.get_intent() is not None:
            return
        d1 = (abs(self.ball.location.y - self.foe_goal.location.y))+200
        d2 = abs(self.me.location.y - self.foe_goal.location.y)
        in_front = d1 > d2
        if in_front:
            self.set_intent(goto(self.friend_goal.location))
            return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        if abs(self.foes[0].location.x - self.ball.location.x) > 600 and abs(self.foes[0].location.y - self.ball.location.y) > 600 and d1<1200:
            self.set_intent(goto(self.friend_goal.location))
            if 700>self.ball.location.x>300:
                self.set_intent(atba())
                return   
        if d2<600 and in_front == False:
            self.set_intent(jump_shot(self.ball.location, self.foe_goal.location, 173, 2))
            return
        else: 
            self.set_intent(short_shot(self.foe_goal.location))
            return
        