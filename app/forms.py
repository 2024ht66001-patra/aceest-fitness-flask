from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class WorkoutForm(FlaskForm):
    category = SelectField('Select Category', choices=[('Warm-up', 'Warm-up'), ('Workout', 'Workout'), ('Cool-down', 'Cool-down')], validators=[DataRequired()])
    exercise = StringField('Exercise', validators=[DataRequired()])
    duration = IntegerField('Duration (min)', validators=[DataRequired(), NumberRange(min=1, message='Duration must be a positive number.')])
    submit = SubmitField('Add Session')