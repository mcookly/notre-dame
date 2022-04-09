#1. Load data
library(faraway)
data("debt")

ncol(debt) # output no. columns pre-cleaning

#2. Clean data
debt <- data.frame(cbind(debt$incomegp, debt$agegp, debt$bankacc, debt$ccarduse))
colnames(debt) <- c("incomegp", "agegp", "bankacc", "ccarduse")
debt <- na.omit(debt)

ncol(debt) # output no. columns post-cleaning

#3. Fit PO model
library(VGAM)
po_model <- vglm(as.ordered(ccarduse) ~ agegp + incomegp + bankacc,
                 data = debt,
                 family = cumulative(parallel = T))
summary(po_model)

#4. Predict the CC use of Age group 1 and Income group 1
model_val <- po_model@coefficients[2] + po_model@coefficients[3] + po_model@coefficients[4]
P11 <- exp(model_val) / (1 + exp(model_val))

#5. Fit and test GENORD model
genord <- vglm(as.ordered(ccarduse) ~ agegp + incomegp + bankacc,
               data = debt,
               family = cumulative(parallel = F))
G5 <- po_model@criterion$deviance - genord@criterion$deviance
DF <- length(genord@coefficients) - length(po_model@coefficients)
chi2 <- pchisq(G5, DF, lower.tail = F)

#6. Assess fit using Generalized HL test
library(generalhoslem)
logitgof(debt$ccarduse, po_model@fitted.values, ord = T)
         