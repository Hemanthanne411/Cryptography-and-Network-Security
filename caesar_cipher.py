def main(): 
    text=str(input("Enter the text to be encrpted : ")) 
    key=int(input("Enter the key for encryption : ")) 
    encrypted_text=""
    
    for i in text: 

        if (i.isupper()):
            # chr() -- to convert to alpabet
            # ord() --to convert to integer version of alphabet
            # 65 -- the integer version for capital letter starts from (65-90)
            encrypted_text+=chr((ord(i)-65 + key)% 26 +65)
        elif (i.islower()):
            # lower case starts from 97-122
            encrypted_text+= chr((ord(i) + key - 97) % 26 + 97)
    print(f"the encrypted message : {encrypted_text}")
if __name__=="__main__":
    main()
