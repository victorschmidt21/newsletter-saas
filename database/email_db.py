from database.database import supabase

class EmailDB:
    def __init__(self):
        pass

    def getEmail(self):
        emails = []
        response = (
            supabase.table("users")
            .select("email")
            .execute()
        )
        for email in response.data:
            emails.append(email['email'])

        return emails