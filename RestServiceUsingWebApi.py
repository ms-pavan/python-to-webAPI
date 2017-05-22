import json
import requests


def _url(path):
    return 'http://localhost:51950/api' + path
def CurrentData():
    print('GET Request-Showing current data')
    print('--------------------------------')
    print('CarName------CarModel--------CarPrice-------CarColor')
    print('--------------------------------')
    response = requests.get(_url('/myapi/GetAllcarDetails'))
    for repo in response.json():
        print ('[{}]   {}  {}  {}'.format(repo['CarName'], repo['CarModel'],repo['CarPrice'], repo['CarColor']))
    print('--------------------------------')
    
CurrentData()

print('Post Request--Inserting record')
headers = {'content-type': 'application/json'}
url = _url('/myapi/PostCar')
data = {"Id":"1","CarName":"BMW","CarModel":"Benz","CarPrice":"80 Lakh","CarColor":"Silver"}
requests.post(url, data=json.dumps(data), headers=headers)
print('Record Added')

CurrentData()

print('Update Data--Updating Price of the above record')
task_id=1
url = _url('/myapi/Putcar/{:d}/'.format(task_id))
requests.put(url, json={"Id":"1","CarName":"BMW","CarModel":"M","CarPrice":"90 Lakh","CarColor":"Silver"})

CurrentData()

print('Delete Record-Deleting the above record')
task_id=1
requests.delete(_url('/myapi/Deletecar/{:d}/'.format(task_id)))

CurrentData()



    


    



