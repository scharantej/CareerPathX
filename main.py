### **main.py**


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get user input from form
    career_goals = request.form['career_goals']
    skills = request.form['skills']
    interests = request.form['interests']

    # Generate personalized career recommendations
    recommendations = generate_recommendations(career_goals, skills, interests)

    # Redirect to results page
    return redirect(url_for('results', recommendations=recommendations))

@app.route('/results')
def results():
    # Get career recommendations from URL parameters
    recommendations = request.args.get('recommendations')

    # Render results page with recommendations
    return render_template('results.html', recommendations=recommendations)

@app.route('/plan')
def plan():
    # Generate personalized career plan
    career_plan = generate_career_plan()

    # Render plan page with career plan
    return render_template('plan.html', career_plan=career_plan)

def generate_recommendations(career_goals, skills, interests):
    # Placeholder function to generate personalized career recommendations
    return ['Software Engineer', 'Data Analyst', 'Project Manager']

def generate_career_plan():
    # Placeholder function to generate personalized career plan
    return '''
    **Strengths:**
    - Excellent communication skills
    - Strong problem-solving abilities
    - Passion for learning

    **Areas for Improvement:**
    - Public speaking skills
    - Time management

    **Step-by-Step Plan:**
    1. Take a public speaking course
    2. Use time management techniques
    3. Network with professionals in your field
    '''

if __name__ == '__main__':
    app.run(debug=True)
