#0. Read in data
S <- c(0,0,0,0,1,1,1,1)
P <- c(0,0,1,1,0,0,1,1)
C <- c(0,1,0,1,0,1,0,1)
count <- c(1376,73,563,436,573,63,640,1267)

#1. Observed marginal odds for S and C
ct1 <- xtabs(count ~ S + C)
theta1 <- round((ct1[1,1]*ct1[2,2]) / (ct1[1,2]*ct1[2,1]), digits = 2)

#2. Observed conditional odds for S and C given P is 0 (low)
ct2 <- xtabs(count ~ S + C, subset = (P==0))
theta2 <- round((ct2[1,1]*ct2[2,2]) / (ct2[1,2]*ct2[2,1]), digits = 2)

#3. (PS, CS) model
model3 <- glm(count ~ P*S + C*S, family = "poisson")

#4. Fit more models
library(MASS)

# Mutual
model4 <- round(AIC(glm(count ~ P + C + S, family = "poisson")), digits = 3)

# Conditional
model5 <- round(AIC(glm(count ~ P*S+P*C, family = "poisson")), digits = 3)
model6 <- round(AIC(glm(count ~ C*S+P*C, family = "poisson")), digits = 3)
model7 <- round(AIC(glm(count ~ P*S+S*C, family = "poisson")), digits = 3)

# Joint
model8 <- round(AIC(glm(count ~ P*S+C, family = "poisson")), digits = 3)
model9 <- round(AIC(glm(count ~ P+S*C, family = "poisson")), digits = 3)
model10 <- round(AIC(glm(count ~ P*C+S, family = "poisson")), digits = 3)

# Uniform
model11 <- round(AIC(glm(count ~ P*C+S*C+P*S, family = "poisson")), digits = 3)

# Saturated
model12 <- round(AIC(glm(count ~ P*C*S, family = "poisson")), digits = 3)

#5. Fitted count (model11)
mod <- glm(count ~ P*C+S*C+P*S, family = "poisson")