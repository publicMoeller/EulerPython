1. We need to be aware how a number systems of permutation would work (I do not want to count)
2. I will call our ordered elements (0,1...n)
3. For i to be the first digits we counted (|n|-1)! numbers before.
4. So we can recursively find out our number. The only important thing is to base our calculation on the order of the elements left and not on the order of elements that are availible in total

2,1,0 is 2! * 2 + 1! *1 = 5

we need to add 1 since the problem seems to call the ordered list 1 and not 0


 2*f(9)
 +6*f(8)
 +6*f(7)
 +2*f(6)
 +5*f(5)
 +1*f(4)
 +2*f(3)
 +2*f(2)
= 1000000
drawing from
0,1,2,3,4,5,6,7,8,9
means 
1672804539 
minus 1 should be
1672804395

After thinking it through and getting the wring answer lets do it the dumb way 3.2 million strings isn't too bad.

It was (2, 7, 8, 3, 9, 1, 5, 4, 6, 0)
So I only missed that there is a 0 when choosing from the set of remaining elements. 
Idea was correct though. And factorial number systems seem to be a thing.