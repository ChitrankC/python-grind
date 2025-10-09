import re

# -> str | None tells the tool or the developer that this funciton will either return the string or None if proper email is not taken are argument 
def get_domain_name(email:str) -> str | None: 
    match = re.search(r"@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", email)
    """
        This:
        Ensures the domain part has only valid characters
        Requires a . with at least two characters (like .com, .org, .in)
    """

    if match:
        return match.group(1)
    return None


email = input("enter the email string : ")
domain = get_domain_name(email)
print(domain)