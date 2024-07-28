try:
    file = open("file.txt")
    a_dict = {"key": "value"}
    #print(a_dict["not_a_key"])
except FileNotFoundError:
    open("file.txt", mode="w")
except KeyError as error_message:
    print(f" The key {error_message} does not exist ! ")
else:
    print("what else do you want ? ")
finally:
    raise KeyError