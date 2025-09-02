from database.email_db import EmailDB

class EmailFetcher:
    emailDB = EmailDB()
    def __init__(self):
        pass

    def getEmails(self):
        emails = self.emailDB.getEmail()
        emails = ','.join(emails)
        return emails
    