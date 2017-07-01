# Twilio password: p__4___i___!!!

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd41e3f6bc65bbbf0d78c917603c7a45e"
# Your Auth Token from twilio.com/console
auth_token  = "54989cdff4e0c90f258fbcdf966f2dbd"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16263992552",
    from_="+18184234959",
    body="Hello from Python!")

print(message.sid)
