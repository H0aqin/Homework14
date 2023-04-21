class Player:
    def __init__(self):
        self.current_time = 0
        self.quality = '480p'
        self.playing = False
        self.last_pause_time = 0
   def play(self, address):
       if self.playing:
           print("Media file is already playing")
           return False
       else:
           self.playing = True
           print("Playing media file at", address)
           return True

       def pause(self):
           if self.playing:
               self.playing = False
               self.last_pause_time = self.current_time
               print("Media file paused")
           else:
               print("Media file is not playing")

       def save_last_time(self):
           print("Current time saved as last pause time:", self.current_time)

       def change_quality(self, quality):
           self.quality = quality
           print("Quality changed to", self.quality)