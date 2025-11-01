from flask import Flask, render_template, jsonify, request
from datetime import datetime
import os
from dotenv import load_dotenv
import logging

# Версия приложения
__version__ = '1.1.0'

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-key-change-in-production')

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Статистика в памяти (в production использовать БД)
stats = {
    'total_attempts': 0,
    'total_wins': 0,
    'sessions': 0,
    'start_time': datetime.now().isoformat()
}

@app.route('/')
def index():
    stats['sessions'] += 1
    logger.info(f"Новая сессия. Всего сессий: {stats['sessions']}")
    return render_template('index.html')

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Получить общую статистику"""
    return jsonify({
        'version': __version__,
        'stats': stats
    })

@app.route('/api/attempt', methods=['POST'])
def log_attempt():
    """Логировать попытку поймать кнопку"""
    stats['total_attempts'] += 1
    logger.info(f"Попытка поймать кнопку. Всего попыток: {stats['total_attempts']}")
    return jsonify({
        'success': True, 
        'total_attempts': stats['total_attempts']
    })

@app.route('/api/win', methods=['POST'])
def log_win():
    """Логировать успешное согласие"""
    stats['total_wins'] += 1
    data = request.get_json() or {}
    attempts = data.get('attempts', 0)
    logger.info(f"Пользователь согласился после {attempts} попыток. Всего побед: {stats['total_wins']}")
    return jsonify({
        'success': True, 
        'total_wins': stats['total_wins']
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': __version__,
        'timestamp': datetime.now().isoformat(),
        'uptime': stats['start_time']
    })

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False') == 'True'
    logger.info(f"Запуск приложения версии {__version__}")
    logger.info(f"Debug режим: {debug_mode}")
    app.run(debug=debug_mode, host='0.0.0.0', port=5001)

