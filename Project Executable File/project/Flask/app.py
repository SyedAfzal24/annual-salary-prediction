from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='Template')
model = pickle.load(open('NewDoctorsPay (1).pkl', 'rb'))

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Service')
def Service():
    return render_template('Service.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        try:
            Speciality = request.form['speciality']
            Feel_Fairly_Compensated = request.form['fairly_compensated']
            Overall_Satisfaction = request.form['overall_satisfaction']
            Satisfied_Income = request.form['satisfied_income']
            Would_Choose_Medicine_Again = request.form['choose_medicine_again']
            Would_Choose_the_Same_Speciality = request.form['choose_same_speciality']
            Survey_Respondents_by_Speciality = request.form['survey_respondents']
            print('running')
            pred = [[float(Speciality), float(Feel_Fairly_Compensated), float(Overall_Satisfaction), float(Satisfied_Income), float(Would_Choose_Medicine_Again), float(Would_Choose_the_Same_Speciality), float(Survey_Respondents_by_Speciality)]]
            print(pred)
            output = model.predict(pred)
            print(output)

            return render_template('result.html', predict="The Predicted Salary of a Doctor is:" + str(output[0]))
        except Exception as e:
            print(f"Error: {e}")
            return render_template('result.html', predict="An error occurred during prediction.")
    else:
        return render_template('result.html', predict="Invalid request method.")

if __name__ == '__main__':
    app.run(debug=True)
