# In the previous exercise, we retrieved the first, fourth, and last list elements to isolate the rating data. We can also retrieve the first three list elements to isolate the pricing data:

# img

# Instead of selecting element by element, we can use a syntax shortcut:

# img

# When we select the first n elements (n stands for a number) from a list named a_list, we can use the syntax shortcut a_list[0:n]. In the example above, we needed to select the first three elements from the list row_3, so we used row_3[0:3].

# When we selected the first three elements, we sliced a part of the list. For this reason, we call the process of selecting a part of a list list slicing.

# There are many ways that we might want to slice a list:

# img

# To retrieve any list slice we want, we do the following:

#     We identify the first and the last element of the slice.
#     We identify the index numbers of the first and the last element of the slice.
#     We retrieve the list slice we want by using the syntax a_list[m:n], where the following are true:
#         m represents the index number of the first element of the slice
#         n represents the index number of the last element of the slice plus one (if the last element has the index number 2, then n will be 3, if the last element has the index number 4, then n will be 5, and so on).

# img

# When we need to select the first or last x elements (x stands for a number), we can use even simpler syntax shortcuts:

#     a_list[:x] when we want to select the first x elements.
#     a_list[-x:] when we want to select the last x elements.

# img 


#INSTRUCTIONS
    # Select the first four elements from row_1 using a list slicing syntax shortcut. Assign the output to a variable named first_4_fb.
    # Select the last three elements from row_1 using a list slicing syntax shortcut. Assign the output to a variable named last_3_fb.
    # From row_5, select the list slice ['USD', 1126879] using a list slicing syntax shortcut. Assign the output to a variable named pandora_3_4.
    # Print first_4_fb, last_3_fb, and pandora_3_4 to see the results.

    # Select the first four elements from row_1 using a list slicing syntax shortcut. Assign the output to a variable named first_4_fb.
    # Select the last three elements from row_1 using a list slicing syntax shortcut. Assign the output to a variable named last_3_fb.
    # From row_5, select the list slice ['USD', 1126879] using a list slicing syntax shortcut. Assign the output to a variable named pandora_3_4.
    # Print first_4_fb, last_3_fb, and pandora_3_4 to see the results.

# answer
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
 
first_4_fb =  row_1[:4]
last_3_fb = row_1[-3:]
pandora_3_4 = row_5[2:4]

print(first_4_fb)
print(last_3_fb)
print(pandora_3_4)