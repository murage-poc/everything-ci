
def selection(list):
    """
    Given a list [23,45,3,23,5,67,5]
    Until the list is sorted:
       - For each element until there at last index:
            - Check for a smaller value to the right 
            - If found, swap
            - If not, continue with the outer loop
    """
    l = len(list)
    touched =False 
    for index,val in enumerate(list):
        for innerIndex in range(index,l):
            if  list[innerIndex]< val:
                #swap
                list[index]=list[innerIndex]
                list[innerIndex]=val
                touched=True
                break #break for next outer index
    # go over the list again to ensure it's sorted
    if touched:
        selection(list)
    return list


def bubble(list):
    """
    For each adjacent element, swap if not sorted.
    Repeat until sorted
    """
    last =len(list)-1
    touched = False
    for index,val in enumerate(list):
        if index ==last:
            continue
        elif val > list[index+1]:
            #swap
            list[index] = list[index+1]
            list[index+1] = val
            touched=True
    if touched:
       return bubble(list)    
    return list

def quick(list):
    """
    Choose a pivot index/element 
    """
    pass    


def merge(list):
    """Divide and conquer
    Divide the list into sub parts (min 2 elements)
    - Sort each part
    - Then merge two parts and sort the together untill all the parts are merged and sortedpyt
    """
    pass


print(selection([14,3,2,10,4,20,13,21,6]))

print(bubble([14,3,2,10,4,20,13,21,6]))



