#student_grades={9.1, 8.8, 7.5}

#the fact that python doesn't have a min function, we create one
 
def mean(mylist):       # define        nameFunction(parameters):
    the_mean=sum((mylist)/len(mylist))
    return the_mean

print(mean([1,4,6]))