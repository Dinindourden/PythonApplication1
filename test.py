def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name= l_name.title()
    full_name = first_name + " " + last_name
    return full_name

full_name = format_name("JANI", "bARa")
print(full_name)
    