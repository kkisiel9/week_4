names_tuple = "Rod", "Jane", "Freddy"

try:
    print("####### TRY #######")
    print("The TRY block attempts to run")
    print(f"original Tuple: {names_tuple}")
    names_Sorted_As_lit = sorted(names_tuple)
    print(names_Sorted_As_lit)
    names_Sorted_As_lit.append("Bungle")
    print("Added Bungle:", names_Sorted_As_lit)
    print("Attempt to manipulate the tuple...")
    names_tuple[0] - "Zippy"
    print("is this code reached?")
except FileNotFoundError as error:
    print("###### Except: FileNotFoundError ######")
    print("The except/catch block only runs if this error happens")
    print(f"The following file cannot be found: {error.filename}. Please try another file.")
except TypeError as error:
    print("##### Except: TypeError ######")
    print("Oh dear, that is not allowed on that type")
    print(error)
except Exception as error:
    print("##### EXCEPT: Exception #######")
    print("oh dear, that is not allowed on that type")
    print(error)
finally:
    print("the finnally block always runs")
    print("the finally block is used to tidy up")
    if names_tuple:
        names_tuple = None

print("after exception handling is finished... the programme can conitnue")