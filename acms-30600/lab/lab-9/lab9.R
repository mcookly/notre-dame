##########
# Part 1

#3. Calculate p-value
p3 <- pchisq(32.1754, 3, lower.tail = F)

#4. Repeat hand calculations
data <- c(226, 109, 110)
props <- c(.635, .193, .172)
marj <- chisq.test(data, p= props)
marj$expected
marj$statistic
marj$p.value

##########
# Part 2

install.packages("faraway")
library(faraway)
library(ResourceSelection)
library(ROCR)
data(wbca)

#5. Fit model
benign_regress <- glm(Class ~ BNucl+ Thick+ Chrom+ UShap+ USize,
                      family = "binomial", data = wbca)
predict_values <- data.frame(cbind(median(wbca$BNucl),
                                   median(wbca$Thick),
                                   median(wbca$Chrom),
                                   median(wbca$UShap),
                                   median(wbca$USize)))
colnames(predict_values) <- c("BNucl", "Thick", "Chrom", "UShap", "USize")
predict.glm(benign_regress, type = "response", newdata = predict_values)

#6. Test for removal of UShap and USize
benign_regress1 <- glm(Class ~ BNucl+ Thick+ Chrom,
                       family = "binomial", data = wbca)
summary(benign_regress1)
G <- benign_regress1$deviance - benign_regress$deviance
df <- benign_regress1$df.residual - benign_regress$df.residual
p6 <- pchisq(G, df, lower.tail = F)

#7. Conduct HL test
hl_test <- hoslem.test(benign_regress$y, benign_regress$fitted.values)
hl_test$statistic
hl_test$observed
hl_test$expected
p7 <- hl_test$p.value
gr3_cont <- (hl_test$observed[3,1] - hl_test$expected[3,1])^2 /hl_test$expected[3,1] +
  (hl_test$observed[3,2] - hl_test$expected[3,2])^2 /hl_test$expected[3,2]

#8. ROC and AUC
pred <- prediction(benign_regress$fitted.values, wbca$Class)
perf <- performance(pred, measure = "tpr", x.measure = "fpr")
plot(perf, colorize = T)
abline(a = 1, b = -1)

auc_tmp <- performance(pred, "auc")
auc <- as.numeric(auc_tmp@y.values)
