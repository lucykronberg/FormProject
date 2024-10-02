from flask import Flask, url_for, render_template,request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')
    
@app.route("/response")
def render_response():
    worldTally = 0
    mathTally = 0
    artTally = 0
    gardeningTally = 0
    scienceTally = 0
    csTally = 0
    for value in request.args:
        if request.args[value]=="World History": 
            worldTally +=1
        if request.args[value]=="Math":
            mathTally +=1
        if request.args[value]=="Science":
            scienceTally  +=1
        if request.args[value]=="Art":
            artTally +=1
        if request.args[value]=="Gardening":
            gardeningTally +=1
        if request.args[value]=="CS":
            csTally +=1
            
    x = max(worldTally,mathTally,scienceTally,artTally,gardeningTally,csTally)
    
    answer = ""
    if x == worldTally:
        answer = "Tormey"
    if x == mathTally:
        answer = "Mr. Reussner"
    if x == artTally:
        answer = "Ms. Barr"
    if x == scienceTally:
        answer = "Mr. Lotze"
    if x == csTally:
        answer = "Ms. Adams"
    if x == gardeningTally:
        answer = "Jose"
        
    print(answer)

    return render_template('response.html', teacherName = answer)
    
    
if __name__=="__main__":
    app.run(debug=False)