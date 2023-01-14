from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length
from wtforms.widgets import TextArea

class InputForm(FlaskForm):
    """Form to submit input to the interpreter."""
    input = StringField('Input', widget=TextArea(), validators=[Length(min=1, max=30000)], render_kw={"rows": 5, "cols": 150})
    submit = SubmitField('Run')
