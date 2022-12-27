from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
    """Form to submit input to the interpreter."""
    input = StringField('Input', validators=[DataRequired(), Length(min=1, max=20000)])
    submit = SubmitField('Run')
    reset = SubmitField('Reset')