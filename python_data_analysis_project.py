# Author: Wania Faraz
# CEGEP (college) Project

menu = """
 1-How many records are there in the data file? Print all records
 2-Display a numbered list to show each company and number of cereals produced  
 3-Which company produced the most cereals? How many? 
 4-Which company produced the least cereals? How many?
 5-Display all cereals in increasing order based on calories content
 6-Display all cereals produced by a given company (input required)
 7-Display all cereals with calories below a given amount (input required)
 8-What is the name of the cereal with the least sugar content? 
 9-Display the 25 cereals with the lowest sugar (in order, start with lowest)
10-Display all cereals with rating > 50% (in order, start with highest)
11-Show a distribution pie chart (count of cereals from different companies)
12-Exit
Enter your selected option :"""

D1= {} # name (str): company (str)
D2= {} # name (str): calories (int)
D3= {} # name (str): sugars (int)
D4= {} # name (str): rating (float)

#Read the data file and fill the 4 dictionaries
file = open('cereals.txt')
for line in file:
    line = line.strip('\n')
    record = line.split(',')
    D1[record[0]] = record[1] #company
    D2[record[0]] = int(record[3]) #calories
    D3[record[0]] = int(record[9]) #sugar content
    D4[record[0]] = float(record[15]) #rating
file.close()

#Dictionary for Option 2,3,4: Companies and the #cereals produced by each
No_cereals = dict.fromkeys(D1.values(),0)
for value in D1.values():
    No_cereals[value] += 1
Companies = list(No_cereals.keys()) #list of companies
numbers = list(No_cereals.values()) #list of the number of cereals produced by each company

#list of cereals in order of sugar content (least to greatest):
ordered_sugar = sorted(D3, key = D3.get)

#list of cereals in order of rating (greatest to least):
ordered_ratings = sorted(D4, key = D4.get, reverse = True) #cereal names
ratings_in_order = [] #ratings
for x in range(len(ordered_ratings)):
    ratings_in_order.append(int(round(D4[ordered_ratings[x]],0)))
    
option = 1
while option != 12:
    option = int(input(menu))
    if option == 1:
        print("There are",len(D1.keys()) ,'records:')
        print('{:40s} {:9s} {:7s}  {:10s}'.format('Name:', 'Calories:', 'Sugars:', 'Rating:'))
        for key in D1:
            name = key
            calories = D2[key]
            sugars = D3[key]
            rating = D4[key]
            print('{:40s} {:9d} {:7d} {:10.6f}'.format(name, calories, sugars, rating))
       
    elif option == 2:
        print('{:21s}{:12s}'.format('Company','# of cereals'))
        print('{:21s}{:12s}'.format(15*'-', 12*'-'))
        for x in range(len(No_cereals)):
            print('{:2d}- {:17s}{:12d}'.format(x+1,Companies[x],No_cereals[Companies[x]]))
 
    elif option == 3:  
        highest_No = max(numbers)
        efficient = Companies[numbers.index(highest_No)]
        print(efficient+' produced the most number of cereals.')
        print('Number of cereals produced:', highest_No)

    elif option == 4:
        lowest_No = min(numbers)
        slowest = Companies[numbers.index(lowest_No)]
        print(slowest+' produced the least number of cereals.')
        print('Number of cereals produced:', lowest_No)

    elif option == 5:
        print('{:39s}{:6s}'.format('Cereal name', 'Calories'))
        print('{:39s}{:6s}'.format(11*'-', 8*'-'))
        for x in D2:
            print('{:39s}{:8d}'.format(x, D2[x]))
    elif option == 6:
        print('Here are all the companies:')
        print('Post, Quaker, Kelloggs, Discontinued, General Mills, Nesquik')
        print('')
        comp = input('Enter a company to view the cereals they produce: ')
        if not(comp in Companies):
            print('This is not one of the above companies.')
            continue
        print('')
        print('Here are all the cereals produced by ' + comp + ' and their ratings:')
        for cereal in D1:
            if D1[cereal] == comp:
                print('{:39s}{:6.2f}'.format(cereal, D4[cereal]))

    elif option == 7:
        print('Each cereal contains 50 to 160 calories.')
        max_cal = input('Enter the maximum number of calories for which you would like to view all the cereals: ')
        if max_cal.isdigit():
            max_cal = int(max_cal)
            if max_cal <= 50:
                print("There aren't any cereals below this calorie count.")
                continue
            for cereal in D2:
                if D2[cereal] < max_cal:
                    print('{:39s}{:3d}'.format(cereal, D2[cereal]))
        else:
            print('Please enter a whole number.')
                       
        
    elif option == 8:
        print('Here is the cereal with the least sugar content:')
        print('{:25s}{:3d}'.format(ordered_sugar[0], D3[ordered_sugar[0]]))   
        
    elif option == 9:
        print('Here are the 25 cereals with the least amount of sugar, and their sugar content:')
        for x in range(25):
            print('{:39s}{:3d}'.format(ordered_sugar[x], D3[ordered_sugar[x]]))
        
    elif option == 10:
        print('Here are all the cereals with a rating higher than 50%:')
        for i in range(len(ratings_in_order)):
            if ratings_in_order[i] > 50:
                print('{:39s}{:3d}'.format(ordered_ratings[i], ratings_in_order[i]))
                
        
    elif option == 11:
        import matplotlib.pyplot as pl
        #Recall: Companies = list of companies
        colors = ['blue', 'yellow', 'green', 'orange', 'red', 'purple']
        #Recall: No_cereals = Number of cereals per company
        pl.pie(No_cereals.values(), labels=Companies, colors=colors, startangle=90,  autopct='%1.1f%%')
        pl.axis('equal')
        pl.title('Distribution of Number of Cereals per Company')
        pl.show()
        
    elif option == 12:
        print("Exiting...")

    else:
        print("Invalid option. Please choose a valid option.")

