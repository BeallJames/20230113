 # string concatenation

youtuber = "james" # string variable

# 3 methods

# # 1
# print("subscribe to " + youtuber)
# # 2
# print("subscribe to {}".format(youtuber))
# #3 
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous person: ")

madlib = f"computer programming is so {adj}! \
it makes me so excited all the time becuase i love to {verb1}. \
stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)