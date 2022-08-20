from flask import Flask, render_template, url_for, request
from ShortestPath import Graph


import requests, json



org_avail={
    'Eyes':['I','C','G','F'],
    'Kidney':['B','F','H','C','G'],
    'Liver':['C','F',],
    'Heart':['D','H'],
    'Pancreas':['E','I','F']
}
place_hash={
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
}
value_place_hash={
    0:'A',
    1:'B',
    2:'C',
    3:'D',
    4:'E',
    5:'F',
    6:'G',
    7:'H',
    8:'I', 
}

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/routing',methods=['POST', 'GET'])
def routing():
    output = request.form.to_dict()
    start = output["locs"]
    organ = output['orgs']
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]]
    g=Graph(9,graph)
    g.dijkstra(place_hash[start])
    path_details=g.outputs


    '''
    api_key ='AIzaSyBgAdZ-1TQ_5FEIgh-B4VOpEpGyXl_nZKY'
    source = start
    dest = 'Hyderabad'
    url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
    r = requests.get(url + 'origins = ' + source +
                    '&destinations = ' + dest +
                    '&key = ' + api_key)

    x = r.json()
    return render_template('index.html', path=x, dist=x)
    print(x)


    '''
    avail=org_avail[organ]
    min_dist=1e9
    '''
    min_path=[]
    for hsptl in avail:
        if(start==hsptl):
            min_dist=0
            min_path=[start]
        else:
            dist,path=path_details[place_hash[hsptl]]
            if(dist<min_dist):
                min_dist=dist
                min_path=path
    if(min_dist==0):
        return render_template('index,html',path='NA', dist='NA')
    else:
        path=[]
        for locn in min_path:
            path.append(value_place_hash[locn])
        path=' --> '.join(path)
        return render_template('index.html', path=path, dist=min_dist)
    '''
    minn=10e9
    mn=-1
    for i in range(len(path_details)):
        if(path_details[i]!=0 and path_details[i]<minn):
            minn=path_details[i]
            mn=i
    return render_template('index.html', path=value_place_hash[mn], dist=minn)

if __name__ == "__main__":
    app.run(debug=True,port=5001)