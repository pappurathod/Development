'''
@Author: Pappu Rathod
@Date: 14/05/2022
@Last Modified by: Pappu Rathod
@Title: User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

uname = input("enter The User Name : ")
unamelength = len(uname)
if unamelength >= 3:
    print("Hello",uname,", ""How are you?")
else:
    print("User Name is not valid")