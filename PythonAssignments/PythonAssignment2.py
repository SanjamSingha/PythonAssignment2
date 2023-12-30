# Exercise 1 Given a list as a parameter,write a function that returns a list of numbers that are less than ten. Use [1,11,14,5,8,9] as list
def numbers(input_list):
    return [num for num in input_list if num< 10]
input_list = [1, 11, 14, 5, 8, 9]
result_list = numbers(input_list)
print(result_list)

#Exercise 2 Write a function that takes in two lists and returns the two lists merged together and sorted
cakes=["Chocolate", "Vanilla", "Carrot", "Red Velvet"]  
cakes2=["Caramel","Cookies and Cream","Cheesecake"]
merged_list=(cakes + cakes2)
merged_list.sort()
print(merged_list)