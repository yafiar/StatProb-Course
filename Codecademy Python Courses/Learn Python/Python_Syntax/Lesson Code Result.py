#ini hanya untuk belajar basic python
print("Hello world!")
print "Ini coba "+"pakai string"
todays_date = "30 Agustus 2024"
product = 40 * 3
remainder = 1398 % 11

-----------------------------------------------------------------------------------------------------
#rainfall variable
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
annual_rainfall += september_rainfall

october_rainfall = 7.20
annual_rainfall += october_rainfall

november_rainfall = 5.06
annual_rainfall += november_rainfall

december_rainfall = 4.06
annual_rainfall += december_rainfall
print annual_rainfall

-----------------------------------------------------------------------------------------------------
#comments
city_name = "St. Potatosburg"
#pop pada kota ini sebanyak
city_pop = 340000

-----------------------------------------------------------------------------------------------------
#percobaan int & float
cucumbers = 2
price_per_cucumber = 3.25

total_cost = cucumbers * price_per_cucumber
print total_cost

-----------------------------------------------------------------------------------------------------
#float devine
cucumbers = 100
num_people = 6

whole_cucumbers_per_person = cucumbers/num_people
print whole_cucumbers_per_person

float_cucumbers_per_person = float(cucumbers)/num_people
print float_cucumbers_per_person

-----------------------------------------------------------------------------------------------------
#multi line stings
haiku = """The old pond,
A frog jumps in:
Plop!"""

print haiku

-----------------------------------------------------------------------------------------------------
#boolines
# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.

age_is_12 = False
name_is_maria = True

-----------------------------------------------------------------------------------------------------
#ValueError
float_1 = 0.25
float_2 = 40.0
product = float(float_1) * float(float_2)
big_string = "The product was " + str(product)

-----------------------------------------------------------------------------------------------------
#review
skill_completed = "Python Syntax"
exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed * points_per_exercise

print "I got " + str(point_total) + " points!"
