from flask import Flask, request, redirect, url_for, render_template
from db_handler import db, ldb, render
from processor import debug
from os import environ as env
from webhook import logging

app = Flask('app')
f = "subjects/"


@app.route('/', methods=["GET", "POST"])
def the():
  try:
    a = request.args.get("f")
    return render_template("base.html")
  except Exception:
    return render_template('base.html')
  finally:
    return render_template("base.html")


@app.route('/<grade>/query')
def q(grade):
    if request.args.get("q") in ldb._unappend(
            f=f"subjects/{grade}.json")[request.args.get("sub")]:
        return render_template("notes.html",
                               qo=db.key_focus(k=request.args.get("q"),
                                               f=grade),
                               sub=request.args.get("sub"),
                               grade=grade,
                               topic=request.args.get("q"))


@app.route('/publish', methods=["GET", "POST"])
def send():
    if request.method == "GET":
        return render_template("creation.html")
    elif request.method == "POST":
        ldb._append(k=request.form["subject"],
                    v={request.form["topic"]: request.form["topic"]},
                    f=f"subjects/{request.form['grade']}.json")
        db.store(k=request.form["topic"],
                 v=request.form["notes"],
                 f=request.form["grade"])
        return redirect(
            f'/{request.form["grade"]}/query?sub={request.form["subject"]}&q={request.form["topic"]}'
        )


@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template('search.html')
    elif request.method == "POST":
      return redirect(f'/{request.form["grade"]}/query?sub={request.form["subject"]}&q={request.form["topic"]}')


@app.route('/r/<temp>')
def render_(temp):
    return render_template(f'{temp}.html')

app.run(host='0.0.0.0', port=8080, debug=debug())