subjects = ["Math", "Physics", "Biology", "Chemistry", "Language", "Geography"]

print(subjects)
subjectsremove = input("Какие предметы вам не нравятся? ").capitalize()
subjects.remove(subjectsremove)
print(subjects)