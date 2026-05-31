class RemoteControl():
    def __init__(self):
        self.channels = ['CN', 'DisneyXD', 'PoGO', 'Nickelodeon']
        self.index = -1 #off

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index +=1
        if self.index == len(self.channels):
            raise StopIteration
        
        return self.channels[self.index]
    

print("OG Channels: \n")
r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))