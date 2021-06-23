# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is "  + str(estimated_cost) + " dollars.")
  return estimated_cost

def diffence_in_cost(cost1, cost2):
    print("The difference in insurance cost is " + str(cost1 - cost2) + " dollars.")
    return cost1 - cost2


# Initial variables for Maria 
#age = 28
#sex = 0  
#bmi = 26.2
#num_of_children = 3
#smoker = 0  

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, "Maria")

#print("The estimated insurance cost for Maria is " + str(maria_insurance_cost) + " dollars.")

# Initial variables for Omar
#age = 35
#sex = 1 
#bmi = 22.2
#num_of_children = 0
#smoker = 1  

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, name ="Omar")

#print("The estimated insurance cost for Omar is " + str(insurance_cost) + " dollars.")

my_own_insurance_cost = calculate_insurance_cost(27, 0, 20.2, 0, 0, name ="my own")

diffence_in_cost(omar_insurance_cost, maria_insurance_cost)

# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
   print("To lower your cose, you should consider quitting smoking.")
  else: 
    print("Smoking is not an issue for you.")


def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.")
  elif bmi_value < 18.5:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")
 
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost
  
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)

estimate_insurance_cost(name = 'John', age = 30, sex = 1, bmi = 20.2, num_of_children = 3, smoker = 0)

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
print(str(names) + '\n')
insurance_costs.append(8320.0)
print(str(insurance_costs) + '\n')

medical_records = list(zip(insurance_costs, names))
print(str(medical_records) + "\n")

num_medical_records = len(medical_records)
print(str(num_medical_records) + '\n')

print("There are " + str(num_medical_records) + " medical records.\n")

first_medical_records = medical_records[0]
print(str(first_medical_records) + '\n')

print("Here is the first medical record: " + str(first_medical_records) + '\n')

medical_records.sort()
print(str(medical_records) + '\n')

print("Here are the medical records sorted by insurance cost: " + str(medical_records) + "\n")

cheapest_three = medical_records[:3]
print(str(cheapest_three) + '\n')

print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three) + '\n')

priciest_three = medical_records[-3:]
print(str(priciest_three) + "\n")

print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three) + "\n")

occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records." + '\n')
