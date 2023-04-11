'''
For self hosting flask app using gunicorn
refer here for details:
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04
'''
from app import app

if __name__ == "__main__":
    app.run()
