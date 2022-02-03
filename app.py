from flask import Flask, render_template, request
import age_calculator

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        age = age_calculator.get_age(start_date, end_date)
        if age:
            return render_template('index.html', has_results=True, results=age, correct_dates=True, start_date=start_date, end_date=end_date)
        else:
            return render_template('index.html', has_results=False, results=[], correct_dates=False, start_date=False, end_date=False)
    else:
        return render_template('index.html', has_results=False, results=[], correct_dates=True, start_date=False, end_date=False)


if __name__ == '__main__':
    app.run(debug=True)
