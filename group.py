
def groupThePeople(groupSizes):
    groups={}
    
    for i, size in enumerate(groupSizes):
        
        #if size not in groups add an empty list and append a new list with ID number
        if size not in groups:
            groups[size]=[]
            groups[size].append([i])
            
        # if the most currently appended list for key is less than size keep appending IDs to list
        elif len(groups[size][-1]) < size:
            groups[size][-1].append(i)
            
        # if the most currently append list for key is equal to size append a new list with id
        elif len(groups[size][-1]) == size:
            groups[size].append([i])

    # iterate through dictionary and add all values to a single answer list
    answer = []
    for key in groups:
        for item in groups[key]:
            answer.append(item)

    return answer