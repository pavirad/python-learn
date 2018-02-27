def find_recurring_char(inp_string):
    hash_table = {}
    for x in inp_string:
        if x in hash_table:
            return(x)
        else:
            hash_table[x] = 1
    return("Nothing Found!")

print(find_recurring_char("abca"))
