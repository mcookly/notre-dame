#0. Load data
gavote <- read.table("gavote.txt", header = T)

#1. Calculate undercount for each county
undercount <- (gavote$ballots - gavote$vote) / gavote$ballots

#2. Fit a LinReg model: econ predicts undercount
regress_ec <- lm(undercount ~ gavote$econ)
summary(regress_ec)

#5. Regress with econ and rural
regress_ec_ru <- lm(undercount ~ gavote$econ + gavote$rural)
summary(regress_ec_ru)
