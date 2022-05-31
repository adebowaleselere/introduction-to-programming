# 60 seconds make 1 minute
# 60 minutes make one hour
# 24 hours make one day
# hence there are 31,536,000 seconds in a year

secondsInAYear = 31536000
birthInOneYear = secondsInAYear // 7
deathInOneYear = secondsInAYear // 13
immigrantInOneYear = secondsInAYear // 45

populationInOneYear = (birthInOneYear + immigrantInOneYear) - deathInOneYear
currentPopulation = 312032486

yearOnePopulation = currentPopulation + populationInOneYear
yearTwoPopulation = yearOnePopulation + populationInOneYear
yearThreePopulation = yearTwoPopulation + populationInOneYear
yearFourPopulation = yearThreePopulation + populationInOneYear
yearFivePopulation = yearFourPopulation + populationInOneYear

print("year 1 population")
print(yearOnePopulation)
print(" ")
print("year 2 population")
print(yearTwoPopulation)
print(" ")
print("year 3 population")
print(yearThreePopulation)
print(" ")
print("year 4 population")
print(yearFourPopulation)
print(" ")
print("year 5 population")
print(yearFivePopulation)
print(" ")
