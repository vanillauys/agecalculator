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
            return render_template('index.html', has_results=True, results=age, correct_dates=True)
        else:
            return render_template('index.html', has_results=False, results=[], correct_dates=False)
    else:
        return render_template('index.html', has_results=False, results=[], correct_dates=True)


if __name__ == '__main__':
    app.run(debug=True)
