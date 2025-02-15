from sys import excepthook

names_tuple = 'Rod', 'Jane', 'Freddy'

try:
    # these are the arguments/ functions that we want to try out. They will keep getting tested and below this, we have what to do if certain errors are reached

    print('###### TRY #######')
    print('The TRY block attempts to run')
    print(f'Original Tuple: {names_tuple}')
    names_sort_as_list = sorted(names_tuple)
    print(names_sort_as_list)
    names_sort_as_list.append('Bungle')
    print('Added Bungle:', names_sort_as_list)
    print('Attempt to manipulate the tuple...')
    names_tuple[0] = 'Zippy'
    # at this point an error has been reached because the tuple is immutable
    print('Is this code reached?')
#     this line did not print because we reached the error and now have to go to exceptions
except FileNotFoundError as error:
    # did not print because it was not a filenotfound type of error
    # error is a new variable which python has assigned to the thing which has stopped the code from working above
    print('##### EXCEPT": FileNotFoundError ####')
    print('The except / CATCH block only runs if this error happens')
    print(f'The following file cannot be found {error.filename}. Please try another file')
except TypeError as error:
    print('###### EXCEPT: Exception #######')
    print('Oh dear, that is not allowed on that type')
    print(error)
# this printed because the error type was a typeerror ie trying to change the tuple
except Exception as error:
    print('###### EXCEPT: Exception #######')
    print('Generic catch-all except/ catch block')
    print(error)
# this is s generic error but did not run because the code above was executed as that defined the error correctly
finally:
# Always close the file handle after use
    print('The FINALLY block ALWAYS runs')
    print('The finally block is used to tidy up')
    if names_tuple:
        names_tuple = None
#     if statement asking if the variable is empty (which it isn't).
#       assigning variable to None, which is null (not false/0/empty)
# this printed. Finally will run if none of the other exceptions define the error or even if they do
# this will always run
print('After exception handling is finished.. the programme can continue')
# the programme will continue to run after the finally loop so this printed