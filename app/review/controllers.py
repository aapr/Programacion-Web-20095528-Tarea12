from flask import Blueprint

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from app.models import Movie, Review
import os, urlib.request

review = Blueprint('review', __name__)


@review.route('/')
def index():
	return render_template('review.html')

@review.route('/', methods=['GET'])
def getAllReview():
	if request.method == 'GET':
		data = []
		for i in Review.query.all():
			data.append(i.serialize())
		result = jsonify(data)
		return result

@review.route('/', methods=['GET'])
def getAllMovies():
	if request.method == 'GET':
		data = []
		for i in Review.query.all():
			data.append(i.serialize())
		result = jsonify(data)
		return result

@review.route('/', methods=['GET'])
def getMovieByName():
	if request.method == 'GET':
		name = request.form['name']

		if Movie.query.filter_by(Name = name).startswith() > 0:
			data = Movie.query.filter_by(Name = name).startswith()
			result = jsonify(data.serialize())
			return result
		else:
			return render_template('review.html')

 

		
	return render_template('movie.html')

@review.route('/', methods=['POST'])
def postFormData():
	if request.method == 'POST':
		name = request.form['name']

		if Movie.query.filter_by(Name = name).count() > 0{
			data = Movie.query.filter_by(Name = name).first()

			title = request.form['reviewTitle']
			description = request.form['Description']
			score = request.form['movieScore']

			result = Review( title, description, score, None, None, data.id);

			db.session.add(result)
			db.session.commit()  
		}
		
	return render_template('review.html')

@review.route('/', methods=['POST'])
def postFormData():
	if request.method == 'POST':
		name = request.form['name']
		
		if Movie.query.filter_by(Name = name).count() == 0{
			
			poster = request.form['poster']

			try:
				f = open('app/static/posters/' + name + '.jpg','wb')
				with urllib.request.urlopen(poster) as url:
                    s = url.read()
				f.write(s)
				f.close()
				localPoster = '_' + name + '.jpg'
			except:
				localPoster = ''

			description = request.form['Description']

			result = Movie( name, description, localPoster);

			db.session.add(result)
			db.session.commit()  
		}
	 
	return render_template('movie.html')

