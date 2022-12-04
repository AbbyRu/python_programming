def user_info(name,age = 25,city = "Mombasa"):
    '''This function prints name,age and city from an argument provided to the function'''
    print("{} is {} years old, from {}".format(name,age,city))


user_info("Abigael", 22,"Nairobi City")
user_info("Ruon")
user_info(age= 58, name= "Myra")

def application(fname,lname,email,company,*args,**kwargs):
    print("{} {} works at {}.Her email is {}.".format(fname,lname,company,email))


application("Jess","Ingrass","mail@mail.com","Fintech",75000,hire_date="Sep 2010")