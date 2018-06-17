from flask import Flask, request
import json
import re
import csv

with open('test_files/190titles.csv', 'rb') as csv_file:
    titles_list = [i[0] for i in csv.reader(csv_file, delimiter=' ', quotechar='|')]
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/values', methods=["Post"])
def get_values():
    beginning = request.get_data()