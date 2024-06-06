from flask import render_template,flash, url_for, flash, redirect,request, jsonify,abort
from crop import app,db
from crop.forms import LoginForm,PostNewsForm,PostArticleForm,PostSurveyForm
from crop.models import Article,News,Survey
import numpy as np
import pandas as pd
import pickle
import requests

model = pickle.load(open('crop_model.pkl','rb'))

def forecast():
    params = { 'access_key': '2c5f0dfb9f9325266f1b4fb015c7bd7f', 'query': 'Yangon'}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    location = api_response['location']['name']
    return location

@app.route("/")
@app.route("/home")
def home():
    return render_template('public/home.html',title="Home")

@app.route('/crop/predict')
def crop_predict():
    return render_template('public/crop_predict.html')

@app.route('/crop/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('public/crop_predict.html', prediction_text='ထြက္ႏွုန္း (တင္း) {} '.format(output))    

@app.route("/crop")
def crop():
    return render_template('public/crop.html',title="Crop") 

@app.route("/crop/detail")
def crop_detail():
    return render_template('public/crop_detail.html',title="Crop Detail")        

@app.route("/region")   
def region():
    return render_template('public/region.html',title="Region") 

@app.route("/admin/home")
def admin_home():
    articles = Article.query.all()
    news = News.query.all()
    return render_template('admin/admin_home.html',title="Home",articles=articles,news=news)

@app.route("/admin/article")
def  admin_article():
    return render_template('admin/admin_article.html',title="Admin Article") 

@app.route("/admin/news")
def  admin_news():
    return render_template('admin/admin_news.html',title="Admin News") 
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'winleithwe@gmail.com' and form.password.data == 'wlt435':
            flash('You have been logged in!', 'success')
            return redirect(url_for('admin_home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('admin/admin_login.html', form=form,title="Login")

@app.route("/logout")
def logout():
    return redirect(url_for('home'))

@app.route("/article/post", methods=['GET', 'POST'])
def post_article():
    form = PostArticleForm()
    if form.validate_on_submit():
        article = Article(title=form.title.data, content=form.content.data)
        db.session.add(article)
        db.session.commit()
        flash('Your article has been created!', 'success')
        return redirect(url_for('admin_home'))
    return render_template('admin/post_article.html',form=form,legend='Post Article',title='New Post') 

@app.route("/article/<int:article_id>")
def article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('admin/admin_article.html', title=article.title, article=article)

@app.route("/article/<int:article_id>/update", methods=['GET', 'POST'])
def update_article(article_id):
    article = Article.query.get_or_404(article_id)
    form = PostArticleForm()
    if form.validate_on_submit():
        article.title = form.title.data
        article.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('admin_home'))
    elif request.method == 'GET':
        form.title.data = article.title
        form.content.data = article.content
    return render_template('admin/post_article.html', title='Update Article',
                           form=form, legend='Update Article')

@app.route("/article/<int:article_id>/delete", methods=['POST'])
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('admin_home'))

@app.route("/news/post", methods=['GET', 'POST'])
def post_news():
    form = PostNewsForm()
    if form.validate_on_submit():
        news = News(title=form.title.data, content=form.content.data)
        db.session.add(news)
        db.session.commit()
        flash('Your article has been created!', 'success')
        return redirect(url_for('admin_home'))
    return render_template('admin/post_news.html',form=form,legend='Post News',title='New Post') 

@app.route("/news/<int:news_id>")
def news(news_id):
    news = News.query.get_or_404(news_id)
    return render_template('admin/admin_news.html', title=news.title, news=news)

@app.route("/news/<int:news_id>/update", methods=['GET', 'POST'])
def update_news(news_id):
    news = News.query.get_or_404(news_id)
    form = PostNewsForm()
    if form.validate_on_submit():
        news.title = form.title.data
        news.content = form.content.data
        db.session.commit()
        flash('Your News has been updated!', 'success')
        return redirect(url_for('admin_home'))
    elif request.method == 'GET':
        form.title.data = news.title
        form.content.data = news.content
    return render_template('admin/post_news.html', title='Update News',
                           form=form, legend='Update News')

@app.route("/news/<int:news_id>/delete", methods=['POST'])
def delete_news(news_id):
    news = News.query.get_or_404(news_id)
    db.session.delete(news)
    db.session.commit()
    flash('Your News has been deleted!', 'success')
    return redirect(url_for('admin_home'))
    
@app.route("/survey/form", methods=['GET', 'POST'])
def post_surveyform():
    form = PostSurveyForm()
    if form.validate_on_submit():
        survey = Survey(soiltype=form.soiltype.data, croptype=form.croptype.data,seedquality=form.seedquality.data,seedrate=form.seedrate.data,fertilizertype=form.fertilizertype.data,manuretype=form.manuretype.data,landpreparation=form.landpreparation.data,sowingtype=form.sowingtype.data,fertilizeramt=form.fertilizeramt.data,herbicideamt=form.herbicideamt.data,insecticideamt=form.insecticideamt.data,manureamt=form.manureamt.data,address=form.address.data)
        db.session.add(survey)
        db.session.commit()
        flash('ဆာေဗးေဖာင္ သြင္းျပီးပာျပီ', 'success')    
        return redirect(url_for('post_surveyform'))
    return render_template('public/survey_form.html',form=form,legend='ဆာေဗးေဖာင္',title='Survey Form',survey_text='hello') 
    

@app.route("/home/article")
def home_article():
    articles = Article.query.all()
    return render_template('public/article.html',title="Home",articles=articles)

@app.route("/home/news")
def home_news():
    news = News.query.all()
    forecast()
    return render_template('public/news.html',title="Home",news=news)

@app.route("/survey/show")
def show_survey():
    surveys = Survey.query.all()
    forecast()
    return render_template('admin/admin_survey.html',title="Home",surveys=surveys)