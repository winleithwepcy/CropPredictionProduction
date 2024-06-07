from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,validators,TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PostArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class PostNewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')  


SOILTYPE_CHOICES = [('fluvisols','ႏုန္းေျမ'),('gleysols','လယ္ေျမမ်ား'),('ferralsols','ဂ၀ံေျမ'),('arenosol','သဲကုန္းေျမ'),('vertisols','ေျမနီသဲ၀န္း'),('acrisols','ေတာင္ျမင့္ေျမနီ ေျမ၀ာ')]
CROPTYPE_CHOICES = [('paddy', 'စပား'),('corn','ေျပာင္း'),('peas','ပဲ'),('sugarcane','ျကံ')]
SEEDQUALITY_CHOICES = [('certified seed','Certified seed'),('hybrid seed','Hybrid Seed')]
FERTILIZERTYPE_CHOICES = [('npk','NPK'),('cmpd','Compound'),('urea','ယူရီးယား')]
MANURETYPE_CHOICES = [('manure','ေျမေဆြး'),('biosuper','Biosuper'),('faeces', 'ေနာက္ေခ်း')]
LANDPREPARATION_CHOICES = [('plough','ထယ်ခွဲ'),('harrow','ထွန်သည်')]
SOWINGTYPE_CHOICES = [('labour','အစိုကြဲ'),('machine','အခြောက်ကြဲ')]
ADDRESS_CHOICES = [('ayawaddy','ဧရာ၀တီတိုင္း'),('bago','ပဲခူးတိုင္း'),('shan','ရွမ္းျပည္')]

class PostSurveyForm(FlaskForm):
    soiltype = SelectField('ေျမဆီလြွာအမ်ိုးအစား', choices=SOILTYPE_CHOICES)
    croptype = SelectField('သီးႏွံအမ်ိဳးအစား', choices=CROPTYPE_CHOICES)
    seedquality = SelectField('မ်ိဳးေစ့အရည္အေသြး', choices=SEEDQUALITY_CHOICES)
    seedrate = 	IntegerField('ပ်ိဳးျကဲႏွုန္း', validators=[DataRequired()])
    fertilizertype = SelectField('ဓာတ္ေျမျသဇာအမ်ိုးအစား',choices=FERTILIZERTYPE_CHOICES)
    manuretype = SelectField('ေျမေဆြးအမ်ိုးအစား', choices=MANURETYPE_CHOICES)
    landpreparation = SelectField('ေျမျပင္နည္း', choices=LANDPREPARATION_CHOICES)
    sowingtype = SelectField('ပ်ိုးျကဲပံု',choices=SOWINGTYPE_CHOICES)
    fertilizeramt  = IntegerField('ဓာတ္ေျမျသဇာပမာဏ', validators=[DataRequired()])
    herbicideamt = IntegerField('ေပာင္းသတ္ေဆးပမာဏ', validators=[DataRequired()])
    insecticideamt = IntegerField('ပိုးသတ္ေဆးပမာဏ', validators=[DataRequired()])
    manureamt = IntegerField('သဘာ၀ေျမေဆြး', validators=[DataRequired()])
    address = SelectField('ေနရပ္', choices=ADDRESS_CHOICES)
    submit = SubmitField('အချက်အလက်များ ထည့်ရန်')  

     