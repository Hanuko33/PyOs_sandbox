try:
    args = tmp[1]
    if args in listdir(cur_dir):
        cur_dir = cur_dir + "/" + args
    elif args == "sandbox":
        pass
    else:
        print(args, "- no such directory")
    del args
except IndexError:
    cur_dir = "sandbox"
except NameError:
    pass
del tmp
