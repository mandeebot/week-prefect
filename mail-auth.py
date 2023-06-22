from time import sleep
from prefect_email import EmailServerCredentials, email_send_message
from prefect import flow,task



@flow
def create_mail_block():
    credentials = EmailServerCredentials(
        username="adalihaskeservices@gmail.com",
        password="gbwrgicfveoxmtbx")
    credentials.save(name="email-auth-block", overwrite=True)

@flow
#creating a credentials bucket block
def example_email_send_message_flow(email_addresses: list[str]):
    email_server_credentials = EmailServerCredentials.load("email-auth-block")
    for email_address in email_addresses:
        subject = email_send_message.with_options(name=f"email {email_address}").submit(
            email_server_credentials=email_server_credentials,
            subject="Example Flow Notification using mail",
            msg="This proves email_send_message works!",
            email_to=email_address)

#example_email_send_message_flow(["mandeebot@hotmail.com"])

if __name__ == "__main__":
    create_mail_block()
    sleep(5)
    example_email_send_message_flow(["adalihaskeservices@gmail.com"])