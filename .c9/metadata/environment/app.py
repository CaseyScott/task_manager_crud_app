{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":55,"position":55,"stack":[[{"start":{"row":0,"column":0},"end":{"row":20,"column":15},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","","app.config['MONGO_DBNAME'] = 'task_manager'","app.config['MONGO_URI'] = 'mongodb://casey:rOOtuser@cluster0-shard-00-00-uoefk.mongodb.net:27017,cluster0-shard-00-01-uoefk.mongodb.net:27017,cluster0-shard-00-02-uoefk.mongodb.net:27017/task_manager?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'","","mongo = PyMongo(app)","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template('tasks.html', tasks=mongo.db.tasks.find())","    ","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","    port=int(os.environ.get('PORT')),","    debug=True)"],"id":1}],[{"start":{"row":8,"column":43},"end":{"row":8,"column":51},"action":"remove","lines":["rOOtuser"],"id":2},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["S"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["t"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["r"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["i"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["x"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["7"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["6"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["0"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["0"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["k"]}],[{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"remove","lines":["k"],"id":3},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"remove","lines":["0"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"remove","lines":["0"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["6"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"remove","lines":["7"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"remove","lines":["x"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"remove","lines":["i"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"remove","lines":["r"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"remove","lines":["t"]},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"remove","lines":["S"]}],[{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["r"],"id":4},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["O"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["O"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["T"]}],[{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"remove","lines":["T"],"id":5}],[{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["t"],"id":6},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["u"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["s"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["e"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":187},"end":{"row":8,"column":188},"action":"remove","lines":["t"],"id":7}],[{"start":{"row":8,"column":187},"end":{"row":8,"column":188},"action":"insert","lines":["T"],"id":8}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":281},"action":"remove","lines":["mongodb://casey:rOOtuser@cluster0-shard-00-00-uoefk.mongodb.net:27017,cluster0-shard-00-01-uoefk.mongodb.net:27017,cluster0-shard-00-02-uoefk.mongodb.net:27017/Task_manager?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"],"id":9}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":117},"action":"insert","lines":["mongodb+srv://casey:<password>@cluster0-uoefk.mongodb.net/test?retryWrites=true&w=majority"],"id":10}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":57},"action":"remove","lines":["password>"],"id":11},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"remove","lines":["<"]}],[{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["r"],"id":12},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["O"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["O"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["t"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["u"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["s"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["e"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":84},"end":{"row":8,"column":86},"action":"remove","lines":["es"],"id":13}],[{"start":{"row":8,"column":84},"end":{"row":8,"column":85},"action":"remove","lines":["t"],"id":14},{"start":{"row":8,"column":83},"end":{"row":8,"column":84},"action":"remove","lines":["t"]}],[{"start":{"row":8,"column":83},"end":{"row":8,"column":84},"action":"insert","lines":["T"],"id":15},{"start":{"row":8,"column":84},"end":{"row":8,"column":85},"action":"insert","lines":["a"]},{"start":{"row":8,"column":85},"end":{"row":8,"column":86},"action":"insert","lines":["s"]},{"start":{"row":8,"column":86},"end":{"row":8,"column":87},"action":"insert","lines":["k"]},{"start":{"row":8,"column":87},"end":{"row":8,"column":88},"action":"insert","lines":["_"]}],[{"start":{"row":8,"column":88},"end":{"row":8,"column":89},"action":"insert","lines":["m"],"id":16},{"start":{"row":8,"column":89},"end":{"row":8,"column":90},"action":"insert","lines":["a"]},{"start":{"row":8,"column":90},"end":{"row":8,"column":91},"action":"insert","lines":["n"]},{"start":{"row":8,"column":91},"end":{"row":8,"column":92},"action":"insert","lines":["a"]},{"start":{"row":8,"column":92},"end":{"row":8,"column":93},"action":"insert","lines":["g"]},{"start":{"row":8,"column":93},"end":{"row":8,"column":94},"action":"insert","lines":["e"]},{"start":{"row":8,"column":94},"end":{"row":8,"column":95},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":123},"action":"remove","lines":["mongodb+srv://casey:rOOtuser@cluster0-uoefk.mongodb.net/Task_manager?retryWrites=true&w=majority"],"id":17},{"start":{"row":8,"column":27},"end":{"row":8,"column":120},"action":"insert","lines":["mongodb+srv://casey:<password>@taskmanager-uoefk.mongodb.net/test?retryWrites=true&w=majority"]}],[{"start":{"row":8,"column":47},"end":{"row":8,"column":57},"action":"remove","lines":["<password>"],"id":18},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["r"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["O"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["O"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["U"],"id":19},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["s"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["e"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":86},"end":{"row":8,"column":90},"action":"remove","lines":["test"],"id":20}],[{"start":{"row":8,"column":86},"end":{"row":8,"column":87},"action":"insert","lines":["t"],"id":21},{"start":{"row":8,"column":87},"end":{"row":8,"column":88},"action":"insert","lines":["a"]},{"start":{"row":8,"column":88},"end":{"row":8,"column":89},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":86},"end":{"row":8,"column":89},"action":"remove","lines":["tas"],"id":22},{"start":{"row":8,"column":86},"end":{"row":8,"column":98},"action":"insert","lines":["task_manager"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"insert","lines":["    "],"id":23}],[{"start":{"row":20,"column":3},"end":{"row":20,"column":4},"action":"insert","lines":[" "],"id":24}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":25}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"remove","lines":[" "],"id":26}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "],"id":27}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"insert","lines":["    "],"id":28}],[{"start":{"row":20,"column":8},"end":{"row":20,"column":12},"action":"insert","lines":["    "],"id":29}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":12},"action":"insert","lines":["    "],"id":30}],[{"start":{"row":16,"column":3},"end":{"row":16,"column":4},"action":"remove","lines":[" "],"id":31},{"start":{"row":16,"column":3},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":3},"action":"insert","lines":["   "]},{"start":{"row":17,"column":3},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":18,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":[" "],"id":32}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["@"],"id":33},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":["a"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":["p"]},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":["p"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["."],"id":34},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["r"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["o"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["u"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["e"],"id":35}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"remove","lines":[" "],"id":36},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"remove","lines":[" "]}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":12},"action":"insert","lines":["()"],"id":37}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":13},"action":"insert","lines":["''"],"id":38}],[{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["/"],"id":39},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["a"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["d"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["d"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":[">"]}],[{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"remove","lines":[">"],"id":40}],[{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["_"],"id":41},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["t"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["a"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["s"]},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["k"]}],[{"start":{"row":17,"column":23},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":42},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["d"]},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["e"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":[" "],"id":43},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["a"]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["d"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["d"]},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["_"]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":8},"action":"remove","lines":["add_"],"id":44},{"start":{"row":18,"column":4},"end":{"row":18,"column":12},"action":"insert","lines":["add_task"]}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":14},"action":"insert","lines":["()"],"id":45}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":[":"],"id":46}],[{"start":{"row":18,"column":15},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":47},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["r"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["t"],"id":48},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["u"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["r"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":[" "],"id":49},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["r"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["e"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["n"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["m"]}],[{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"remove","lines":["m"],"id":50}],[{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["d"],"id":51},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["e"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":17},"action":"remove","lines":["render"],"id":52},{"start":{"row":19,"column":11},"end":{"row":19,"column":28},"action":"insert","lines":["render_template()"]}],[{"start":{"row":19,"column":27},"end":{"row":19,"column":29},"action":"insert","lines":["''"],"id":53}],[{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":["a"],"id":54},{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"insert","lines":["d"]},{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"insert","lines":["d"]},{"start":{"row":19,"column":31},"end":{"row":19,"column":32},"action":"insert","lines":["t"]},{"start":{"row":19,"column":32},"end":{"row":19,"column":33},"action":"insert","lines":["a"]}],[{"start":{"row":19,"column":33},"end":{"row":19,"column":34},"action":"insert","lines":["s"],"id":55},{"start":{"row":19,"column":34},"end":{"row":19,"column":35},"action":"insert","lines":["k"]},{"start":{"row":19,"column":35},"end":{"row":19,"column":36},"action":"insert","lines":["."]}],[{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"insert","lines":["h"],"id":56},{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"insert","lines":["t"]},{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"insert","lines":["m"]},{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"insert","lines":["l"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":24,"column":23},"end":{"row":24,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":0},"timestamp":1560932330825,"hash":"1f2f916bf23619c67c49ce45a716563b9934a2ed"}