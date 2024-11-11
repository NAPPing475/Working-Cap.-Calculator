from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serves the HTML file

@app.route('/calculate', methods=['POST'])
def calculate():
    # Parse JSON data from the POST request
    data = request.json
    tca = float(data.get('tca', 0))  # Total Current Assets
    ocl = float(data.get('ocl', 0))  # Other Current Liabilities

    # Perform the calculations
    wcg = tca - ocl
    min_nwc = tca * 0.25
    mpbf = (tca - min_nwc) * 0.75
    dp = mpbf

    # Return the calculated values as JSON
    return jsonify({
        'wcg': round(wcg, 2),
        'min_nwc': round(min_nwc, 2),
        'mpbf': round(mpbf, 2),
        'dp': round(dp, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
