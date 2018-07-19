from flask import Flask, render_template

app = Flask(__name__)

Gs=[
    {
        'GPU_TASK_NO':'1',
        'RUNNING_STATE':'FALSE',
        'STOP_STATE':'FALSE',
        'PAUSE_STATE':'FALSE',
    },

    {
        'GPU_TASK_NO':'2',
        'RUNNING_STATE':'TRUE',
        'STOP_STATE':'FALSE',
        'PAUSE_STATE':'FALSE',
    }


]

@app.route("/")
def home():

    return render_template('roster.html',Gs=Gs)

@app.route("/about")
def about():
    return '<h1>About</h1>'

if __name__== '__main__':
    app.run(debug=True)
