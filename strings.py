# STRINGS
# We can define strings using single (‘ ‘) or double (“ “) quotes. 

course_title = "PYTHON FOR BEGINNERS"

# Accessing individual characters or slices
print("Expected O/P:H \nActual O/P:",course_title[3])
print("Expected O/P:S \nActual O/P:",course_title[-1])
# Slicing
print("Expected O/P:YTH \nActual O/P:",course_title[1:4])
# Slicing if you expect reversed output
print("Expected O/P:OHT \nActual O/P:",course_title[4:1:-1])
print("Expected O/P:SRE \nActual O/P:",course_title[-1:-4:-1])