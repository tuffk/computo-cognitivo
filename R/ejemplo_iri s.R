# @Author: Juan Carlos Leon Jarquin <shiro-saber>
# @Date:   09-Jan-2017
# @Email:  jleon@nearshoremx.com
# @Last modified by:   shiro-saber
# @Last modified time: 09-Jan-2017
# @License: Belongs to Nearshore Delivery Solutions

#librerias
library(datasets)
library(xtable)

#aqui se hace la regresion polinomial, en la cual se le puede poner la formula polinomial que se tenga.
fit <- lm(formula = Petal.Width ~ Petal.Length + Sepal.Length + Sepal.Width, data=iris)

#aqui se hace una nueva regresion con una fórmula nueva.
fit2 <- lm(Petal.Width ~ Petal.Length + Sepal.Length + Sepal.Width + Petal.Length:Sepal.Length, data=iris)

#se crea una tabla anova con los calculos de la polinomial
anova(fit, fit2)

#seguimos haciendo pruebas con mas formulas
fit3 <- lm(Petal.Width ~ Petal.Length + Sepal.Length + Sepal.Width + Species, data=iris)
summary(fit3)

#Tabla anova
anova(fit, fit3)

#para imprimir la tabla en estilo html
#print(xtable(fit3), type="html")
