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

@review.route('/reviews', methods=['POST'])
def data_post():
	if request.method == 'POST':
		data = request.form.to_dict();
	return data

@review.route('/movies', methods=['POST'])
def data_post():
    name = request.form['name']
	data = request.form.to_dict();
	if (Movie.query.filter_by(name=data["title"]).first() == None){

		data = Movie(data["id"], data["title"], data["description"], None);

		db.session.add(data)
		db.session.commit()  
	}
	else{console.log("poop")}
	
    return render_template('movie.html')