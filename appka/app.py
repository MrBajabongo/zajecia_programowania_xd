from random import choices
from flask import Flask, render_template, url_for, redirect 
import os 
import flask_wtf 
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, RadioField 
from wtforms.validators import DataRequired


app = Flask(__name__)
app.secret_key = '(:-:)'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/strona')
def strona():
    return "Y"

@app.route('/podstrona', methods=['GET', 'POST'])
def podstrona():
    name=20
    return render_template('podstrona.html', name=name)

@app.route('/jinja_fory')
def jinja_fory():
    lista = ["aaaaaa", "bbbbbbbbbbb", "cccccccccccc"]
    return render_template('jinja_fory.html', lista=lista)

@app.route('/jinja_ify')
def jinja_ify():
    nr = 2
    return render_template('jinja_ify.html', nr=nr)

#FORMS
@app.route('/forms', methods=["GET", "POST"])
def forms():

    form = X()
       
    if form.validate_on_submit():
       
        best_like_league = form.best_like_league.data
        like_football_team = form.like_football_team.data
        like_other_league = form.like_other_league.data
        place_in_league = form.place_in_league.data
        
        string = '{},{},{},{}\n'.format(best_like_league, like_football_team, like_other_league, place_in_league)
        
        save_forms(string)
        
        return redirect( url_for('form_result'))
    
    return render_template("forms.html", form=form)

@app.route('/form_result')
def form_result():
    return render_template("form_result.html")

#Save forms
def save_forms(string):
    if not 'data' in os.listdir():
        os.mkdir('data')
        if not 'forms_data.txt' in os.listdir('data'):
            os.system('touch forms_data.txt')
    with open('data/forms_data.txt', "a+") as f:
        f.write(string)
      


#Form
class X(FlaskForm):

    league = [
        ('Premie_League', 'Premier_league'),
        ('La_Liga', 'La_liga'),
        ('Bundesliga', 'Bundesliga'),
        ('Seria_A', 'Seria_A'),
        ('Ligue_1', 'Ligue_1'),
    ]
    place = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('inne', 'inne'),
    ]

    
    best_like_league = SelectField('Moja ulubiona liga piłkarska:', choices=league )
    like_football_team = StringField('Moja ulubiona drużyna z tej ligi:', validators=[DataRequired()])
    like_other_league = BooleanField('Lubisz jeszczę inną ligę ?')
    place_in_league = RadioField("Wytypuj miejsce w lidze: ", choices=place)
        
    button = SubmitField('OK')

if __name__ == "__main__":
    app.run(debug=True)
