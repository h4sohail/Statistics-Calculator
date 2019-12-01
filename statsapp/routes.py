from flask import render_template, url_for, request
from statsapp import app
from statsapp.forms import DataForm, ArgForm
from statsapp.funcs import *

choices = { 'Go Home': 'home',
			'Mean' : 'mean',
			'Median': 'median',
			'Mode': 'mode',
			'Sample Variance': 'samplevariance',
			'Population Variance': 'populationvariance',
			'Sample Standard Deviation': 'samplesd',
			'Population Standard Deviation': 'populationsd',
			'Z-Score' : 'zscore',
			'Percentile' : 'percentile',
			'Interquartile Range' : 'iqr',
			'Five Number Summary' : 'fivenum'
}


def parse_form(page):
	return [float(i) for i in request.form['body'].split(',')]


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', 
    						choices=choices)


@app.route('/about')
def about():
	if request.method == 'POST':
	    return render_template('index.html', 
	    						title='about')


@app.route('/mean', methods=['GET', 'POST'])
def mean():
	form = DataForm()

	if form.validate_on_submit():
		print('yay?')
		result = get_mean(parse_form('/mean'))
		return render_template('mean.html', 
								choices=choices,  
								form=form, 
								operation='Mean', 
								result=result)

	return render_template('mean.html', 
							choices=choices, 
							form=form, 
							operation='Mean')


@app.route('/median', methods=['GET', 'POST'])
def median():
	form = DataForm()

	if form.validate_on_submit():
		result = get_median(parse_form('/median'))
		return render_template('median.html', 
								choices=choices, 
								form=form, 
								operation='Median', 
								result=result)

	return render_template('median.html', 
							choices=choices, 
							form=form, 
							operation='Median')


@app.route('/mode', methods=['GET', 'POST'])
def mode():
	form = DataForm()

	if form.validate_on_submit():
		try:
			result = get_mode(parse_form('/mode'))
			return render_template('mode.html', 
									choices=choices, 
									form=form, 
									operation='Mode', 
									result=result)

		except statistics.StatisticsError:
			return render_template('mode.html', 
									choices=choices, 
									form=form, 
									operation='Mode', 
									result='No unique mode')

	return render_template('mode.html', 
							choices=choices,  
							form=form, 
							operation='Mode')


@app.route('/samplevariance', methods=['GET', 'POST'])
def samvar():
	form = DataForm()

	if form.validate_on_submit():  
		result = get_sam_variance(parse_form('/samplevariance'))
		return render_template('samvar.html', 
								choices=choices, 
								form=form, 
								operation='Sample Variance', 
								result=result)

	return render_template('samvar.html', 
							choices=choices, 
							form=form, 
							operation='Sample Variance')


@app.route('/populationvariance', methods=['GET', 'POST'])
def popvar():
	form = DataForm()

	if form.validate_on_submit():	  
		result = get_pop_variance(parse_form('/populationvariance'))
		return render_template('popvar.html', 
								choices=choices, 
								form=form, 
								operation='Population Variance', 
								result=result)

	return render_template('popvar.html', 
							choices=choices, 
							form=form, 
							operation='Population Variance')


@app.route('/samplesd', methods=['GET', 'POST'])
def samsd():
	form = DataForm()

	if form.validate_on_submit():	  
		result = get_sam_sd(parse_form('/samplesd'))
		return render_template('samsd.html', 
								choices=choices, 
								form=form, 
								operation='Sample Standard Deviation', 
								result=result)

	return render_template('samsd.html', 
							choices=choices,
							form=form, 
							operation='Sample Standard Deviation')


@app.route('/populationsd', methods=['GET', 'POST'])
def popsd():
	form = DataForm()

	if form.validate_on_submit():  
		result = get_pop_sd(parse_form('/populationsd'))
		return render_template('popsd.html', 
								choices=choices, 
								form=form, 
								operation='Population Standard Deviation', 
								result=result)

	return render_template('popsd.html', 
							choices=choices, 
							form=form, 
							operation='Population Standard Deviation')


@app.route('/zscore', methods=['GET', 'POST'])
def zscore():
	form = ArgForm()

	if request.method == 'POST':
		result = get_zscore(float(form.x.data), float(form.mean.data), float(form.sd.data))
		return render_template('zscore.html', 
								choices=choices, 
								form=form, 
								operation='Z-Score',
								result=result)

	return render_template('zscore.html', 
							choices=choices, 
							form=form,
							operation='Z-Score')


@app.route('/percentile', methods=['GET', 'POST'])
def percentile():
	form = ArgForm()

	if request.method == 'POST':  
		result = get_percentile(parse_form('/percentile'), float(form.arg.data))
		percentile = int(form.arg.data)
		return render_template('percentile.html', 
								choices=choices, 
								form=form, 
								percentile=percentile,
								operation='Percentile', 
								result=result)

	return render_template('percentile.html', 
							choices=choices, 
							percentile='p', 
							form=form, 
							operation='Percentile')


@app.route('/iqr', methods=['GET', 'POST'])
def iqr():
	form = DataForm()
	if form.validate_on_submit():  
		result = get_iqr(parse_form('/iqr'))
		return render_template('iqr.html', 
								choices=choices, 
								form=form, 
								operation='Interquartile Range', 
								result=result)

	return render_template('iqr.html', 
							choices=choices, 
							form=form, 
							operation='Interquartile Range')


@app.route('/fivenum', methods=['GET', 'POST'])
def five_num_summ():
	form = DataForm()
	if form.validate_on_submit():
		result = get_five_num_summary(parse_form('/fivenum'))
		return render_template('fivenum.html', 
								choices=choices, 
								form=form, 
								operation='Five Number Summary', 
								result=result)

	return render_template('fivenum.html', 
							choices=choices, 
							form=form, 
							operation='Five Number Summary')

