from flask import Flask, render_template, request

app = Flask(__name__)

# medical questions and answers
questions = {
    'question1': 'Do you have a fever?',
    'question2': 'Are you experiencing cough and/or shortness of breath?',
    'question3': 'Are you experiencing headache and/or body aches?',
    'question4': 'Are you experiencing nausea and/or diarrhea?',
}

answers = {
    'answer1_yes': 'a viral infection.',
    'answer1_yes_cure': 'Rest, hydrate and take over-the-counter fever reducers.',

    'answer1_no': 'a bacterial infection.',
    'answer1_no_cure':  'Antibiotics may be required. Please see a doctor.',

    'answer2_yes': 'COVID-19.',
    'answer2_yes_cure': 'Isolate yourself and seek medical attention.',

    'answer2_no': 'a bacterial infection.',
    'answer2_no_cure':  'Antibiotics may be required. Please see a doctor.',

    'answer3_yes': 'the flu.',
    'answer3_yes_cure': 'Rest, hydrate and take over-the-counter flu medications.',

    'answer3_no': 'a bacterial infection.',
    'answer3_no_cure':  'Antibiotics may be required. Please see a doctor.',

    'answer4_yes': 'You may have food poisoning. ',
    'answer4_yes_cure':'Rest and hydrate. Seek medical attention if symptoms persist.',

    'answer4_no': 'a bacterial infection.',
    'answer4_no_cure':  'Antibiotics may be required. Please see a doctor.',
}

# home page
@app.route('/')
def index():
    return render_template('index.html')

# medical questionnaire
@app.route('/questionnaire')
def questionnaire():
    return render_template('questionnaire.html', questions=questions)

# results page
@app.route('/results', methods=['POST'])
def results():
    result = ''
    for key in request.form:
        result += request.form[key]

    if result == '1100':
        return render_template('results.html', result=answers['answer1_yes'], cure = answers['answer1_no_cure'])
    elif result == '1110':
        return render_template('results.html', result=answers['answer2_yes'],cure = answers['answer2_yes_cure'])
    elif result == '1001':
        return render_template('results.html', result=answers['answer3_yes'], cure = answers['answer3_yes_cure'])
    elif result == '1011':
        return render_template('results.html', result=answers['answer4_yes'], cure = answers['answer4_yes_cure'])
    elif result == '0010':
        return render_template('results.html', result=answers['answer1_no'],cure = answers['answer1_no_cure'])
    elif result == '0110':
        return render_template('results.html', result=answers['answer2_no'],cure = answers['answer2_no_cure'])
    elif result == '0001':
        return render_template('results.html', result=answers['answer3_no'], cure = answers['answer3_no_cure'])
    elif result == '0101':
        return render_template('results.html', result=answers['answer4_no'], cure = answers['answer4_no_cure'])
    else:
        return 'Invalid input'

if __name__ == '__main__':
    app.run(debug=True)
