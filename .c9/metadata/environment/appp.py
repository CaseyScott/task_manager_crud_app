{"changed":true,"filter":false,"title":"appp.py","tooltip":"/appp.py","value":"import os\nfrom flask import Flask, render_template, redirect, request, url_for\nfrom flask_pymongo import PyMongo\nfrom bson.objectid import ObjectId\n\napp = Flask(__name__)\n\napp.config['MONGO_DBNAME'] = 'task_manager'\napp.config['MONGO_URI'] = 'mongodb://casey:rOOtuser@cluster0-shard-00-00-uoefk.mongodb.net:27017,cluster0-shard-00-01-uoefk.mongodb.net:27017,cluster0-shard-00-02-uoefk.mongodb.net:27017/task_manager?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'\n\nmongo = PyMongo(app)\n\n@app.route('/')\n@app.route('/get_tasks')\ndef get_tasks():\n    return render_template('tasks.html', tasks=mongo.db.tasks.find())\n    \nif __name__ == '__main__':\n    app.run(host=os.environ.get('IP'),\n    port=int(os.environ.get('PORT')),\n    debug=True)","undoManager":{"mark":-2,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":20,"column":15},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","","app.config['MONGO_DBNAME'] = 'task_manager'","app.config['MONGO_URI'] = 'mongodb://casey:rOOtuser@cluster0-shard-00-00-uoefk.mongodb.net:27017,cluster0-shard-00-01-uoefk.mongodb.net:27017,cluster0-shard-00-02-uoefk.mongodb.net:27017/task_manager?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'","","mongo = PyMongo(app)","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template('tasks.html', tasks=mongo.db.tasks.find())","    ","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","    port=int(os.environ.get('PORT')),","    debug=True)"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":15},"end":{"row":20,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1560847843207}