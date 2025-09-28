# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
# JSON 응답 시 ASCII가 아닌 문자를 이스케이프 처리하지 않도록 설정합니다.
app.config['JSON_AS_ASCII'] = False

@app.route('/decision')
def get_decision():
    data = {"decision": "네, 좋은 생각이에요! 👍"}
    return jsonify(data)

# ... (이하 코드)
# 모든 도메인에서의 요청을 허용합니다.
CORS(app)

@app.route('/api/random')
def random_number():
    """1부터 99 사이의 랜덤한 정수를 생성하고 JSON 형태로 반환합니다."""
    number = random.randint(1, 99)
    return jsonify({'number': number})

# 새로 추가된 API 엔드포인트
@app.route('/api/decision')
def decision_maker():
    """미리 정의된 응답 리스트에서 하나를 랜덤으로 선택하여 JSON 형태로 반환합니다."""
    answers = [
        "네, 좋은 생각이에요! 👍",
        "음, 다시 생각해 보세요. 🤔",
        "당장 시작하세요! 🔥",
        "별로 좋은 선택은 아닌 것 같아요. 👎",
        "물론이죠! 왜 망설이세요? 😄",
        "오늘은 좀 쉬는 게 어때요? 😴",
        "확신할 수 없어요. 동전을 던져보세요! 🪙"
    ]
    decision = random.choice(answers)
    return jsonify({'decision': decision})

if __name__ == '__main__':
    # Render.com과 같은 클라우드 환경에서는 Gunicorn을 사용하므로,
    # 이 부분은 로컬 테스트용으로 사용됩니다.
    app.run(host='0.0.0.0', port=5000)
