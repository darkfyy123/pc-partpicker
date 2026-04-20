from flask import Flask, render_template, blueprints






template = blueprints.Blueprint("web", __name__, static_folder="static", template_folder="templates")





@template.route("/")
def home():
    return render_template("home.html")



@template.route("/partpicker")
def index():
    return render_template("partpicker.html")

@template.route("/edit")
def builds_edit():
    return render_template("web_edit.html")


@template.route("/table_add")
def table_add():
    return render_template("table_add.html")



@template.route("/table_del")
def table_del():
    return render_template("table_del.html")



@template.route("/table_upd")
def table_upd():
    return render_template("table_upd.html")



@template.route("/table_show")
def table_show():
    return render_template("table_show.html")



@template.route("/builds")
def builds_load():
    return render_template("builds.html")



@template.route("/build_del")
def build_del():
    return render_template("build_del.html")
