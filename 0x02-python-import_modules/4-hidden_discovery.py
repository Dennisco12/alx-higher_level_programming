#!/usr/bin/python3
if __name__ == "__main__":
    """A funtion that prints all the names in the file hidden_4"""
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if name[0:2] == "__":
            continue
        print(name)

