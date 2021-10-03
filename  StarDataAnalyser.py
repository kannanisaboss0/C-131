#------------------------------------------------------------------------------------StarDataAnalyser.py------------------------------------------------------------------------------------#
'''
Importing modules:
-csv 
-plotly.figure_facotry (ff)
-sys
-math (mth)
-statistics (st)
'''
import csv
import plotly.figure_factory as ff
import sys
import math as mth
import statistics as st
import time as tm



print("Welcome to StarDataAnalyser.py. We provide methods to analyse a given set of stars and compare their statiistics")
tm.sleep(3.3)
view_information_weight=input("Do not know the mathematical definition of weight?")

#Verifying whether the user knows about the mathematical expression fo weight or not in order to conduct further actions
#Case-1
if(view_information_weight=="I Don't Know" or view_information_weight=="i don't know" or view_information_weight=="I don't know" or view_information_weight=="I don't Know" or view_information_weight=="I Don't know" or view_information_weight=="I Dont Know" or view_information_weight=="i dont know" or view_information_weight=="I dont know" or view_information_weight=="I dont Know" or view_information_weight=="I Dont know"):
  print("Weight is mathematically related to Newton's Second Law of Motion, which states that the rate of change of momentum of an object is directly proportional to the applied unbalanced force in the direction of the force.")
  tm.sleep(5.4)

  print("In other words, Newton's Second Law of Motion can be mathematically express as: ")
  tm.sleep(2.3)

  print("F=ma")
  print("F is the force exerted")
  print("m is the mass of the object")
  print("a is the acceleration the object experiences")
  tm.sleep(4.5)

  print("Since the weight of an object is the effect of gravity on it, it can be considered the product of the object's mass and the acceleration of gravity produced by the larger body.")
  tm.sleep(3.9)

  print("Hence the formula for weight is:")
  print("W=mg")
  print("W is the fweight of the object")
  print("m is the mass of the object")
  print("g is the acceleration due to gravity produced on the object by  the larger body")
  tm.sleep(2.2)

#Verifying whether the user knows about escape velocity or not in order to conduct further actions
view_information_escape_velocity=input("Don't know about escape velocity?")
#Case-1
if(view_information_escape_velocity=="I Don't Know" or view_information_escape_velocity=="i don't know" or view_information_escape_velocity=="I don't know" or view_information_escape_velocity=="I don't Know" or view_information_escape_velocity=="I Don't know" or view_information_escape_velocity=="I Dont Know" or view_information_escape_velocity=="i dont know" or view_information_escape_velocity=="I dont know" or view_information_escape_velocity=="I dont Know" or view_information_escape_velocity=="I Dont know"):
  print("The escape velocity of a body, is the minimum velocity required to escape the body's gravitational pull.")
  tm.sleep(2.3)

  print("The escape velocity of all objects escaping from the gravitaional pull of a planet are constant, and hence not related to the object's mass.")
  tm.sleep(3.2)

  print("The formula for escape velocity of an object is:")
  print("√(2GM/r)")
  print("G is the Gravitational Constant equal to 6.67 × 10^-11")
  print("M is the mass of the large body")
  print("r is the distnace from the large body's center of mass")
  tm.sleep(5.4)

  print("This formula for escape velocity of an object is usually preferred for massive bodies such as planets.")
  tm.sleep(2.3)

  print("To know more about escape velocity, visit 'https://letstalkscience.ca/educational-resources/stem-in-context/escape-velocity'")
  tm.sleep(2.3)

print("Loading Data...")
tm.sleep(4.5)  

#Defining a function to print the ending message 
def PrintEndingMessage():
  print("Thank You for using StarDataAnalyser.py")


#Defining a function to calculate the weight of an object of chosen mass on the desired star of the user
def CalculateWeight(star_name_param,star_gravity_param):
  mass_input=input("Please enter the mass of the desired object whose weight on {} is to be found:".format(star_name_param))

  #Verifying whether the user hass added a unit or not next to the entered value
  #Case-1
  if(" " not in mass_input):
    mass_input=mass_input+" kg"

  first_value,second_value=mass_input.split(" ")

  second_value_lowered=second_value.lower()
  
  #Assessing the unit provided by the user and converting it accordingly to kilograms (kg)
  #Case-1
  if(second_value_lowered=="g" or second_value_lowered=="grams" or second_value_lowered=="gram"):
    first_value_converted=float(first_value)/1000
  #Case-2  
  elif(second_value_lowered=="t" or second_value_lowered=="tons" or second_value_lowered=="ton" or second_value_lowered=="tonnes" or second_value_lowered=="tonne"):
    first_value_converted=float(first_value)*1000
  #Case-3  
  else:
    first_value_converted=float(first_value) 

  weight_object=first_value_converted*star_gravity_param
  print("The weight of an object of mass {} kg on the surface of {} is {} kg".format(first_value_converted,star_name_param,weight_object))


#Defining a function to calculate the escape velocity of an object on the desired star of the user
def CalculateEscapeVelocity(star_name_param,star_radius_param,star_mass_param,gravitational_constant_param):
  escape_velocity_input=input("Please enter the distance from {} in order to find the escape velocity:".format(star_name_param))

  #Verifying whether the user hass added a unit or not next to the entered value
  #Case-1
  if(" " not in escape_velocity_input):
    escape_velocity_input=escape_velocity_input+" m"

  first_value_escape_velocity,second_value_escape_velocity=escape_velocity_input.split(" ")

  second_value_escape_velocity_lowered=second_value_escape_velocity.lower()
  
  #Assessing the unit provided by the user and converting it accordingly to metres (m)
  #Case-1
  if(second_value_escape_velocity_lowered=="km" or second_value_escape_velocity_lowered=="kilograms" or second_value_escape_velocity_lowered=="kilogram"):
    first_value_escape_velocity_converted=float(first_value_escape_velocity)*1000
  #Case-2  
  elif(second_value_escape_velocity_lowered=="cm" or second_value_escape_velocity_lowered=="centimetres" or second_value_escape_velocity_lowered=="centimetre"):
    first_value_escape_velocity_converted=float(first_value_escape_velocity)/100
  #Case-3  
  else:
    first_value_escape_velocity_converted=float(first_value_escape_velocity)
    

  escape_velocity=mth.sqrt(2*gravitational_constant_param*float(star_mass_param)/first_value_escape_velocity_converted+float(star_radius_param))
  print("The escape velolcity of {} at {} m away from it is {}".format(star_name_param,first_value_escape_velocity_converted,escape_velocity))


#Defing a function to show the options of calculations for the user on the desired star of the user
def ShowCalculationOptions(star_name_param,star_mass_param,star_radius_param,star_gravity_param,gravitational_constant_param):
  calculations_list=["Unusable_element","Weight","Escape Velcocity"]
  calculation_count=0

  for calculation in calculations_list[1:]:
    calculation_count+=1
    print("{}:{}".format(calculation_count,calculation))

  calculation_choice_input=int(input("Please enter the index of the value desired to calculate:"))
  
  #Assessing the user's choice and selecting the calculation functions accordingly
  #Case-1
  if(calculation_choice_input==1):
    CalculateWeight(star_name_param,star_gravity_param)
  #Case-2  
  if(calculation_choice_input==2):
    CalculateEscapeVelocity(star_name_param,star_radius_param,star_mass_param,6.67*10**-11)  


#Defining a function to provide the user the actions the user can conduct
def ProvideOptionsForSegregation(choice_param,choice_count_param):
  for choice in choice_param[1:]:
    choice_count_param+=1
    print("{}:{}".format(choice_count_param,choice))

  choice_input=int(input("Please enter the index of the action desired to perform:"))
  choice_count_param=0

  #Verifying whether the user's input is valid
  #Case-1
  if(choice_input>2 or choice_input<1):
    sys.exit("Invalid Input. Please enter either 1 or 2 according to the action desired to perform .")
  #Case-2  
  else:
    None

  user_choice=choice_list[choice_input]

  HandleUserInput(user_choice,choice_param,choice_count_param)


#Defining a function to perform the corresponding actions to the user's input
def HandleUserInput(choice_param,choice_param_2,choice_count_param):

  #Assessing the user's input to select the functions accordingly
  #Case-1 
  if(choice_param=="Find Star Details"):
    input_star_param=input("Please enter the star name, desired to know about:")
    GatherInformationFromStarList(star_list,reader_list,input_star_param,gravity_list,radius_list,choice_param,choice_param_2,choice_count_param)
  #Case-2  
  elif(choice_param=="Plot Distribution Graph"):
    ChooseParametersForDistributionGraph()

#Defining a functions to phrovide the paramters the user can choose accordingly for the plotting the dsitribution graph
def ChooseParametersForDistributionGraph():
  parameter_list=["Unusable_Element","Gravity","Mass","Radius"]
  parameter_count=0

  for parameter in parameter_list[1:]:
    parameter_count+=1
    print("{}:{}".format(parameter_count,parameter))

  parameter_input=int(input("Please enter the index of the parameter desired to plot the distribution graph on:"))

  #Verifying whether the user's input is valid
  #Case-1
  if(parameter_input>4 or parameter_input<1):
    sys.exit("Invalid Input. Please enter a number rangeing between of 1 and 3, inclusive of extremes.")
  #Case-2
  else:
    user_choice=parameter_list[parameter_input]   
    PlotDistributionGraphAndCalculateStatistics(parameter_list[parameter_input]) 


#Defining a function to plot the distribution and calculated related statistics
def PlotDistributionGraphAndCalculateStatistics(label_param):
  data_variable=None

  #Assessing the user's input with the use of a paramter from a previous function
  #Case-1
  if(label_param=="Gravity"):
    data_variable=gravity_list
  #Case-2
  elif(label_param=="Mass"):
    data_variable=mass_list
  #Case-3  
  elif(label_param=="Radius"):
    data_variable=radius_list

  #Plotting the distribution graph
  dist_plot=ff.create_distplot([data_variable],[label_param],show_hist=False)
  dist_plot.show()

  lower_mean_count=0
  higher_mean_count=0

  data_variable_mean=st.mean(data_variable)

  for data_variable_element in data_variable:

    #Assessing whether the values are greater or lesser in the mean
    #Case-1
    if(data_variable_element<data_variable_mean):
      lower_mean_count+=1
    #Case-2  
    elif(data_variable_element>data_variable_mean):
      higher_mean_count+=1

  print("The mean is: {}".format(data_variable_mean))
  print("{} have their radius lower than the mean-{}".format(lower_mean_count,data_variable_mean))
  print("{} have their radius higher than the mean-{}".format(higher_mean_count,data_variable_mean))

  restart_procedure_prompt=input("Plot more?")

  #Assessing the user's choice to plot the distribution graph, posssibly with a different parameter
  #Case-1
  if(restart_procedure_prompt=="Yes" or restart_procedure_prompt=="yes" or restart_procedure_prompt=="YES" or restart_procedure_prompt=="yEs" or restart_procedure_prompt=="yeS" or restart_procedure_prompt=="Y" or restart_procedure_prompt=="y"):
    ChooseParametersForDistributionGraph()
  #Case-2  
  else:
    print("Request Accepted.")
    PrintEndingMessage()  


#Defining a function to display data about the star the user has chosen
def GatherInformationFromStarList(star_param,reader_param,star_input_param,gravity_param,radius_param,choice_param,choice_param_2,choice_count_param):
  
  #Verifying whether the user's input is a valid star in the star list
  #Case-1
  if(star_input_param not in star_param):
      restart_prompt=input('The star could not be found. Try again?')  

      #Asking the user whether they want to restart the procedure due to the entry of an invalid input
      #Case-1
      if(restart_prompt=="Yes" or restart_prompt=="yes" or restart_prompt=="YES" or restart_prompt=="yEs" or restart_prompt=="yeS" or restart_prompt=="Y" or restart_prompt=="y"):
        ProvideOptionsForSegregation(choice_param_2,choice_count_param)
      #Case-2
      else:
        print("Request Accpeted.")
        PrintEndingMessage() 
  #Case-2       
  else:      
    for star_element_index,star_element in enumerate(star_param):

        #Assessing whether the user's input matches the star in the star list and performing necessary actions on matching   
        #Case-1
        if(star_input_param==star_element):
          star_data_collective=reader_param[star_element_index]
          star_data_collective=star_data_collective[1:]

          star_name=star_data_collective[0]
          star_distance=star_data_collective[1]
          star_mass=star_data_collective[2]

          print("Name: {}".format(star_name))
          print("Distance: {} Astronimcal Units".format(star_distance))
          print("Mass: {} kilograms".format(float(star_mass)*1.989e+30))

          star_radius=radius_param[star_element_index]
          print("Radius: {} metres".format(star_radius))

          star_gravity=gravity_param[star_element_index]
          print("Gravity: {} metres per second sqaure".format(star_gravity))

          calculate_prompt=input("Conduct calaculations?")

          #Asking the user whether they want to start the process again
          #Case-1
          if(calculate_prompt=="Yes" or calculate_prompt=="yes" or calculate_prompt=="YES" or calculate_prompt=="yEs" or calculate_prompt=="yeS" or calculate_prompt=="Y" or calculate_prompt=="y"):
            ShowCalculationOptions(star_name,star_mass,star_radius,star_gravity,6.67*10**-11)
          #Case-2  
          else:
            print("Request Accepted.")
            PrintEndingMessage()  
          break
          

with open("final_data.csv","r") as f:
  reader=csv.reader(f)
  reader_list=list(reader)

headings=reader_list.pop(0)
headings=headings[1:]


gravity_list=[]
mass_list=[]
radius_list=[]
star_list=[]
distance_list=[]

gravitational_constant=6.67*10**-11
for star_data_index,star_data_element in enumerate(reader_list):
  mass_list_element=star_data_element[3]
  for mass_character in mass_list_element:

    #Verifying whether the value contains a comma
    #Case-1
    if(mass_character==","):
      mass_element_list.replace(",","")
    #Case-2  
    else:
      continue  

  star_list_element=star_data_element[1]
  star_list.append(star_list_element)

  mass_list_element_modified=float(mass_list_element)*1.989e+30
  mass_list.append(mass_list_element_modified)
  
  radius_list_element=star_data_element[4]


  for radius_character in radius_list_element:

    #Verifying whether the value contains a comma
    #Case-1
    if(radius_character==','):
      radius_list_element=radius_list_element.replace(',',"")
    #Case-2  
    else:
      continue  

  radius_list_element_modified=float(radius_list_element)*6.957e+8
  radius_list.append(radius_list_element_modified)


  gravity_element=gravitational_constant*mass_list_element_modified/radius_list_element_modified**2
  gravity_list.append(gravity_element)

choice_list=["Unusable_Element","Find Star Details","Plot Distribution Graph"]
choice_count=0


ProvideOptionsForSegregation(choice_list,choice_count)
#------------------------------------------------------------------------------------StarDataAnalyser.py------------------------------------------------------------------------------------#