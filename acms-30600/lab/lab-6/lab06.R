###########################
# Part 1

#0. Load packages
library(faraway)
library(lmtest)
data(airquality)

#1. Fit model to predict Ozone
ozone_regress <- lm(Ozone ~ Wind + Temp + Solar.R, data = airquality)

#2. Plot fitted v. residual values
plot(ozone_regress$residuals, ozone_regress$fitted.values)

#3. Par something
par(mfrow = c(3,1))
ozone <- airquality$Ozone
plot(ozone, airquality$Wind)
plot(ozone, airquality$Temp)
plot(ozone, airquality$Solar.R)

#4. Sqrt()
plot(ozone, sqrt(airquality$Wind))
plot(ozone, sqrt(airquality$Temp))
plot(ozone, sqrt(airquality$Solar.R))

#5. log()
plot(ozone, log(airquality$Wind))
plot(ozone, log(airquality$Temp))
plot(ozone, log(airquality$Solar.R))


# Part 3
########

#7. Rerun regression and plot
ozone_reg_trans <- lm(log(Ozone) ~ Wind + Temp + Solar.R,
                                  data = airquality)
par(mfrow = c(1,1))
hist(ozone_reg_trans$residuals, breaks = 20)

#8. QQ Plot
qqnorm(ozone_reg_trans$residuals)
qqline(ozone_reg_trans$residuals)

#9. Conduct Shapiro-Wilk test
shapiro.test(ozone_reg_trans$residuals)

#10. Durbin-Watson Test
dwtest(ozone_reg_trans)

# Part 5
########
predict_data <- data.frame(Solar.R = 186, Wind = 10, Temp = 80)
predict(ozone_reg_trans, newdata = predict_data)