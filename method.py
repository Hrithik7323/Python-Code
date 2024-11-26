student = {
    "name" : "Hrirhik kumar",
    "subjects" : {
        "phy" : 65,
        "chem" : 78,
        "math" : 50
    }
}

print(list(student.keys()))

print(list(student.values()))

print(list(student.items()))

pairs = list(student.items())
print(pairs[0])

print(student["name"])
print(student.get("name"))


student.update({"city" : "Bihar"})
print(student)
