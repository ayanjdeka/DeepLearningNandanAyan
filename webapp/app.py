from flask import Flask, render_template, request, redirect, url_for
import os
import random
import pandas as pd
from sklearn.metrics import classification_report

app = Flask(__name__)

# Load image paths
image_paths = []
for class_name in ['positive', 'negative']:
    class_dir = os.path.join('static', 'generated_images', class_name)
    for img_name in os.listdir(class_dir):
        if img_name.lower().endswith((".jpg", ".jpeg", ".png")):
            image_paths.append((f"{class_name}/{img_name}", class_name))

# Shuffle images at app startup
random.shuffle(image_paths)
index_state = {'current': 0}

@app.route('/')
def index():
    if index_state['current'] >= len(image_paths):
        return redirect(url_for('evaluate'))

    img_path, true_label = image_paths[index_state['current']]
    return render_template('index.html', img_path=img_path, true_label=true_label)

@app.route('/submit', methods=['POST'])
def submit():
    selected_label = request.form['label']
    true_label = request.form['true_label']
    with open('results.csv', 'a') as f:
        f.write(f"{true_label},{selected_label}\n")
    index_state['current'] += 1
    return redirect(url_for('index'))

@app.route('/evaluate')
def evaluate():
    if not os.path.exists('results.csv'):
        return "No results to evaluate."

    df = pd.read_csv("results.csv", names=["true_label", "predicted_label"])
    report = classification_report(df["true_label"], df["predicted_label"], target_names=["positive", "negative"], output_dict=False)
    return f"<h1>Evaluation Complete</h1><pre>{report}</pre><a href='/'>Restart</a>"

@app.route('/reset')
def reset():
    index_state['current'] = 0
    if os.path.exists("results.csv"):
        os.remove("results.csv")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
