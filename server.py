from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')                           
def principal():
    return render_template('index.html')  
    

#def four():
#  return "4"
#@app.route('/(x)/(y)'

@app.route('/<int:x>')                           
def personal(x):
    return render_template("unvalor.html", x=x)  

@app.route('/4')                           
def cuatro():
    return render_template('cuatro.html')  

@app.route('/<int:x>/<int:y>')                           
def tableropersonal(x,y):
    return render_template("tableropersonal.html", x=x, y=y)  

if __name__=="__main__":
    app.run(debug=True) 