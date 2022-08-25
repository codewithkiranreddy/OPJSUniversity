#Name : Saikiran Chittireddy
#College : OPJS University
#Year of passout : 2022
#Contact No : 8520959890
#Email ID : codewithkiranreddy@gmail.com


class PlanetaryData:
  def __init__(self, planets):
    self.planets = planets
  
  def countOfMoons(self):
    count = 0
    for planet in self.planets:
      if planet["rings"]== True:
        count += planet["moons"]
    print(count)

  def findGas(self):
    gas = set()
    for planet in self.planets:
      gas.update(set(planet["gasses"]))
    
    result = ''
    gasses_count = 0
    for each_gas in gas:
      for planet in self.planets:
        gas_count = planet["gasses"].count(each_gas)
        if gas_count > gasses_count:
          gasses_count = gas_count
          result = each_gas
    print(result)


planets = [{
  "name" : "Mercury",
  "gasses" : [],
  "moons" : 0,
  "rings" : False
},
{
  "name" : "Venus",
  "gasses" : ["Carbon Dioxide", "Nitrogen"],
  "moons" : 0,
  "rings" : False
},
{
  "name" : "Earth",
  "gasses" : ["Nitrogen", "Oxygen"],
  "moons" : 1,
  "rings" : False
},
{
  "name" : "Jupitor",
  "gasses" : ["Hydrogen", "Helium"],
  "moons" : 79,
  "rings" : True
},
{
  "name" : "Saturn",
  "gasses" : ["Hydrogen", "Helium"],
  "moons" : 83,
  "rings" : True
},
{
  "name" : "Uranus",
  "gasses" : ["Hydrogen", "Helium", "Methane"],
  "moons" : 27,
  "rings" : True
}]
data = PlanetaryData(planets)
data.countOfMoons()
data.findGas()
