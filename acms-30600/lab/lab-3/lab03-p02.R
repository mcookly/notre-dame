#1. Import data
accidents <- read.csv("accidents.csv", header = TRUE)

#2. Calculate mean difference
differences <- accidents$Before - accidents$After

#3. Test to see if number of accidents has been reduced
t.test(differences, alternative = "greater", conf.level = 0.95)
