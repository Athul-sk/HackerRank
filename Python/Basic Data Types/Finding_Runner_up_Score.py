#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
#You are given n scores. Store them in a list and find the score of the runner-up.

n = int(input())
arr = map(int, input().split())
list=[]
for i in arr:
    list.append(i)    #adding the elements in the array to list
highest_score  = max(list)    #Finding the highest score in the list to remove it
while highest_score in list:
    list.remove(highest_score)  #removing the highest score to make the runner up as highest
print(max(list))                #printing the runnerup ( i.e the current highest in list)
