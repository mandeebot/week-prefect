from time import sleep
from prefect_email import EmailServerCredentials, email_send_message
from prefect import flow,task



@flow
#creating a mail credentials block for prefect server
def create_mail_block():
    credentials = EmailServerCredentials(
        username="testmail@gmail.com",
        password="234535")
    credentials.save(name="email-auth-block", overwrite=True)

@flow
#creating a credentials bucket block
def send_mail_flow(email_addresses: list[str]):
    email_server_creds = EmailServerCredentials.load("email-auth-block")
    for email_address in email_addresses:
        subject = email_send_message.with_options(name=f"email {email_address}").submit(
            email_server_credentials=email_server_creds,
            subject="Example Flow Notification using mail",
            msg="This proves email_send_message works!",
            email_to=email_address)

#send_mail_flow(["mandeebot@hotmail.com"])

if __name__ == "__main__":
    create_mail_block()
    sleep(5)
    send_mail_flow(["adalihaskeservices@gmail.com"])