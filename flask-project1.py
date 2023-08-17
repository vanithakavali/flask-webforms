from flask import Flask,render_template,request
from flask_wtf import Form

from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


FAI=Flask(__name__)

class NameForm(Form):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField()

@FAI.route('/webforms',methods=['GET',"POST"])
def webforms():
    NF=NameForm()

    if request.method=='POST':
        form_data=NameForm(request.form)

        if form_data.validate():
            return form_data.data
        

    return render_template('webforms.html',NF=NF)

@FAI.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        fd=request.form
        return str(fd)

    return render_template('htmlforms.html')


if __name__=='__main__':
    FAI.run(debug=True)