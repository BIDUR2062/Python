def calculate_fine(book_name, borrowed_days, allowed_days, fine_per_day):
    if isinstance(borrowed_days,int) and isinstance(allowed_days, int):
        if not (borrowed_days<allowed_days):
            return {
                "book":book_name,
                "borrowed_days":borrowed_days,
                "Allowed_Days":allowed_days,
                "total_fine_days":borrowed_days-allowed_days,
                "fine":(borrowed_days-allowed_days)* fine_per_day
            }

        else:
            return{
                "book":book_name,
                "borrowed_days":borrowed_days,
                "Allowed_Days":allowed_days,
                "fine":0,

            }

    else:
        return "Error number shoud be in int"



print(calculate_fine("python",10,5,10)) # 50
print(calculate_fine("html",1,5,10)) # 50

print(calculate_fine("html",1.9,5,10)) # error number should in int
print(calculate_fine("html",1,"5",0)) # error number should in int