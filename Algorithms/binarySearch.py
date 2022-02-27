#https://youtu.be/DnvWAd-RGhk


#return the last one that repeats

list = [0, 1, 4, 4, 4, 5]
target = 4
def binarySearch(list,target):
   firstIndex = 0
   lastIndex = len(list) -1
   while lastIndex >= firstIndex:
       mediumIndex = firstIndex + (lastIndex - firstIndex)//2
       mediumValue = list[mediumIndex]
       if mediumValue == target:
           if list[mediumIndex] == list[mediumIndex + 1]:
               counter = 0
               while list[mediumIndex] == list[mediumIndex + 1]:
                   counter = counter + 1
                   if list[mediumIndex] != list[mediumIndex + counter + 1]:
                       return mediumIndex + counter

       elif target < mediumIndex:
           lastIndex = mediumIndex - 1

       else:
           firstIndex = mediumIndex + 1
   return

print(binarySearch(list,target))


