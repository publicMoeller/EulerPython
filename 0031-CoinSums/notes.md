# First thoughts.
1. Knapsacks are somewhat hard usually, but this one is basically cheating because:
    - We have arbitrary amount of all objects
    - we have a unit that divides our total space AND every other unit. We can always fill up.
2. This allows us to enumerate all solutions by always filling up to the max before going to the next unit. Remembering the last solution up to the point where we stopped having a choice allows to find the next one easily. 
# On second thought
1. we should probably use dynamic programming instead of making entropy. 
2. If we have already calculated how many options there are to fill up the remaining amount, we just calculate the number by adding.
3. Effectively this will lead to us making one choice per £amount because we already calculated all smaller ones.

2ct 
choose 2ct --> done
chosse 1ct --> 1ct remaining, we calculated that, it's 1

--> 2 options

3ct
choose 1ct --> 2 options for 2
choose 2ct --> 1 option for 1

4. Problem: Like this we are counting ordered sets assuming (1,2) != (2,1)
5. The problem is small enough to just enumerate, but I want to do something not shamefully inefficient, something that would work for larger amounts.
6. We can do the above but for restricted choices. How many options are there to fill x with coins not larger than y. Then we can use the last choice as the largest allowed coin, therefore ensuring that our choices are ordered. This results in the same outcome as ordering and deleting double entries.

3ct
choose 1ct --> 2ct remaining, 1 possibility to fill with coins from (1ct)
choose 2ct --> 1 ct remaining, 1 possibility to fill with coins form (2ct,1ct)

then we sum up to create a table for 3ct: (1ct) = 1,(2ct,1ct) = 2 , all other sets = 2 

# Solution I acutally used:

1. Build a lookup table line by line. Line number is ct amount
2. colums show possibilites to divide the amount with coins not larger than 1ct, 2ct,5ct...
3. Result is therefore in line 200 the rightmost number.
4. It should wort with other coins as long as a 1ct is in the mix.
5. It gives the correct answer for 100£ or MAXAMOUNT = 10000 