from flask import Flask, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route('/compute')
def compute():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': [90, 85, 92]
    }
    df = pd.DataFrame(data)
    output_path = 'output/result.csv'
    os.makedirs('output', exist_ok=True)
    df.to_csv(output_path, index=False)
    return f"Data computed and saved to {output_path}"

@app.route('/download')
def download():
    return send_file('output/result.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
