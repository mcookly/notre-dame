# I got this right on the first try!!!

#########
# Part 01
library(faraway)

data("troutegg")

#1. Fit regression model
trout_regress <- glm(survive/total ~ location + period,
                     data = troutegg,
                     family = "binomial",
                     weights = total)

#2. Conduct Model Utility Test

# Original model
G1 <- trout_regress$null.deviance - trout_regress$deviance
DF1 <- trout_regress$df.null - trout_regress$df.residual
pval1 <- pchisq(G1, DF1, lower.tail = F)

# Model with interaction
trout_regress_int <- glm(survive/total ~ location + period + location*period,
                      data = troutegg,
                      family = "binomial",
                      weights = total)
pval2 <- pchisq(trout_regress_int$null.deviance - trout_regress_int$deviance,
               trout_regress_int$df.null - trout_regress_int$df.residual,
               lower.tail = F)


#########
# Part 02

library(nnet)
library(generalhoslem)
data("hsb")

#4. Fit multinomial model
program_regress <- multinom(prog ~ ses + math, data = hsb)

#5. Predict subject who has math=74 and high ses.
subject <- data.frame(74, "high")
colnames(subject) <- c("math", "ses")
subject_probs <- predict(program_regress, newdata = subject, type = "probs")

#7. GHL
ghl_test <- logitgof(hsb$prog, program_regress$fitted.values, g = 5, ord = F)
ghl_test$p.value

#8. Contribution of 1
gr1_cont <- 0
for (j in 2:4) {
  obs <- ghl_test$observed[1,j]
  exp <- ghl_test$expected[1,j]
  gr1_cont <- gr1_cont + (obs - exp)^2 / exp
}
