#!/usr/bin/env python
import os

from flask import Flask, render_template, request

from plainform import *


app = Flask(__name__)

_theme_dir = os.path.join(os.path.dirname(__file__), 'static', 'css', 'themes')
themes = [
    (theme, color[:-4])
    for theme in os.listdir(_theme_dir)
    for color in os.listdir(os.path.join(_theme_dir, theme))
    if color.endswith('.css')]


class Form(Form):
    name = StringField('Name', class_='class', data_string='data')
    password = PasswordField('Password')
    check1 = BooleanField('Check 1')
    check2 = BooleanField('Check 2')
    radio = RadioField(
        'Choice', choices=[('radio1', 'Radio 1'), ('radio2', 'Radio 2')],
        default='radio2')
    select = SelectField(
        'Super choice', choices=[
            ('select1', 'Select 1'), ('select2', 'Select 2')])
    multiselect = SelectMultipleField(
        'Mega choice', choices=[
            ('select1', 'Select 1'), ('select2', 'Select 2')])
    checklist = CheckboxListField(
        'Hyper choice', choices=[
            ('select1', 'Select 1'), ('select2', 'Select 2')])
    button = ButtonField('Useless button')
    image = FileField('Image')
    hidden = HiddenField('Ghost')
    textarea = TextAreaField('Long text')
    html = HTMLField('HTML')
    search = SearchField('Search')
    phone = TelField('Phone')
    color = ColorField('Color')
    url = URLField('URL')
    email = EmailField('Email')
    date = DateField('Date')
    datetime = DateTimeField('Date and Time')
    datetimelocal = DateTimeLocalField('Local Date and Time')
    integer = IntegerField('Integer')
    decimal = DecimalField('Decimal')
    integerrange = IntegerRangeField('Integer Range')
    decimalrange = DecimalRangeField('Decimal Range')
    submit = SubmitField('Try!')


@app.route('/', methods=['GET', 'POST'])
@app.route('/<path:theme>', methods=['GET', 'POST'])
def index(theme=None):
    form = Form(request.form, attributes={'class': 'form'})
    return render_template(
        'index.html', themes=themes, theme=theme, form=form())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
