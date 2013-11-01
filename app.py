import os
import newrelic.agent
from flask import Flask, render_template, send_from_directory

#configuring newrelic check
config_file = os.environ.get('NEW_RELIC_CONFIG_FILE')
environment = os.environ.get('NEW_RELIC_ENVIRONMENT')

newrelic.agent.initialize(config_file, environment)

# initialization
app = Flask(__name__)
app.config.update(
    Debug = True,
)

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.route("/")
def index():
    return render_template('website homepage.html')

#launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)

