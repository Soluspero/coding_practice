'''
Quick Sort Tutorial (100 Marks)
Finding Rank of Students

Rahul is one of the topper of IP University. He always secured good marks in each subject from last 2 years. Today, mid year results of a particular subject is announced he is curious in knowing his rank in class so he decided to make a rank list .

He collected data of all the students i.e. name, scholar number and marks of every student of his class. He started creating the rank list i.e student having maximum marks at the top and if two students are having same marks then the student having lexicographically smaller name comes first , if both name and marks of the student collide then student having smaller scholar number comes first.

Input Format

Input 1: It will be a double dimensional string array where:

First row will tell the total number of rows M which tells the total number of students in class.

Second row will tell the total number of columns

Next each consecutive N lines contains name , scholar number and marks scored in exam of each student.


Constraints
1 <= M <= 1000
1 <= length of name <= 10
1 <= scholar number <= 1000
0 <= marks <= 30

Output Format

It will be an double dimensional string array which shows the rank list of students as explained in input.

Sample TestCase 1
Input

5
3
arun 8 28
harshit 10 30
surya 7 26
satyam 27 6

Output

harshit 10 30
arun 1 28
arun 8 28
surya 7 26
satyam 27 6


'''