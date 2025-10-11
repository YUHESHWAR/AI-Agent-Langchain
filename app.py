from flask import Flask, request, jsonify
from flask_cors import CORS
from main import agent_executor, parser

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')

    if not query:
        return jsonify({'error': 'Query is required'}), 400

    try:
        raw_response = agent_executor.invoke({"query": query})
        output_string = raw_response.get('output', '')
        structured_response = parser.parse(output_string)
        summary = structured_response.summary
        return jsonify({'summary': summary})
    except Exception as e:
        print("Error processing request:", e)
        return jsonify({'error': 'Failed to process the request'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
