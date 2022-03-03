#7. Load data
library(faraway)
library(MASS)
data(seatpos)

#8. Model
hip_regress <- lm(hipcenter ~ Ht + HtShoes + Thigh + Leg, data = seatpos)
summary(hip_regress)

#9. VIF
vif(hip_regress)

#10. StepAIC()
stepAIC(hip_regress)

#11. Fit final model
hip_regress1 <- lm(hipcenter ~ Ht + Leg, data = seatpos)
summary(hip_regress1)
