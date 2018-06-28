# aptoide_challenge_result
This is the result of the Aptoide job challenge

This project only requires Flask as a third party lib, are others are Python internals. To install Flask just do
"pip install Flask" and you should be good.

To start the server just run "python main.py" and your server should be up and running, ready to receive data.

To question the server just curl to it, for example: curl -d "Face" -X POST http://localhost:8080/autocomplete

---------------------------------------------Project Content---------------------------------------------------

The file main.py contains the simple API to call the autocomplete service. It only contains a POST endpoint that returns
the findings for the prefix that we send in.
This is a simple Flask server running locally on port 8080.

The file search.py is where we have the search logic and also where we have our Trie to store our titles.
This is currently using the 6500 title test file that you provided.

The file test_search.py represents six unit tests that cover what I think is most of the search and storing logic.