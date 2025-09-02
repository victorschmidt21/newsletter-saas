from database.database import supabase

class EmailDB:
    def __init__(self):
        pass

    def getManyEmails(self):
        emails = []
        response = (
            supabase.table("users")
            .select("email")
            .execute()
        )
        for email in response.data:
            emails.append(email['email'])

        return emails
    
    def createEmail(self, email: str):
        response = (
            supabase.table("users")
            .insert({'email': email})
            .execute()
        )
        print(response)
        return
    
    def getEmail(self, email: str):
        response = (
            supabase.table("users")
            .select('email')
            .eq("email", email)
            .execute()
        )
        return response.data
