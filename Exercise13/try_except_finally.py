# this is tuple containing elements
names_tuple = 'Rod', 'Jane', 'Freddy'

# try block tries to execute the code and displays the original tuple
# sorting the tuple -sorted function sorts the elements into a list
# tuples are immutable, lists are mutable so can be changed
# to change the list .append method is used to add 'bungle' and print updated list
try:
    print("######## TRY #######")
    print("The TRY block attempts to run")
    print(f"Original Tuple:{names_tuple}")
    names_sorted_as_list = sorted(names_tuple)
    print(names_sorted_as_list)
    names_sorted_as_list.append("Bungle")
    print("Added Bungle:", names_sorted_as_list)
    print("Attempt to maninpulate the tuple...")
    names_tuple[0] = 'Zippy'
    print("Is this code reached?")
# the code the tries to add 'zippy' to the tuples_names
# but it iss not a list - it is a tuple
# tuples are immutable
# therefore this displays an error
except FileExistsError as error:
    print("######## EXCEPT: FileNotFoundError ########")
    print("The EXCEPT / CATCH block only tuns if this error happens")
    print(f"The following file can not be found;{error.filename}. Please try another file")
# The TypeError is printed as a result because a tuple (style) is not allowed to be changed
except TypeError as error:
    print("######## EXCEPT: TypeError #########")
    print("Oh dear, that is not allowed on that type")
    print(error)
# this does not apply to this code as the one above has been displayed
except Exception as error:
    print("######## EXCEPT: Exception ########")
    print("Generic catch-all except / catch block")
    print(error)
# in try except finally, the finally block/code always runs
# it prints messages to show that it is tidying up
# that is why names_tuple is set to none
finally:
    #Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")
    if names_tuple:
        names_tuple = None

# this is printed so that the program can continue to run
print("After exception handling is finished....the program can continue")

# Further notes
# first the try clause is executed e.g. the code between try & except
# in this case sorts the tuple into a list & appends one item to the list
# when the code tries to add an item to the original tuple (tuples cannot be changed)
# an TypeError is displayed from the except block
# if there is no exception then only the TRY code will run
# except code will not get executed
# if an execution occurs the try clause will be skipped and EXCEPT code will run
# finally is a keyword that is always used after try & except blocks
