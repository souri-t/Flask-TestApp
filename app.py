from flask import Flask, request
app = Flask(__name__)                             

@app.route('/')                                   
def hello_world(): 
    # textで指定されたパラメータをJsonに整形して返す
    text = request.args.get('text', '')                  
    return { 'text' : text }           

@app.route('/users', methods=['GET'])
def get_user():
    # DBからフィルタリングして取得
    return { 'text' : 'aaa' }

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user2(user_id=None):
    # DBからフィルタリングして取得
    return { 'text' : user_id }

# 外部に公開できるようにポート開放
if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=5000, debug=False)
