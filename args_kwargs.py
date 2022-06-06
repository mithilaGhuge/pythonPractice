#args and kwargs 
def my_func(*args, **kwargs):
    print("args:",args)
    print("kwargs:",kwargs)

my_func(1,2,x=1)

#*act as args
#** act as kward arguments
def sec_func(a,b,*temp,**temp2):
    print("a:",a)
    print("b:",b)
    print("args:",temp)
    print("kwargs:",temp2)
    


sec_func(1,2,4,"hi",5.8,True,{"x":5},[1,2,3,4,"hi"],c=10)