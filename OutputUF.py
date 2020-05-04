def text_maker(sen):
    Question_mark =("how", "when", "why")
    capitalized = sen.capitalize()
    if sen.startswith(Question_mark):
        return "{}?".format(capitalized)
    else:
       return "{}.".format(capitalized)
    

result = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        result.append(text_maker(user_input))

print(" ".join(result))

