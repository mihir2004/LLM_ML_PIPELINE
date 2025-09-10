from flask import Flask, request, jsonify, render_template
from modules.ingest import load_csv, load_db
from modules.qc import run_qc_report
from modules.cleaning import suggest_cleaning
from modules.pipeline import generate_pipeline, regenerate_pipeline

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    source_type = request.form.get('source_type')
    if source_type == 'csv':
        file = request.files.get('file')
        df = load_csv(file)
    else:
        uri = request.form.get('db_uri')
        df = load_db(uri)
    report = run_qc_report(df)
    return jsonify(report)

@app.route('/cleaning/suggest', methods=['POST'])
def cleaning_suggest():
    data = request.get_json()
    qc = data['qc_json']
    sample = data['sample_records']
    suggestions = suggest_cleaning(qc, sample)
    return jsonify(suggestions)

@app.route('/pipeline/generate', methods=['POST'])
def pipeline_generate():
    data = request.get_json()
    schema = data['schema_json']
    bundle = generate_pipeline(schema)
    return jsonify(bundle)

@app.route('/pipeline/regenerate', methods=['POST'])
def pipeline_regenerate():
    data = request.get_json()
    original = data['original_pipeline']
    tweak = data['tweak_instruction']
    updated = regenerate_pipeline(original, tweak)
    return jsonify(updated)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv('PORT', 5000)))
