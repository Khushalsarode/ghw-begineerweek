from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Replace 'to' with the recipient's phone number (including country code) and 'from_' with your Twilio WhatsApp-enabled number
message = client.messages.create(
                              body='Hello from your Python script!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+1234567890'
                          )

print(f"WhatsApp message SID: {message.sid}")
