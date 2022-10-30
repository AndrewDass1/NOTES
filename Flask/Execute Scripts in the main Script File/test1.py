from flask import Flask

import test2 #as ...
# Can write test2 as so below can write the new name .run_a_function
# run_a_function that was defined in test2 and now being called

app = Flask(__name__)

@app.route("/")
def run_test2():
    return test2.run_a_function