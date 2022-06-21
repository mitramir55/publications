
from flask import Flask, redirect, url_for, render_template, request, session
from graphviz import render
import numpy as np
import pandas as pd



app = Flask(__name__)

# config------------------------------------------------
VOCAB_FILE = 'Vocabulary.xlsx'
ALLOWED_EXTENSIONS = {'txt'}

app.config['SECRET_KEY'] = '12345'

#------------------------------------------------------
@app.route('/', methods=['POST', 'GET'])
def index(**kwargs):
    return render_template('index.html')




    