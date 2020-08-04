# A country collects property tax on the assessment value, which is 60% of the property's actual value. The property tax is then 72 cents per $100 dollars of the assessment value. Write a program that asks for the actual value of a piece of property and displays the assessment value and property tax.


#Ask the user to input actual value
actual_value= float(input(" What is the property's actual value: "))
#Assessment is 60% of actual value
assessment_value= 0.60 * actual_value
# Property tax is 72% of assessment divided by 100
property_tax= 0.72 * (assessment_value/100) * 1
print("If your property's actual value is: $" + format(actual_value, ",.2f") + " then the assessment value is: $" + format(assessment_value, ",.2f") + " and the property tax is: $" + format(property_tax, ",.2f"))

# Now with functions, used different variable names to avoid confusion from the previous solution.

#Ask user for property value. Store answer in function.
def Property_Actual():
  property_value= float(input(" What is the property's actual value: "))
  return property_value

#Now get assessment value. This has an argument because we need to know the actual value to take 60% of it. Store in function
def Assessment(property_actual_value):
  assessment_amount= 0.60 * property_actual_value
  return assessment_amount

#Now get property tax. This also has an argument because we need to know what the assessment is in order to apply the property tax equation. Store answer in function
def Property_Tax(assessment):
  property_taxation= 0.72 * (assessment/100) *1
  return property_taxation

#Now combine everything. We can now use the stored information from the previous functions but to actaully use them, we need to store the functions into a variable inside of the Main function. Once we do that, we can pass the variables as arguments for the functions that required one. Then, make sure you make your print statement to show your desired statement.
def Main():
  actual= Property_Actual()
  assessment= Assessment(actual)
  propertyTax= Property_Tax(assessment)
  print("Your property is worth: $" + format(actual, ",.2f") + " Its assessment value is: $" + format(assessment, ",.2f") + " And the property tax is: $" + format(propertyTax, ",.2f"))

#Lastly, don't forget to call the function.
Main()
