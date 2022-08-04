from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Flask initialisation
app = Flask(__name__)
# Create a new instance of a ChatBot
bot = ChatBot(
    'helpbot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
     database= mongodb_name,
     database_uri= mongodb_uri,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.70
        }
    ]
)

small_talk=['hi there!',
            'hi!','how are you?',
            'I\'m great!', 'glad to hear that, have you eaten?', 'fine, you?','i\'m happy talking to you',
            'i\m ok','what\'s wrong?','that sound\'s rough',
            'i feel awesome','excellent,glad to hear that',
            'not good','sorry to hear that',
            'have you eaten?','yes i did','what did you eat?', 'I ate'
            'that sounds delicious','where did you eat that?', 'i made it myself','that\'s amazing',
            'I cooked it', 'Wow! I wish I could cook', 'I went out to the hawker to eat that', 
            'do you go there often?','yes', 'do you like the place?', 'i do like it', 'what do you like about it?']
small_talk2=['hey how have you been my friend?','I\'m good how about you?',
             'im ok but life has been very boring, I miss going out.', 
             'I\'m very bored as well', 'want to go for coffee?','always cool',
             'nice!','glad to hear that','i am free on Wednesday, would you be free then?',
             'definitely','cool!','ok see you then?', 'see you', 'i like talking to you','that makes me really happy to hear that', 'goodbye','see ya, talk again soon!']
small_talk_what_did_u_do=['what did you do today?', 'oh nothing much',
            'Do you want me to suggest some activities?','sure', 'how about taking a walk outside, the weather is nice today',
            'I went out today', 'sounds fun!']
help_chat_call=['help me', 'how can i help?', 
                'how do i make a call?',
                'sure! i will explain step by step', 'let\'s start',
                'first, go back to the main chats page, by clicking on the top left arrow. then you will see the call call at top, click that and click into any contacts to make a call','thank you', 'is there anything else you need help with?', 'no, i\'m good','okay have a great day! chat with me if you need any help']
trainer = ListTrainer(bot)

for item in (small_talk, small_talk_what_did_u_do, small_talk2,help_chat_call):
    trainer.train(item)
    

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/get", methods=["GET","POST"])
def chatbot_response():
	msg = request.form["msg"]
	response = bot.get_response(msg)
	return str(response)

if __name__ == "__main__":
    app.run()
