# masking email like H********@gmail.com
import re
def mask_email (email: str) -> str | None:
     #captures whatever is before @ in group 1 and after @ in group 2 similar to slicing 
    re_email = re.search(r"(.+)@(.+)", email)
    #handling the invalid email cases 
    if not re_email:  
        return None  
    print("processing using the re library : ")
    username = re_email.group(1)
    domain = re_email.group(2)

    re_masked_email = username[0] + '*'*(len(username)-1)
    print(f"{re_masked_email}@{domain}")

    print("now processing the same request using slicing and find function ()")

    mail_index = email.find("@")
    if mail_index == -1:
        return None
    mail_username = email[:mail_index]
    mail_domain = email[mail_index+1:]
    masked_mail = mail_username[0] + '*'*(len(mail_username)-1)
    print(f"{masked_mail}@{mail_domain}")
    print("done")

email = input("enter the email valid one : ")
mask_email(email)