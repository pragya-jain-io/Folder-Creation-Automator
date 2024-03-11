# importing os module   
import os  
    
# Directory  
directory = ["Artificial Intelligence ",
"Artificial Intelligence Lab ",
"Advanced Java Programming ",
"Advanced Java Programming Lab ",
"Universal Human Values ",
"Web Technologies ",
"Web Technologies Lab ",
"Principles of Management for Engineers ",
"Programming in Python ",
"Programming in Python Lab ",
"Statistics, Statistical Modelling & Data Analytics ",
"Statistics, Statistical Modelling & Data Analytics Lab"
]
    
# Parent Directory path  
parent_dir = "C:/Users/User/Desktop/College/6th Semester Subjects"
    

for i in directory:
  
    path = os.path.join(parent_dir, i)  
    os.mkdir(path)  
    print("Directory '% s' created" % i)  
