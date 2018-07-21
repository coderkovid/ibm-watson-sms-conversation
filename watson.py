import watson_developer_cloud
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route("/")
def index():
	return '<a href="/sms">SMS</a>'

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # Start our TwiML response
    from_number = request.values.get('From')
    country = request.values.get('FromCountry')
    message_body = request.values.get('Body')
    print(request.values)
    print('{} has sent a message saying {} from {}'.format(str(from_number), str(message_body), str(country)))
    service = watson_developer_cloud.AssistantV1(
    username = 'your_username', # replace with service username
    password = 'your_service_password', # replace with service password
    version = '2018-02-16'
          )
    workspace_id = 'your_workspace_id'
    user_input = str(message_body)
    context = {}
    while True:
            response = service.message(
                    workspace_id = workspace_id,
                    input = {
                    'text': user_input
                     },
            context = context
                    )

            if response['intents']:
                    print('Detected intent: #' + response['intents'][0]['intent'])

            # Print the output from dialog, if any.
            
            
            if response['output']['text']:
                    resp = MessagingResponse()
                    resp.message(str(response['output']['text'][0]))
                    return str(resp)

            # Update the stored context with the latest received from the dialog.
            context = response['context']

    # Prompt for next round of input.


    

    


  


app.run(debug=True)

