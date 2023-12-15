from app import create_app
import os

app = create_app('config.py')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=int(os.getenv('PORT', 443)), debug=True, ssl_context=('cert.pem', 'key.pem'))
    pass
