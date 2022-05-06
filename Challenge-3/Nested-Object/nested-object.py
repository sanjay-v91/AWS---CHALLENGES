import json

def findkeys(node, kv): # Called findkeys Fuction
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
               yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x

if __name__ == '__main__':
    object = input("Enter the object\n") # Enter the Object 
    object1 = json.loads(object) # Converts the input String  to Dictionary     
    key = input("What key would you like to find?\n") # Input the key that we want find 
    key1 = key.replace("/", ""); #Example : Replaces the '/' in the input key and saving the key1 = xyz which is a string

    def split(key1): # Called Split function 
        return list(key1)


    #print(split(key1))
    key2 = split(key1) # Calls the split function to convert the word into list of letters like this ['x', 'y', 'z']

    key3 = key2[-1] # Takes the last value of the list , i.e key3 = z
    #print(key3)
    #print(list(findkeys(object1, key3)))
    s = list(findkeys(object1, key3)) # Passing the Object and Key3 as arguments to the "findkeys" function
    listToStr = ' '.join(map(str, s)) # Convert the list to string 
    print("The value is : " + listToStr) # Finally we convert ['a'] to 'a' (List to String)
