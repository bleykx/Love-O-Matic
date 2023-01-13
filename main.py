from flask import Flask, jsonify
import random
from injector import Injector
from Utils import SentenceGeneratorUtil

app = Flask(__name__)

injector = Injector()
injector.binder.bind(SentenceGeneratorService, SentenceGeneratorService)
my_class = injector.get(MyClass)


romantic_sentences = [
    "Every time I see you, my heart skips a beat.",
    "I can't imagine my life without you.",
    "I love the way you make me feel.",
    "You are my everything.",
    "I never knew love could be this magical until I met you."
]

@app.route('/romantic_sentence', methods=['GET'])
def generate_romantic_sentence():
    sentence = random.choice(romantic_sentences)
    return jsonify(sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True)

