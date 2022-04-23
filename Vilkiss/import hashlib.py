import hashlib


asd = u"dasda"
print(asd)
file_hach = hashlib.sha3_256()
file_hach.update(asd)
print(asd)
file_hach.digest(asd)
print(asd)