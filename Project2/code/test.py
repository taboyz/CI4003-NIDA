while True:
    try:
        input_from_time = float(input("Enter from Time (24hrs format ex. 09.00):"))
        input_to_time = float(input("Enter to Time (24hrs format ex. 17.00):"))
        if input_from_time >= input_to_time :
            print ("From time must less than to time")
            continue
        else:
            break
    except:
        print ("Plase check you Time Format again")
        continue