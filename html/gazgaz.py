from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7190394616:AAEuGjXLYWuDfe4IVYyf1KMmZPmtsY7toOg'
TELEGRAM_CHAT_ID = '7190394616'

@app.route('/visitor_info', methods=['POST'])
def visitor_info():
    # Получаем данные о посетителе из запроса
    visitor_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    # Формируем сообщение для отправки в Telegram
    message = f'New visitor info:\nIP: {visitor_ip}\nUser-Agent: {user_agent}'

    # Отправляем сообщение в Telegram
    send_telegram_message(message)

    return jsonify({'status': 'success'})

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f'Error sending Telegram message: {response.text}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
