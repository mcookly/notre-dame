library(MASS)
#Data Setup
round1 <- read.csv("Y2019.csv", stringsAsFactors = FALSE)
round1$Conf <- as.factor(round1$Conf)
round1$Team <- as.factor(round1$Team)
train <- read.csv("training data 2019.csv", stringsAsFactors = FALSE)
train$Win_percent <- train$Wins / (train$Wins + train$Losses)
train$Conf <- as.factor(train$Conf)
train$Team <- as.factor(train$Team)

teams <- nrow(train)
evens <- seq(2, teams, 2)
odds <- seq(1, (teams - 1), 2)
######################################################################################
#Functions
two2one <- function(variable){
  temp <- data.frame(c(variable[1,],variable[2,]))
  for (i in 2:(teams/2^(round))){
    temp[i,]<- c(variable[(2*i-1),],variable[(2*i),])
  }
  temp
}

transfer <- function(round, roundit,tempround){
  for(i in 1:(64/2^(round))){
    roundit$prob[(2 * i - 1)] <- tempround$prob[i]
    roundit$prob[(2 * i)]     <- 1 - roundit$prob[(2 * i - 1)]
  }
  roundit$prob
}

winlose <- function(round,roundit){
  for (i in 1:(64/2^(round - 1))){
    if(i %in% odds){
      roundit[i,(2*round+8)] <- rbinom(1,1,roundit[i,(2*round+7)])
      roundit[(i+1),(2*round+8)] <- 1-roundit[i,(2*round+8)]
    }
  }
  roundit[,(2*round+8)]
}

######################################################################################
#Simulation
total.wins <- matrix(0,64,6)
iters <- 10
for (k in 1:iters){

######################################################################################
  #round1
  round <- 1
  round1 <- read.csv("Y2019.csv", stringsAsFactors = FALSE)
  round1$Conf <- as.factor(round1$Conf)
  round1$Team <- as.factor(round1$Team)
  train <- read.csv("training data 2019.csv", stringsAsFactors = FALSE)
  train$Win_percent <- train$Wins / (train$Wins + train$Losses)
  train$Conf <- as.factor(train$Conf)
  train$Team <- as.factor(train$Team)
  
  #Change Data
  temp1 <- two2one(train)
  temp2 <- train
  for(i in 1:(teams/2)){
    temp2[(2*i-1):(2*i),]<-temp2[(2*i):(2*i-1),]
  }
  temp2 <- two2one(temp2)
  temp <- rbind(temp1,temp2)
  tempround <- two2one(round1)
  
  #Prediction
  predict.model <-round1.step
  tempround$prob <- predict(predict.model, newdata = tempround, type = "response")
  
  #Transfer
  round1$prob <- transfer(round, round1,tempround)
  
  #Assign winners
  round1$FirstRwin <- winlose(round,round1)
  
  
######################################################################################
  #round 2
  round <-2
  
  #Winners advance
  round2 <- round1[round1$FirstRwin == 1, ]
  tempround <- two2one(round2)
  
  #Predict
  predict.model <-round2.step
  tempround$prob <- predict(predict.model, newdata = tempround, type = "response")
  
  #Transfer
  round2$prob2 <- transfer(round, round2,tempround)
  
  #Assign winners
  round2$SecRwin <- winlose(round,round2)

######################################################################################
  #round 3
  round <-3
  
  #Winners advance
  round3 <- round2[round2$SecRwin == 1, ]

  tempround <- two2one(round3)
  
  #Predict
  predict.model <-round3.step
  tempround$prob <- predict(predict.model, newdata = tempround, type = "response")
  
  #Transfer
  round3$prob3 <- transfer(round, round3,tempround)
  
  #Assign winners
  round3$thrdRwin <- winlose(round,round3)
  
######################################################################################
  #round 4
  round <-4
  
  #Winners advance
  round4 <- round3[round3$thrdRwin == 1, ]

  tempround <- two2one(round4)
  
  #Predict
  predict.model <-round4.step
  tempround$prob <- predict(predict.model, newdata = tempround, type = "response")
  
  #Transfer
  round4$prob4 <- transfer(round, round4,tempround)

  #Assign winners
  round4$frthRwin <- winlose(round,round4)
  
######################################################################################
    #round 5
  round <-5
  
  #Winners advance
  round5 <- round4[round4$frthRwin == 1, ]

  tempround <- two2one(round5)
  
  #Predict
  predict.model <-round5.step
  tempround$prob <- predict(predict.model, newdata = tempround, type = "response")
  
  #Transfer
  round5$prob5 <- transfer(round, round5,tempround)

  #Assign winners
  round5$fifthRwin <- winlose(round,round5)
  
######################################################################################
  #round 6
  round <-6
  
  #Winners advance
  round6 <- round5[round5$fifthRwin == 1, ]

  tempround <- data.frame(c(round6[1,],round6[2,]))
  
  #Predict
  predict.model <-round6.step
  tempround$prob <- predict(predict.model, newdata = tempround, type = "response")
  
  #Transfer
  round6$prob6 <- transfer(round, round6,tempround)
  
  #Assign winners
  round6$sixthRwin <- winlose(round,round6)
  
  winner <- round6[round6$sixthRwin == 1, ]
  ########################################################################################################
  
  #Update winner matrix
  these.teams <- as.integer(rownames(round2))
  total.wins[these.teams, 1] <- total.wins[these.teams, 1] + 1
  
  these.teams <- as.integer(rownames(round3))
  total.wins[these.teams, 2] <- total.wins[these.teams, 2] + 1
  
  these.teams <- as.integer(rownames(round4))
  total.wins[these.teams, 3] <- total.wins[these.teams, 3] + 1
  
  these.teams <- as.integer(rownames(round5))
  total.wins[these.teams, 4] <- total.wins[these.teams, 4] + 1
  
  these.teams <- as.integer(rownames(round6))
  total.wins[these.teams, 5] <- total.wins[these.teams, 5] + 1
  
  these.teams <- as.integer(rownames(winner))
  total.wins[these.teams, 6] <- total.wins[these.teams, 6] + 1
  
  # progress bar
  if( k %% (max(floor(iters/10),1)) == 0 )
    cat(round(k/iters*100,0),"% | ",sep="")
}

#Print winner matrix
rownames(total.wins) <- round1$Team
colnames(total.wins) <- colnames(train[,9:14])
total.wins/iters
