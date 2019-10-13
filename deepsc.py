class BaseCreature:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def create_sound(self,words):
        if hasattr(self,'speak'):
            return self.speak(words)
        else:
            print(self.sound)
            
          
class HomoSapienCreature(BaseCreature):
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def speak(self,words):
        return " ".join(words)
