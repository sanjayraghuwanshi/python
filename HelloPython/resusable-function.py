def emoji_converter(message):
    words = message.split(" ")      #Splits string based on blank space.
    output = ""
    emojis = {
        ":)" : "😊",
        ":(" : "😞"
        }
    for word in words:
        output  += emojis.get(word, word) + " "
        #print(output)
    return output


message = input("> ")
#print(output)
print(emoji_converter(message))