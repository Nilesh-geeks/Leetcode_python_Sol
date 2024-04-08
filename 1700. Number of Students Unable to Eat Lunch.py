Question ::1700. Number of Students Unable to Eat Lunch

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
 
 
Solution::

Complexity::

Time complexity:
O(N) 

Space complexity:
O(1)

Code::
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones =0
        for i in students:
            ones+=i
        
        zeroes = len(students) - ones 
        for i in range(0,len(sandwiches)):
            if sandwiches[i]==0 :
                if zeroes == 0:
                    return len(sandwiches)-i
                zeroes-=1
            else:
                if ones == 0 :
                    return len(sandwiches) - i
                ones-=1
        return 0    def maxDepth(self, s: str) -> int:
        l=c=0
        for i in s:
            if i=='(':
                l+=1;
            elif(i==')'):
                if c<l:
                    c=l
                l-=1
        return c


        

        