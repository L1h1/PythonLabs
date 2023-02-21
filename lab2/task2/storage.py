import os
import re


class Storage:
    
    data = dict()
    cur_user = None
    
    
    def add(self, key_args):
        for element in key_args:
            self.data[self.cur_user].add(element)
        
    
    def remove(self, key):
        if key in self.data[self.cur_user]:
            self.data[self.cur_user].remove(key)
            print(f"Item {key} removed from container {self.cur_user}")
        else:
            print(f"Item not found in {self.cur_user}")


    def find(self, keys):
        got_item=False
        for key in keys:
            if key in self.data[self.cur_user]:
                print(key)
                got_item=True
        if not got_item:
            print("No items found")        


    def lst(self):
        print(f"Contents of container {self.cur_user}:")
        for element in self.data[self.cur_user]:
            print(element)


    def grep(self, filter:str):
        try:
            got_item=False
            for element in self.data[self.cur_user]:
                if re.match(filter,element):
                    print(element)
                    got_item=True
            
            if not got_item:
                print("No matches found")
        except re.error:
            print("Incorrect regex input")


    def save(self):
        with open (f"{self.cur_user}.txt",'w') as file:
            for element in self.data[self.cur_user]:
                file.write(element+' ')
        print(f"Data saved to {self.cur_user}.txt")


    def load(self):
        if not os.path.exists(f"{self.cur_user}.txt"):
            print("No such file in directory.")
            return

        with open (f"{self.cur_user}.txt",'r') as file:
            for element in file.readline().split():
                self.data[self.cur_user].add(element)
        print(f"Container for user {self.cur_user} loaded")     


    def switch(self, username:str):
        if self.cur_user != None:
            if input("Save current container (y/n)?: ") == 'y':
                self.save()

        self.cur_user=username

        if not self.cur_user in self.data.keys():
            self.data[self.cur_user]=set()

        print(f"Switched to {self.cur_user}")

        if input("Load the container (y/n)?: ")=='y':
            self.load()    

    