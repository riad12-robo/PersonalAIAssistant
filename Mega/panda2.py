#here pandas is a class. and Dataframe is a object of this class.
#pandas is a python module used for working with data sets.
#pandas refers as panel data, pyhton data analytics
#most important module for data science

#dictonary used here
import pandas
mydataset = {
    'cars' :["BMW","Toyota","Nissan"],
    'pasing' : [3,7,2]
}

myvar = pandas.DataFrame(mydataset)
print(myvar) 
print(mydataset)