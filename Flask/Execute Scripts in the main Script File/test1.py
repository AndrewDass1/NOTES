from flask import Flask

import test2 #as ...
# Can write test2 as ... where ... is a new name, so down below can write the new name "".run_a_function
# run_a_function was the name of the function that was defined in test2 and now it is being called in the format: filename.functionname

app = Flask(__name__)

@app.route("/")
def run_test2():
    return test2.run_a_function
