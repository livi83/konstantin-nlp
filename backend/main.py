from flask import Flask, jsonify, request
from flask_cors import CORS
from preprocess.Stats import Stats

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS

CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/', methods=['GET'])
def home():
    return jsonify('home')

#text stats
stats = Stats()


USER_INPUT = {
    'text':'',
    'length':'',
    'count_tokens':'',
    'normostana':'',
    'len_without_spaces':'',
    'count_whitespaces':'',
    'count_words':'',
    'unique_words':'',
    'ttr':'',
    'unique_words_list':'',
    'avg_word':'',
    'avg_sentence_chars':'',
    'avg_sentence_words':'',
    'num_sentences':'',
    'tags_chart':''
}
@app.route("/text-stats", methods=["POST","GET"])
def submitData():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        text = post_data.get('text')

        USER_INPUT.update({
            'text':text,
            'length':stats.total_len(text),
            'count_tokens':stats.count_tokens(text),
            'normostana':stats.normostrana(text),
            'len_without_spaces':stats.len_without_spaces(text),
            'count_whitespaces':stats.count_whitespaces(text),
            'count_words':stats.count_words(text),
            'unique_words':stats.unique_words(text)[0],
            'ttr':stats.unique_words(text)[1],
            'unique_words_list':stats.unique_words_list(text),
            'avg_word':stats.avg_word(text),
            'avg_sentence_chars':stats.avg_sentence_chars(text),
            'avg_sentence_words':stats.avg_sentence_words(text),
            'num_sentences':stats.num_sentences(text),
            'word_stats':stats.word_stats(text)[0],
            'tags_chart':stats.word_stats(text)[1],
        })
        response_object['message'] =  'OK'
    else:
        response_object['input'] = USER_INPUT
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()