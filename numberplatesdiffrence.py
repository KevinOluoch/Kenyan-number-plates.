
print  """THIS CODE CALCULATES THE NUMBER OF CIVILIAN CARS BOUGHT BETWEEN
 ANY TWO NUMBER KENYAN NUMBER PLATES WITH THE TWO NUMBER PLATES EXCLUDED

 NB: ->You can enter the number plate in upper or lower case characters
     ->This code assumes that their exists cars with Number plate
       KAA 001 - KZZ 999Z and hence it is not resstricted to cars that have
       been bought officially. 
"""


def get_plate_number(first_or_second):
    """ A function that takes either the string 'first' or 'second'
    and then prompts the user to input the 'first' or 'second' number plate.
    The value given is checked to assert its a valid plate number given in the
    correct format. The value is then returned.
    If the value input by the user is not correct in any way, they are prompted 
    again to input a correct value.
    """


    while True:
        plate_number= raw_input(
        "\n \n Please Enter the %s Number Plate. Use the format KZZ 999(Z): " 
        %(first_or_second))

        # Ensure the format is correct 
        len_of_plate_number = len(plate_number) 
        if not (
           len_of_plate_number == 7
           or len_of_plate_number == 8
           ):
            print "\n The Number Plate is not in the correct format"
            continue

        if  len_of_plate_number == 7:
            if not (
             plate_number[1:3].isalpha()
             and (plate_number[3] == " ")
             and (plate_number[4:7].isdigit()) ):
                print "\n The Number Plate is not in the correct format"
                continue

        elif len_of_plate_number == 8:
            if not (
             (plate_number[1:3] + plate_number[7]).isalpha()
             and (plate_number[3] == " ")
             and (plate_number[4:7].isdigit()) ):
                print "\nThe Number Plate is not in the correct format"
                continue
        
        # Convert lower case Number Plate letters to uppercase
        plate_number = plate_number.upper() 

        # Ensure their are no illegal characters in the Number Plate

        if len_of_plate_number == 8:
            if (plate_number[7] in ("I", "O")
            or plate_number[:3] == "KAF" ):
                print "\nThat Number Plate does not exist"
                print "Please Enter a valid plate number"
                continue

        if (
        plate_number[0] != "K"
        or plate_number[1] in ("I", "O")
        or plate_number[2] in ("I", "O")):
            print "\nThat Number Plate does not exist"
            print "Please Enter a valid plate number"
            continue

        return plate_number


def calculate_number_plate_equivalent(plate_number):
    """A function that calculates a number equivalent of number plates
    starting with KAA 001A as one.
    The three digits are incremented to 999, then they reset to zero and the
    last character which is an alphabet is incremented.
    when the last character reaches 'Z', the third chracter is incremented
    followed by the second.
    the first character is not included in the counting
    the largest value corresponds to KZZ 999Z
    """


    # Dictionary with alphabetical letters as key and equivalent number as value
    letter_number = {
                    letter : count for
                    count, letter in enumerate("ABCDEFGHJKLMNPQRSTUVWXYZ")
                    }

    # Calculating numerical value of the number plate
    if len(plate_number) == 7:
        number_equivalent = (
                                int(plate_number[4:7])
                                + ( 999 * letter_number[plate_number[2]] )
                                + (23976 * letter_number[plate_number[1]] )
                                )


    if len(plate_number) == 8:
        number_equivalent = (
                                int(plate_number[4:7])
                                + ( 999 * letter_number[plate_number[7]] )
                                + (23976 * letter_number[plate_number[2]] )
                                + ( 575424 * letter_number[plate_number[1]] )
                                + 575424
                                )

        # Since KAF series was reseaved for the Kenya Air force, 
        # values after KAF series are decremented to cover the gap
        if (
         letter_number[plate_number[2]] > 5  
         or  letter_number[plate_number[1]] > 0):

            number_equivalent -= 23976

    return number_equivalent



while True:
    # Get the Number Plates
    plate_one = get_plate_number('first')
    print "\nThe First Number Plate is %s " % plate_one
 
    plate_two = get_plate_number('second')
    print "\nThe Second Number Plate is %s " % plate_two

    # Get numerical value of the Number Plates and
    # the diffrence between them
    number_of_plates_between = (calculate_number_plate_equivalent(plate_one)
                            - calculate_number_plate_equivalent(plate_two))
                            
    if number_of_plates_between:
        print ("\n \nBetween %s and %s, " % (plate_one, plate_two))
        print ("there are %d cars bought with the two numbers excluded" 
               % (abs(number_of_plates_between) - 1) )

    else:
        print "\n \nThe two Number Plates you provided are the same"

    #Allow the user to choose to exit or input another set of Number Plates
    break_option = raw_input("\n \nEnter 0 to exit, or any key to continue: ")
    if break_option == "0":
        print "\n \nTHANK YOU & GOODBYE"
        break




