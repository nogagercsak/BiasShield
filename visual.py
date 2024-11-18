# Required Libraries
import subprocess
import sys

# Install required packages
subprocess.check_call([sys.executable, "-m", "pip", "install", "dash"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly"])

from flask import Flask, render_template
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Initialize Flask
server = Flask(__name__)

# Create the Dash App within Flask
app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

# Sample Data
data = pd.DataFrame({
    'Feature': ['Gender', 'Age', 'Income', 'Education'],
    'Bias_Score': [0.7, 0.3, 0.6, 0.4],
    'Mitigated_Score': [0.2, 0.1, 0.15, 0.1]
})

# Dashboard Layout
app.layout = html.Div([
    html.H1("BiasShield Dashboard", style={'textAlign': 'center'}),

    # Tiered Explanation Dropdown
    html.Label("Select Audience Level:"),
    dcc.Dropdown(
        id='audience-level',
        options=[
            {'label': 'Technical', 'value': 'TECH'},
            {'label': 'Non-Technical', 'value': 'NON_TECH'}
        ],
        value='TECH'
    ),

    html.Div(id='explanation-text', style={'margin': '20px'}),

    # Interactive Visualization
    html.Label("Bias Scores by Feature:"),
    dcc.Graph(id='bias-graph')
])

# Callbacks for Interactivity
@app.callback(
    [Output('explanation-text', 'children'),
     Output('bias-graph', 'figure')],
    Input('audience-level', 'value')
)
def update_dashboard(audience_level):
    # Audience-specific Explanations
    explanation = {
        'TECH': "Technical Explanation: This graph shows bias scores before and after mitigation. "
                "Bias_Score reflects systemic imbalances in the data, while Mitigated_Score indicates improvements.",
        'NON_TECH': "Non-Technical Explanation: This graph shows how BiasShield reduces unfairness in AI decisions."
    }

    # Plot Data
    fig = px.bar(pip install -r requirements.txt
        data,
        x='Feature',
        y=['Bias_Score', 'Mitigated_Score'],
        barmode='group',
        title="Bias Scores by Feature"
    )

    return explanation.get(audience_level, ""), fig


# Flask Route for Main Page
@server.route('/')
def index():
    return render_template('index.html')  # Ensure you have an `index.html` in your templates folder


# Run the Application
if __name__ == "__main__":
    server.run(debug=True)
