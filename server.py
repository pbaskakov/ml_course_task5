from sanic import Sanic, response
from sanic.response import json
import spacy

app = Sanic()

@app.route('/', methods=['POST'])
async def procesing(request):
    nlp = spacy.load('xx')
    doc = nlp('{}'.format(request.body))
    resp = {'entities': []}
    for ent in doc.ents:
        ent_data = {'text': ent.text, 'type': ent.label_,
                    'start': ent.start_char, 'end': ent.end_char}
        resp['entities'].append(ent_data)
    return json(resp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
