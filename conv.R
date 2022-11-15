# Caso não tenha a dependência ainda, roda descomenta esse install pra baixar ela
#install.packages("read.dbc", repos = "http://cran.us.r-project.org")
library("read.dbc")


# O primeiro 
dbc2dbf <- function(inputFile, outputFile) {
    x <- read.dbc(inputFile)
    write.csv(x, file=outputFile)
}

allArgs = commandArgs(trailingOnly=FALSE)
args <- tail(allArgs, n=2)

try(dbc2dbf(args[1], args[2]), TRUE)