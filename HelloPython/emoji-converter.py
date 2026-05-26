message = input(">")
words = message.split(' ')      #Splits string based on blank space.
output = ""
emojis = {
    ":)" : "😊",
    ":(" : "😞"
    }
for word in words:
    output  += emojis.get(word, word) + " "
print(output)