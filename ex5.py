name = 'Austin M. Megier'
age = 25 # not a lie
height = 68 # inches
weight = 140 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

height_cm = height * 2.54 # converts inches to cm
weight_kg = weight * round(0.453592) # converts lbs to kg

print(f"Let's talk about {name}.")
print(f"He's {height} inches ({height_cm}cm) tall.")
print(f"He's {weight} ({weight_kg}kg) pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
total_metric = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total_metric}.")