from database import supabase

def getEmails():
    emails = []
    response = (
        supabase.table("users")
        .select("email")
        .execute()
    )
    for email in response.data:
        emails.append(email['email'])
        
    emails = ','.join(emails)
    print(emails)
    return emails