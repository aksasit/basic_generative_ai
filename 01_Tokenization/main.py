import tiktoken

enc =  tiktoken.encoding_for_model("gpt-4o")

text = " Hi, My Name is Asit Kumar Sahoo"

tokens = enc.encode(text)

print("Encode: ", tokens)

decoded = enc.decode(tokens)

print("Decode: ", decoded)