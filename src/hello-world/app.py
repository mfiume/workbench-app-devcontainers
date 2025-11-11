"""
Hello World Flask Application for Verily Workbench
A simple web application demonstrating custom app deployment.
"""

from flask import Flask, render_template_string
from datetime import datetime
import os

app = Flask(__name__)

# HTML template for the hello page
HELLO_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Verily Workbench</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            text-align: center;
            padding: 40px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            max-width: 800px;
        }
        h1 {
            font-size: 3em;
            margin: 0 0 20px 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        .emoji {
            font-size: 4em;
            margin: 20px 0;
            animation: wave 1s ease-in-out infinite;
            display: inline-block;
        }
        @keyframes wave {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(20deg); }
            75% { transform: rotate(-20deg); }
        }
        .info {
            margin: 20px 0;
            font-size: 1.2em;
        }
        .timestamp {
            margin-top: 30px;
            font-size: 0.9em;
            opacity: 0.8;
        }
        .badge {
            display: inline-block;
            padding: 5px 15px;
            margin: 5px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            font-size: 0.9em;
        }
        .workspace-info {
            margin-top: 20px;
            padding: 15px;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="emoji">👋</div>
        <h1>{{ message }}</h1>
        <div class="info">
            <p>Running in <strong>Verily Workbench</strong></p>
            <div>
                <span class="badge">🐳 Docker</span>
                <span class="badge">🐍 Python {{ python_version }}</span>
                <span class="badge">🌶️ Flask</span>
                <span class="badge">☁️ Google Cloud</span>
            </div>
        </div>
        <div class="workspace-info">
            <p><strong>Environment:</strong> {{ environment }}</p>
            <p><strong>Hostname:</strong> {{ hostname }}</p>
        </div>
        <div class="timestamp">
            <p>Server time: {{ timestamp }}</p>
        </div>
    </div>
</body>
</html>
"""


@app.route('/')
def hello():
    """Render the hello world page"""
    import sys

    return render_template_string(
        HELLO_TEMPLATE,
        message="Hello, Verily Workbench! 🎉",
        python_version=f"{sys.version_info.major}.{sys.version_info.minor}",
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        environment=os.getenv('ENVIRONMENT', 'Workbench Custom App'),
        hostname=os.getenv('HOSTNAME', 'application-server')
    )


@app.route('/health')
def health():
    """Health check endpoint"""
    return {
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'message': 'Verily Workbench custom app is running!',
        'app': 'hello-world'
    }


@app.route('/api/info')
def info():
    """App information endpoint"""
    import sys
    return {
        'app_name': 'Hello World',
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'flask_version': '3.0.0',
        'platform': 'Verily Workbench',
        'timestamp': datetime.now().isoformat()
    }


if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Starting Hello World Flask App for Verily Workbench")
    print("=" * 60)
    print("📍 Local URL: http://localhost:8888")
    print("🏥 Health check: http://localhost:8888/health")
    print("ℹ️  Info endpoint: http://localhost:8888/api/info")
    print("=" * 60)
    print()

    # Run the Flask app on port 8888 (Workbench standard)
    app.run(
        host='0.0.0.0',
        port=8888,
        debug=True
    )
