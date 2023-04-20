user_input = int(input("how many times do you want to try? (maximum should be 5) :"))
while 0<user_input<6:
    email = input('enter your email :')
    if len(email)>=6:
        if email[0].isalpha():
            if (('@') in email) and (email.count('@')==1) and (email.count('.')==1) and (('.') in email):
                if(email[-4]=='.' ) ^ (email[-3]=='.'):
                    if (' ') not in email:
                        if email.islower():
                            if ("!" not in  email)  and ("#" not in  email) and ("$" not in  email) and ("%" not in  email) and ("^" not in  email) and ("&" not in  email) and ("*" not in  email) and ("(" not in  email) and (")" not in  email) and ("-" not in  email) and ("=" not in  email) and ("+" not in  email) and ("," not in  email) and ("<" not in  email)and (">" not in  email)and ("?" not in  email)and ("/" not in  email) and (":" not in  email) and (";" not in  email) and ("'" not in  email) and ('''"''' not in  email):
                                if (('@gmail.com') in email):
                                    if ('.in' in email) or ('.com' in email):
                                        print('very good you enterd right email')
                                        break
                                    else:
                                        print("sorry, you have not entered .com or .in")
                                else :
                                    print("sorry, seems '@gmail' is not in your email ")
                            else:
                                print('sorry, you can not enter any not allowed character like !#$%')
                        else:
                            print('sorry, capital letter not allowed')
                    else:
                        print('sorry, space not allowed in email')
                else:
                    print("sorry, seems your '.' is not at right place else you are forgotting something")
            else:
                print("sorry, '@' or '.' is not exist at the right place one time")
        else:
            print('sorry, first character is not alphabet')
    else:
        print('sorry, your email letters are <6')   
    user_input=user_input-1
    print('you have left',user_input,'try')
else:
    ("sorry, you have many attempt")
