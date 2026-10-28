from flask import Flask, render_template  # type: ignore[import-not-found]

app = Flask(__name__)

@app.route('/')
def home():
    # Pass your live Tableau story embed URL to the frontend template
    tableau_url = "https://public.tableau.com/views/Health360ComprehensiveHealthcareRiskAnalysis/Health360ExecutiveStory"
    return render_template('index.html', tableau_url=tableau_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)