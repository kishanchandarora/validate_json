# validate_json
First I create a validateFamily function in which I perform valiatation  Validate all given families in JSON file. That every child should have age and parent or he should be the highest ancestor. Also, child age should not be greater than parent age. 
for that I use a recursion to read our json.file that is define open in global scope in python with help of module json
In this function we recursively call the child of member until all the data is read, I compare the child age with member age, if is more than a parent age I though an error 
with Failed message of child and parent namea. and also check that data does not contain the empty age and child does not exist without his parent existance.


second function insertFamily takes four arguments member, age, parent, name. The last three are taken by user input .
Now I perform the following action:
1. If data is already exist, data is not enter.
2. If data is not exist we check its position to fit in the correct position according to there parent value.
3. If parent are not match any of given data, we create a new object in the same json.file
All are done by recursion .
I open json file in write, So I can edit in the file easily.


Third function find_Ancestor_list1 and find_Ancestor_list2 I create a two function, to take two list out of it according to user input comparsion string, I perform backtacking with help of recursion and add item to the list accordingly to user input string .
Now, I check the two global list and find a common ancestors and least common ancestors in a two list, if a least common ancestor is found I print it, otherwise say does not belong to same family.





