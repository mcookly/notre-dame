#1. Load data
install.packages("faraway")
library(faraway)
data(punting)
help(punting)

#2. Graph in scatterplot
plot(punting$RFlex,
     punting$Distance,
     xlab = "Flexibility of Right Hamstring (degrees)",
     ylab = "Distance of Punt (ft)")

#3. Regress linearly
punt_regress <- lm(punting$Distance ~ punting$RFlex)
summary(punt_regress)
abline(punt_regress)

#4. Compute SSE
sse <- sum(punt_regress$residuals^2)

#7. Compute predicted value
betas <- coef(punt_regress)
new_distance <- betas[[1]] + betas[[2]]*104

#10. Compute 90% confidence interval for Beta1