from flask import Flask, render_template
flask1 = Flask(__name__,template_folder='template')



@flask1.route('/about')
def guptas():
    return render_template('index.html')


flask1.run(debug=True,use_reloader=False)
