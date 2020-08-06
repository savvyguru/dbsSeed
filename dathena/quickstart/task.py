from celery import shared_task,app,task
from .models import File_Meta
import re

@task(name="updateScore1")
def updateScoreTask():
    print("Updating score task")
    queryset = File_Meta.objects.all()
    for file in queryset:
        f = open(file.file.path, "r")
        userfile = f.read()
        text = "".join(userfile)
        sensitiveWord = {"secret":10,"dathena":7,"internal":5,"external":3,"public":1}
        secret_score = 0
        for word,score in sensitiveWord.items():
            secret_score += len(re.findall("(?i)"+word,text)) * score
        file.score = secret_score
        #file.timestamp = models.DateTimeField(auto_now=True)
        file.save()

def test():
    queryset = File_Meta.objects.all()
    for file in queryset:
        f = open(file.file.path, "r")
        sensitiveWord = {"secret":10,"dathena":7,"internal":5,"external":3,"public":1}
        secret_score = 0
        for word,score in sensitiveWord.items():
            secret_score += len(re.findall("(?i)"+word,f.read())) * score
        file.score = 0#secret_score
        #file.timestamp = models.DateTimeField(auto_now=True)
        file.save()
