# IS211_Assignment12

Hi Professor,

I didn't want to spend that much more time on this as I know you have other assignments to grade. Apologizes on this being minimally styled (it's atrocious looking). Everything should work with the exception of the view for anonimized students, you can use the browser to test it though as the route should work. The only thing that doesn't is the button from the login screen. I ran out of time implementing it. Also, I forgot to add a logout button, but it does work from the browser to remove the session information. 

Please let me know if any issues,

Tim


# Note to myself
# Running the assignment

- If the virtual environment is not created already create one and activate it in the terminal of the IS2111_Assignment12 folder: 
  - `python-m venv venv` and `source venv/bin/activate`
- Installing dependencies: they are in the requirements.txt file run `python -m pip install -r requirements.txt`
- If you need to seed the database run `python load_seed_data.py` from the terminal inside of the IS211_Assignment12 folder
- To run the actual flask application I believe it's gonna be `python flask_routes.py` in the terminal
- To deactivate the virtual environment in use: `deactivate`

Needed

- [x] Session/Login middleware to apply security
- [x] Check that all views are available
- [x] Check that all routes are in
- [x] Fill out route logic
- [-] Update view to show route arguments

Further

- [x] Confirm security works on all routes
- [x] Confirm that try/except is used
- [] If time set up testing, probably won't be time
- [-] Optional functionality if time
- [] CSS if time

Tier 1

Routes

- [x] /login route
- [x] /dashboard route
- [x] /student/add route - link from dashboard
- [x] /quiz/add - link from dashboard
- [x] /student/<'id'> - update to dashboard, possibly another link
- [x] /results/add route - link from dashboard
- [-] /quiz/<'id'>/results - optional
- [] use SQL JOINS to expand the output to show not only the results output but also the date the quiz was given and the subject of the quiz - optional
- [] Allow the application to delete quizzes, students, and their results
- [] Check all flashes


Issues

- [] Anonimized student grades is working but needs a form to ask for which quiz result.


# NOTE TO MYSELF:

Virtual Environment Setup:
python-m venv venv

Activate Environment Setup:
source venv/bin/activate

Deactivate Environment Setup:
deactivate

Pin requirements:
python -m pip freeze > requirements.txt

Install requirements:
python -m pip install -r requirements.txt