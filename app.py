#! /usr/bin/env python
#coding=utf-8
import os, sys

from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form

from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required
import MySQLdb, json



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class MysqlLogin(Form):
    host = StringField('host', validators=[Required()])
    name = StringField('name', validators=[Required()])
    password = StringField('password', validators=[Required()])
    port = StringField('port', validators=[Required()])
    database = SelectField('database', choices=[(0, u'请选择数据库')])

    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MysqlLogin()
    form.host.data = "localhost"
    form.port.data = "3306"
    form.name.data = "root"

    return render_template('index.html', form=form)

@app.route('/get_db', methods = ['POST'])
def db_list():

    form = request.form
    conn = None
    cur = None
    try:
        conn = MySQLdb.connect(
            host = form.get('host', 'localhost').strip(),
            user = form.get('name', 'root').strip(),
            passwd = form.get('password', '').strip(),
            port = int(form.get('port', '3306')),
        )
        cur = conn.cursor()
        cur.execute('show databases')
        db_list = cur.fetchall()
        db_arr = []
        for db in db_list:
            db_name = db[0]
            db_arr.append(db_name)
        json_data = {'ret':0, 'msg':'ok', 'data':db_arr}

    except:
        json_data = {'ret':10000, 'msg':'发生错误了', 'reqdata':form}

    finally:
        if cur:
            cur.close()

        if conn:
            conn.close()

    return json.dumps(json_data)

@app.route('/get_tb', methods = ['POST'])
def get_tb():
    """获取数据库表"""

    form = request.form
    db_name = form.get('db_name', '').strip()

    conn = None
    cur = None
    try:
        conn = MySQLdb.connect(
            host=form.get('host', 'localhost'),
            user=form.get('user', 'root'),
            passwd=form.get('password', ''),
            db=form.get('db_name', 'test'),
            port=int(form.get('port', 3306)),
        )
        cur = conn.cursor()
        cur.execute('show tables')
        tb_list = cur.fetchall()
        tbarr = []
        for tb in tb_list:
            tbname = tb[0]
            tbarr.append(tbname)
        json_data = {'ret':0, 'msg':'ok', 'data':tbarr}

    except BaseException:
        json_data = {'ret':10000, 'msg':'发生错误了', 'reqdata':form}

    finally:
        if cur:
            cur.close()

        if conn:
            conn.close()

    return json.dumps(json_data)


@app.route('/get_sql_code')
def get_sql_code():
    """获取SQL代码"""

    form = request.form
    conn = None
    cur = None
    try:
        table = form['table']
        conn = MySQLdb.connect(
            host=form.get('host', 'localhost'),
            user=form.get('user', 'root'),
            passwd=form.get('password', ''),
            db=form.get('db_name'),
            port=int(form.get('port', 3306)),
        )
        cur = conn.cursor()
        cur.execute("desc `%s`" % table)
        print(cur)
        field_list = cur.fetchall()
        print field_list
    except:
        pass




if __name__ == '__main__':
    manager.run()