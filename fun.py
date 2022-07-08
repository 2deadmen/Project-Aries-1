import wikipedia

class Fun:

    def __init__(self):
        pass

    def wikipedia(self,results):
        
        query=results.replace('wikipedia',"")
        resulta=wikipedia.summary(query,sentences=2)
        return resulta