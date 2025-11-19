from flask import Flask,render_template,request,redirect,url_for,flash
app= Flask(__name__)
tasks = [{"id":1,"title":"acheter de pain","done":True},
             {"id":2,"title":"réviser flask","done":False},
             {"id":3,"title":"faire de sport","done":True},
             {"id":4,"title":"préparer le diner","done":True}]
app.secret_key = "1234"
    
@app.route("/")
def home():
    
    return render_template("index.html",tasks=tasks)

@app.route("/add",methods=["POST"])
def add():
    title=request.form.get("tache")
    
    if title:
      d={"id":len(tasks)+1,"title":request.form.get("tache"),"done":False}
      tasks.append(d)
      return redirect(url_for("home"))
    else:
        flash("le champ est vide")
        return redirect(url_for("home"))
  
@app.route("/done/<int:task_id>")
def done(task_id):
        for t in tasks:
           if t["id"] == task_id:
             t["done"]=True
             return redirect(url_for("home"))
         
@app.route("/delete/<int:task_id>")
def delete(task_id):
    for t in tasks:
        if t["id"]==task_id:
            tasks.remove(t)
            return redirect(url_for("home"))         
    

if __name__=="__main__":
    app.run(debug=True)