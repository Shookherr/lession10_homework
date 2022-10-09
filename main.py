# Домашнее задание урок 10. Шумихин Алексей 09.10.22
from flask import Flask
import utilities

app = Flask(__name__)   # create an instance of the Flask class

data = utilities.load_candidates('candidates.json')  # get data from file


@app.route('/')
def page_main():

    page = '<pre>\n' + utilities.get_all(data) + '</pre>'
    return page


@app.route('/candidates/<int:pk>')
def page_candidates(pk):

    is_cand, str_page = utilities.get_by_pk(pk, data)

    if is_cand:
        url_pic = f'http://mypictures.me/{str(pk)}'
        page = f'<img src=\'({url_pic})\'>\n\n<pre>'
    else:
        page = '<pre>'

    page += str_page
    page += '</pre>'
    return page


@app.route('/skills/<skill>')
def page_skills(skill):

    page = '<pre>'
    page += utilities.get_by_skill(skill, data)
    page += '</pre>'
    return page


app.run()
