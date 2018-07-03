# mp = ["sadness","depress",18,9,2002,["emoness","anti-social"]]
# dictionary/object/map
# key : value
# create new dictionary
person = {
    "name": "MP",
    "personality": "anti-social",
    "age": 16,
    "date of birth":18
}
# print (person)

# add/update new key value
# person["hometown"]= "HN"
# print (person)
# person["age"]= 15
# print (person)
# for key in person.keys():
#     print(key)
# read
# print(person["personality"])
# for key in person.keys():
#     print(person[key])
# for value in person.values():
#     print(value)
# for key in person.keys():
#     print(key,end ="\t")
key = "school"
if key in person:
    print (person[key])
else:
    print ("not found")
