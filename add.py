def  arithematic_arranger(list,display = False):
    #simple function for the arrangement and the display of mathematical 
    
    #__________________creating a dictionary of error message 
    errors ={"error_1": "Error : Too many problems",
    "error_2": """Error : operator must be "+" or "-".""",
    "error_3": "Error : Number must only contain digits",
    "error_4": "Error : Numbers cannot be more than four digits"}
    
    #_______creating the required sign for the math operation 
    sign = ["+","-"]

    #creating a list to hold the values of the split value
    
    list_2 = []
    
    #______________________sumation function_____________________
    # this function is going to return the sum of the element if display is true
    def summer(element):

        # doing a type conversion of the number element of the list
        element[0] = int(element[0])
        element[2] = int(element[2])
        add = "+"
        subsract = "-"

        if element[1] == add:
            return str(element[0] + element[2])

        elif element[1] == subsract:
            return str(element[0] - element[2])
        else:
            return-1

    #____________________printing function ______________________
    def printing_formater(element,display):
        space = " "
        dash = "-"
        length_1 = len(str(element[0]))
        length_2 = len(str(element[2]))
        
        #converting the string to interger 
        int(element[0])
        int(element[2])

        # simple function for the printting out the format
        def format(length_1,length_2,space,dash): 

            m = 0
            num_dash = 0
            if length_1 > length_2:
                space_value =( length_1-length_2) 
                m =  1 
                num_dash = length_1 +1

            elif length_1 == length_2:
                space_value =  0
                m = ((length_1 -length_2)) + 1
                num_dash = length_1 + 1
    
            else :
                space_value = 0
                m = (length_2 - length_1)+ 1
                num_dash = length_2 + 1

            # calling our summer funtion to sum our problem
            t = summer(element) 
            print()
            print((space*m) + str(element[0]))
            print(str(element[1]) + space*(space_value) + str(element[2]))
            print(dash*num_dash,)

            if display == True:
                print(space*(num_dash - len(t)) + t)
                print(dash*num_dash,end=' ')
    
            if display ==True:
                print()
        format(length_1,length_2,space,dash)

    #___________________working on the newline function for the project 

    
    def newline(element,display):
        return printing_formater(element,display)

    #___________________decision code block_____________________
    #___________________ checking for the errors________________

    # checking for the first errors for the number of problems for the function
    container_list = []
    if len(list) > 5:
        print(errors.get("error_1"))
    else:
        #splitting the list into individual list ,the split function make use of whitespace
        # splitting the individual items the list to their individual list
        for i in list:
            list_2.append( i.split(" "))

        #checking of the addation and substaction in the list of list
        for element in list_2:
            
            if element[1] not in sign:
                print(errors.get("error_2")) 

            else:
                
                #checking the first and last element if they are digits
                if (element[0].isdigit() == False) | (element[2].isdigit() == False):
                    print(errors.get("error_3"))

                else:
                    # checking for error number four if the individual element
                    # is more than four digits
                    if (len(element[0]) > 4) | (len(element[2]) > 4):
                        print(errors.get("error_4"))

                    else:
                        #print(summer(element),end=' ')
                        #printing_formater(element,display)
                        newline(element,display)
                    


# testing the arithematic arranger function for debuging 
test = ["322 + 8", "1 - 3801", "9999 + 999", "523 - 49","132 + p"]
arithematic_arranger(test,True)