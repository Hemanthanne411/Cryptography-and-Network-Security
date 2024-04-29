#key should be 3x3 matrix size i.e GYBNQKURP
#message should be of 3-size i.e ACT
#create a key_matrix(3x3) and also a message_matrix(3x1)
import numpy as np

def main():
    message=str(input("Enter the message to encrypt : "))
    key=str(input("Enter the key for encryption : "))
    
    #matrix
    
    key_matrix=[[0]*3 for i in range(3)]
    message_matrix=[[0] for i in range(3)]
    
    cipher_matrix=[[0] for i in range(3)]
       

    for i in range(3):
        message_matrix[i][0]=ord(message[i]) - 65
        
    x=0
    for i in range(3):
        for j in range(3):
            key_matrix[i][j]=ord(key[x])- 65
            x+=1
    #print(key_matrix)
    #print(message_matrix)
    
    #product of matrices
    cipher_matrix=np.dot(key_matrix,message_matrix)
    
    cipher_matrix=cipher_matrix% 26
    cipher_text=[]
    for i in range(3):
        cipher_text.append(chr(cipher_matrix[i][0]+65))
    
    
    print("the encrypted message is : " + "".join(cipher_text))
    
    
        
        
    
    
    
if __name__=="__main__":
    main()