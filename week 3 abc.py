class person :

 def  _init_(self,n,g,a): 
   self.name=n
   self.gender=g
   self.age=a

 def talk(self):
    print("Hi I'm ", self.name)

    def vote (self):
        if self.age<18 :
            print("I am eligible to vote")
        else :
            print("I am eligible to vote")   

obj1= person("sam","Male",22)  
obj2= person("Jesse","Female",16)  
obj1.talk()
obj1.vote()

obj2.talk()

