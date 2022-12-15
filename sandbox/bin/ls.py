list_dir = listdir(cur_dir)
print(str(list_dir).replace("[", "").replace("]", "").replace("'", "").replace(",", """
""").replace(" ", ""))
del list_dir
