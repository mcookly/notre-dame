#Lab 8 Starter Code
install.packages("MASS")
library(MASS)

#If you have set your working directory, then the following code will readin the data directly from that directory.
train <- read.csv("training data 2019.csv", stringsAsFactors = FALSE)
train$Win_percent <- train$Wins / (train$Wins + train$Losses)
train$Conf <- as.factor(train$Conf)
train$Team <- as.factor(train$Team)

teams <- nrow(train)

#User defined function
two2one <- function(variable, round){
  temp <- data.frame(c(variable[1,],variable[2,]))
  for (i in 2:(teams/2^(round))){
    temp[i,]<- c(variable[(2*i-1),],variable[(2*i),])
  }
  temp
}

round1.data <- two2one(train,1)
View(round1.data)

# User code
round_winners <- function(round_data, n_round) {
  regress <- glm(round_data[,8+n_round] ~ Seed + Seed.1 + Wins + Wins.1 + Losses + Losses.1 + Win_percent + Win_percent.1 + RPI + RPI.1,
                        family = "binomial", data = round_data)
  round_step <- stepAIC(regress, direction = "backward")
  round_winners <- train[train[,8+n_round]==1,]
  
  return(list("winners" = round_winners, "step" = round_step))
}

# Calculate rounds
round_data <- round1.data

for (i in 1:6) {
  print(colnames(round_data)[8+i])
  round_results <- round_winners(round_data, i)
  assign(paste0("round", i, "winners"), round_results$winners)
  assign(paste0("round", i, ".step"), round_results$step)
  round_data <- two2one(round_results$winners, i+1)
}
