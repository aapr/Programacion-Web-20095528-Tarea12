from flask import Blueprint

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from app.models import Movie, Review

review = Blueprint('review', __name__)


@review.route('/')
def index():
    	return render_template('review.html')

@review.route('/get', methods=['GET'])
def data_get():
		name = request.args.get('name')
		result = Movie.query.filter_by(Name = name).first()
		return result.Name + " " + result.Description + " " + result.Poster

@review.route('/movie', methods=['POST'])
def data_post():
	if request.method == 'POST':
		name = request.form['name']
		data = Movie.query.filter_by(Name= name).first()

		if (data != None){

		result = (data.id, name, data.description, None)
		
		db.session.add(result)
		db.session.commit() 
		} 
	return render_template('movie.html')

@review.route('/review', methods=['POST'])
def data_post():
	if request.method == 'POST':
		name = request.form['name']
		data = Movie.query.filter_by(Name= name).first()
		
		if ( data != None){

			title = request.form['reviewTitle']
			description = request.form['Description']
			score = request.form['movieScore']

			result = Movie( name, title, description, None, score, None);

			db.session.add(result)
			db.session.commit()  
		}
		else{console.log("poop")}
	
	return render_template('review.html')