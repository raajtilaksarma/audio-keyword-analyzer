import speech_recognition as sr

class KeywordCounter():

    def getTranscription(self,audioFileName):
        r = sr.Recognizer()
        audio_file = sr.AudioFile(audioFileName)
        with audio_file as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        return text

    def readKeyWords(self,keywordFileName):
        '''
            Returns a list of keywords read from a text file.
            Each line of the text file should contain one keyword
        '''
        list_kw = []
        with open(keywordFileName,'r') as f:
            for line in f:
                for word in line.split():
                    list_kw.append(word.lower())     
        return list_kw

    def identifyKeyWordCounts(self,keywords, text):
        '''
            Identifies keyword counts given keyword and text
        '''
        count_dict = {kw:0 for kw in keywords}
        for word in text.lower().split():
            if word in keywords:
                count_dict[word]+=1
        result = [word+':'+str(count_dict[word])+' times' for word in count_dict]
        return result

    def __init__(self,audioFileName,keywordFileName):
        self.audioFileName = audioFileName
        self.keywordFileName = keywordFileName
        self.text = self.getTranscription(self.audioFileName)
        self.keywords = self.readKeyWords(self.keywordFileName)
        self.result = self.identifyKeyWordCounts(self.keywords,self.text)

    def getResult(self):
        return self.result
