#1.	Define a vector named x.  x should contain the values 2, 4, 6 and 8.
x <- c(2,4,6,8) # is equivalent to x = c(2,4,6,8)

#2.	Compute the mean and standard deviation of x.
mean(x)
sd(x)

#3.	Return the 4th element of x (sub setting).
x[4]

#4.	Return elements 3 and 4 of x.
x[3:4]

#Read data from file

#Check that you have the appropriate working directory. (getwd())
getwd()

#Use the read.table() function to read in the data.  Call the dataset baseball and include headers.
baseball <- read.table("baseball2011.txt",header=T)

#1.	Look at your data set by calling the variable baseball.
baseball # use View(baseball) for a better view of the data

#2.	Look at the dimensions of the dataset using the dim() function.
dim(baseball)

#3.	Look at the column names of the dataset using the colnames() function.
colnames(baseball)

#4.	Find the mean and standard deviation for the number of homeruns.
mean(baseball$HR)
sd(baseball$HR)

#5.	Look at the data for teams with more than 200 homeruns.
baseball[baseball$HR>200,] # <-- used to isolate rows and attain all columns

#6.	Look at the record for the New York Yankees (NYY).
baseball[baseball$Team=="NYY",]

#7.	Look at the first four variables for the New York Yankees (NYY).
baseball[baseball$Team=="NYY",1:4]
