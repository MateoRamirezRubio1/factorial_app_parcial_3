from flask import Flask, render_template, request, abort
from utils.math_utils import calculate_factorial

app = Flask(__name__)

@app.route('/factorial/<int:number>')
def factorial(number):
    result = calculate_factorial(number)
    return render_template('result.html', number=number, result=result)

@app.errorhandler(404)
def not_found(error):
    return "<h1>404 - Not Found</h1><p>La página solicitada no existe.</p>", 404

if __name__ == '__main__':
    app.run(debug=True)
