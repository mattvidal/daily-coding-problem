"""

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""

def ReturnAddUpToNumber(list, k):
    
    #list length. Just run this function if list.len > 1 
    if(len(list) > 1):

        #Sort list
        list.sort()

        #Scroll through list elements as long as their sum is <= to k
        for i in range(0, len(list)):
            for j in range(0, len(list)):
                if k == list[i] + list[j]:
                    return True 
        return False

    return None

list = [10, 15, 3, 7]
k = 17 
print(ReturnAddUpToNumber(list, k))