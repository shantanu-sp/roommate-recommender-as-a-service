import requests
from threading import *

times = []
threads = []
input_data = [
    {
        "name": "Script Test-30",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    }, {
        "name": "Script Test-31",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    }, {
        "name": "Script Test-32",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    }, {
        "name": "Script Test-33",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    },
    {
        "name": "Script Test-34",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    },
    {
        "name": "Script Test-35",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    },
    {
        "name": "Script Test-36",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    },
    {
        "name": "Script Test-37",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    },
    {
        "name": "Script Test-38",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    },
    {
        "name": "Script Test-39",
        "age": "24",
        "major": "Masters",
        "program": "CS",
        "gender": "Male",
        "preferenceone": "University Pointe",
        "preferencetwo": "University Park",
        "foodpreference": "No Preference",
        "email": "aandey@asu.edu",
        "minrent": "250",
        "maxrent": "550",
        "description": "meh"
    }
]
ids = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


# Test whole system
def sendReq(sampleDict):
    global times
    url = 'https://recommender-dot-roommaterecommender.uc.r.appspot.com/student/getPreferences/4'
    print('Firing test student preference having name : '+str(sampleDict['name']))
    headers = {'content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, json=sampleDict, headers=headers)
    times.append(response.elapsed.total_seconds())
    print(sampleDict['name'], response.status_code, response.elapsed.total_seconds())
    pass


# Test Python Service
def testPythonService(id):
    global times
    getUrl = 'https://recommender-dot-roommaterecommender.uc.r.appspot.com/student/getPreferences/4'
    getUrl = getUrl + str(id)
    headers = {'Accept': 'application/json'}
    response = requests.get(getUrl, headers=headers)
    times.append(response.elapsed.total_seconds())
    print(id, response.status_code, response.elapsed.total_seconds())

'''
# for sampleDict in input_data:
for id in ids:
    t1 = Thread(target=testPythonService, args=(id,))
    t1.start()
    threads.append(t1)

'''
for sampleDict in input_data:
    t1 = Thread(target=sendReq, args=(sampleDict,))
    t1.start()
    threads.append(t1)

for thread in threads:
    thread.join()

print('The average time taken in seconds for ' + str(len(times)) + ' requests is : ' + str((float(sum(times) / len(times)))))