s = "Hello world thisisme2344"
new_s = "".join(filter(str.isalnum, s))
cleaned_s = "".join(filter(str.isalnum, s)).lower()
print(new_s)
print(cleaned_s)
