#https://youtu.be/DnvWAd-RGhk
#return the last one that repeats

list = [0, 1, 4, 4, 4, 5, 6, 9, 10]
target = 9
def binarySearch(list,target):
   firstIndex = 0
   lastIndex = len(list) - 1
   while lastIndex >= firstIndex:
       mediumIndex = firstIndex + (lastIndex - firstIndex)//2
       mediumValue = list[mediumIndex]
       if mediumValue == target:
           return mediumIndex
       elif target < mediumIndex:
           lastIndex = mediumIndex - 1

       else:
           firstIndex = mediumIndex + 1
   return None

print(binarySearch(list,target))


