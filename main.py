cars = {
  'alex':'camero',
  'sam':'mustang',
  'eddy': 'porshce',
  'dean': 'dodge'
}
while True:
  name = input("What's you favorite car?(or blank to quit)")
  if name =="":

      break
  if name in cars:
      print(name+ "\'s car is "+cars[name])
  else:
      print("I dont have a car for",name)
      car = input("Whats their favorite car?")
      cars[name] = car
      print(name+ "\'s favorite car is "+cars[name])