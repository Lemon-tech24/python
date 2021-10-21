from flask import Flask, redirect, url_for, request, render_template, session
import json

app = Flask(__name__)
filename = 'data.json'





if __name__ == '__main__':
    app.run(debug=True)
