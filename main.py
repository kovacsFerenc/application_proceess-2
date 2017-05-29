from flask import Flask, render_template, redirect, request
import queries


app = Flask (__name__)



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/mentors')
def Mentors_schools_page():
    #show_mentors_a_school = queries.show_mentors_and_school()
    return render_template("table.html", datas=queries.show_mentors_and_school())


@app.route('/all-school')
def All_school_page():
    return render_template("table.html", datas=queries.all_school())


@app.route('/mentors-by-country')
def Contacts_page():
    return render_template("table.html", datas=queries.mentors_by_country())


@app.route('/contacts')
def Contacts_pagee():
    return render_template("table.html", datas=queries.contacts_page())


@app.route('/applicants')
def Applicants_page():
    return render_template("table.html", datas=queries.applicants())


@app.route('/applicants-and-mentors')
def Applicants_mentors_page():
    return render_template("table.html", datas=queries.applicants_and_mentor())

if __name__ == '__main__':
    app.run(debug=True)