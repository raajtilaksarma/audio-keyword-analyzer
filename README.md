# audio-keyword-analyzer
A Flask web app to show keyword counts in an audio file

### Demo
![](https://github.com/raajtilaksarma/audio-keyword-analyzer/blob/master/audio_keyword_analyzer.gif)

## Input files to be uploaded
 - A `.wav` file consisting of an audio recording that has some `keywords`
 - A `.txt` file consisting of the list of words identified as `keywords`
 
## Output
 - All `keywords` in the audio file along with the `no of times` each of them appears.

## Check it out live!

https://audio-keyword-analyzer.herokuapp.com/

NOTE : There is an issue if the `.wav` file size is higher than approximately 1MB. With good quality audio, transcription is better but heroku has a timeout of 30 seconds for the response. So in that case you can run it locally.

## Host locally
 - clone the repo
 - `pip3 install -r requirements.txt`
 - `python3 app.py`
 -  Go to `http://localhost:5000/`


