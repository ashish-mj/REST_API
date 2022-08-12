from flask import Flask, jsonify,request

app = Flask(__name__)
app.config['SECRET_KEY']='XXXXXXX'


players =[
          {"Jersey Number": 10,
           "Name" : "Sachin Tendulkar",
           "Age" : 47,
           "Role" : "Batsman",
           "Contract" : "A"
           },
          {"Jersey Number": 7,
           "Name" : "MS Dhoni",
           "Age" : 39,
           "Role" : "Wicket-Keeper",
           "Contract" : "A"
           },
           {"Jersey Number": 12,
           "Name" : "Yuvraj Singh ",
           "Age" : 37,
           "Role" : "Allrounder",
           "Contract" : "B"
           },
           {"Jersey Number": 28,
           "Name" : "Jasprit Bumrah",
           "Age" : 28,
           "Role" : "Bowler",
           "Contract" : "B"
           },
]

@app.route('/players',methods=["GET"])
def getPlayers():
    return jsonify({'Players':players})

@app.route('/players/<int:id>',methods=["GET"])
def getPlayersById(id):
    return jsonify({'Players':players[id]})

@app.route('/players',methods=["POST"])
def createPlayer():
    if request.method=='POST':   
        temp ={}
        temp["Jersey Number"]=request.form['Jersey Number']
        temp["Name"]=request.form['Name']
        temp["Age"]=request.form['Age']
        temp["Role"]=request.form['Role']
        temp["Contract"]=request.form['Contract']
        players.append(temp)
        return jsonify({'Created':temp}),201
    
@app.route('/players/<int:id>',methods=["PUT"])
def updateContractById(id):
        temp = players[id]
        temp['Contract']= request.form['Contract']
        players[id]=temp
        return jsonify({'Updated':temp})
    
@app.route('/players/<int:id>',methods=["DELETE"])
def deleteById(id):
        players[id] = {}
        return jsonify({'Deleted':True})

if __name__ == '__main__':
	app.run(debug=True)
