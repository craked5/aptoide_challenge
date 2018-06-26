from flask import Flask, request
from search import AutocompleteSearch
import csv
import json

app = Flask(__name__)
trie = AutocompleteSearch()

with open('test_files/6500titles.csv', 'r') as csv_file:
    title_list = [i[0] for i in csv.reader(csv_file)]
for title in title_list:
    trie.insert(title)


@app.route('/autocomplete', methods=["Post"])
def get_values():
    search_result = trie.autocomplete_start(request.get_data())
    if search_result is None or search_result is []:
        return json.dumps("No matching titles.")
    return json.dumps(search_result)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080, threaded=True)
