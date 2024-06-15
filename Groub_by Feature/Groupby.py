import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("Courses.xlsx")
print(df)

groupbyCourses=df.groupby("Course")
print(groupbyCourses)
##Note that it will return the keys ordered by their alphapetic order
for courseNameAsKey,courseDataframeAsValue in groupbyCourses:
    print(courseNameAsKey)
    print(courseDataframeAsValue)
    print("\n\n")


#here where the Split Apply Combine Concepr is applied
print("\n\nMax values:\n")
print(groupbyCourses.max())

print("\n\nMin values:\n")
print(groupbyCourses.min())


print("\n\nThe describtion of the seperated dataframes\n")
print(groupbyCourses.describe())


print("\n\nThe plot of the seperated dataframes\n")
plt.plot(groupbyCourses)
plt.show()

