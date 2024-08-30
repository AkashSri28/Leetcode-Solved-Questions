class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            name, domain = email.split('@')
            username = name.split('+')[0].replace('.', '')
            unique_emails.add(username+'@'+domain)
            
        return len(unique_emails)
        