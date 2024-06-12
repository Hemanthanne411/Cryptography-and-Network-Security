import hashlib

def calculate_sha512(message):
    #encode message as bytes before hashing 
    encoded_message=message.encode('utf-8')
    #calculated sha512 digest
    digest=hashlib.sha512(encoded_message).hexdigest()
    
    return digest

message="hello, this is a message"
sha512_digest=calculate_sha512(message)

print(f"message :{message}")
print(f"sha512 digest : {sha512_digest}")