def fomat_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


print(fomat_name("SujAN","PRADHAN"))