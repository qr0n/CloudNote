from flask import Flask, request, redirect, url_for, render_template
from db_handler import db, ldb
app = Flask('app')
f = "subjects/test.json"
@app.route('/', methods=["GET", "POST"])
def the():
  return render_template("base.html") 
  # """
  # <a href="/post">set</a>
  # <a href="/delete">delete</a>
  # <br></br>
  # <a href="/delete_db">delete databank</a>
  # <a href="/create_db">create databank</a>
  # <br></br>
  # <a href="/show">show db</a>
  # <a href="/kf?key=test">key focus</a>
  # <br></br>
  # <iframe src="/show">
  # """

@app.route('/db')
def hello_world():
  return """  
  <a href="/post">set</a>
  <a href="/delete">delete</a>
  <br></br>
  <a href="/delete_db">delete databank</a>
  <a href="/create_db">create databank</a>
  <br></br>
  <a href="/show">show db</a>
  <a href="/kf?key=test">key focus</a>
  <br></br>
  <iframe src="/show">
  """

@app.route('/post')
def publish():
  db.store(k=request.args.get("k"), v=request.args.get("v"))
  return redirect(url_for("hello_world"))

@app.route('/delete')
def delete():
  db.delete(k=request.args.get("k"))
  return redirect(url_for("hello_world"))

@app.route('/show')
def show():
  return str(db.render())

@app.route('/kf')
def key_focus():
  return str(db.key_focus(k=request.args.get("key")))

@app.route("/ct")
def a():
  ldb._append(k="subjects", v=[{"foo" : "bar"}, {"bar" : "foo"}], f=f)

@app.route('/query')
def q():
  if request.args.get("q") in ldb._unappend(f=f)["subjects"][request.args.get("sub")]:
    return db.key_focus(k=request.args.get("q"))

app.run(host='0.0.0.0', port=8080, debug=None)
