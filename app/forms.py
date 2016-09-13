from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class RegisterForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password')
    repeat_password = PasswordField('repeat_password')
    number = IntegerField('number')

    def validate(self):
        normal_validation = Form.validate(self)
        if not normal_validation:
            return False

        # Add custom validation
        if (self.password.data != self.repeat_password.data):
            self.password.errors.append("Le password non coincidono")
            return False

        return True
