class Student():
    def __init__(self,nclass="",age = "",name=""):
        self.name = name
        self.age = age
        self.nclass = nclass
        
    def __str__(self):
        return f"{self.name} has {self.age} years old and the class for him is {self.nclass}"
    def __repr__(self):
        return f"the Student parent class"
    def add(self):
        with open(f"{self.nclass}_class.txt","a") as file:
            file.write(f"{self.name} {self.age} years old\n")
    def exist(self):
        with open(rf"{self.nclass}_class.txt","r") as file:
            data = file.readlines()
            for i in data:
                if self.name in i :
                    return i.strip(r"\n")
            return f"{self.name} not found"
    def remove(self):
        with open(f"{self.nclass}_class.txt","r") as file:
            data = file.readlines()
            ndata = [line for line in  data if self.name not in line]
            if ndata == data:
             return "name not found" 
        with open(f"{self.nclass}_class.txt","w")as file:
            file.writelines(ndata)
            return "Complete"
    def see(self):
        with open(f"{self.nclass}_class.txt","r") as file:
            return file.read()
class Student1_4(Student):
    pass

class Student1_2(Student):
    pass
       
class Student1_3(Student):
    pass
        

class Student1_1(Student):
    pass

        