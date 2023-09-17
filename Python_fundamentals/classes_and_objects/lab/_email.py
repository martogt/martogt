class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        is_sent = False

        def send():
            self.is_sent = True

        def get_info():
            return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {is_sent}"


emails = []
info = input()

while info != "Stop":
    sender, receiver, content = info.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    info = input()

send_emails = (emails)

for el in send_emails:
    emails[el].send()
