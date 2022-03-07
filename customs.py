import csv

file = open("C:/python/weekcheck6/animals.csv", "r", encoding="utf-8")

readCSVFile = csv.DictReader(file, delimiter=",")

listOfAnimals = list(readCSVFile)

countryOfOrigin = input("\n Enter the name of a country: ")
numAnimalsX = 0


for animal in listOfAnimals:
 print(f"{animal['animal']}")
 if animal ["country_of_origin"] == countryOfOrigin:
     numAnimalsX += 1





totalAnimalsValue = 0
fromThisCountry = 0


for animal in listOfAnimals:
 totalAnimalsValue += float(animal['import_value' ])
 if animal ['country_of_origin'] == countryOfOrigin:
  fromThisCountry += 1

 averageAnimalsValue = totalAnimalsValue/numAnimalsX


numAnimals = len(listOfAnimals)
averageAnimalsValue = totalAnimalsValue / numAnimals
 
print(f"Totale waarde: {totalAnimalsValue}.")
print(f"Gemiddelde waarde dier:  {averageAnimalsValue} .")
print(f"Aantal in beslag genomen uit: {countryOfOrigin} {numAnimalsX} .")

file.close()