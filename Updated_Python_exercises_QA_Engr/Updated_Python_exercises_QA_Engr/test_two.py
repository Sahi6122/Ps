import json

'''
for multiple nested case, can use the below data
and try to delete d_two or d_three keys to verify 
method is handling nested traversing
{
  "spreadsheetName": "ABC.xls",
  "inParams": {
    "planselect_1": "test11",
    "retdt": "2019-04-10",
    "appdate": "2019-04-02",
    "statecode": "CA",
    "deptdt": "2019-04-09"
  },
  "d_one": {
    "d_two": {
      "d_three": "should be deleted",
      "normal": 123
    }
  }, 
  "outParams": [
    "dateeff",
    "dateterm",
    "coverageresult",
    "calcdescr",
    "errorchk",
    "planresult",
    "covgsummary",
    "prem"
  ],
  "sessionId": null
}
'''

# provide values that needs to be deleted from the data
values_to_remove = ["outParams",  "appdate"]

def nest_loop(dict_item, obj):
    '''
    this is a recursive loop which
    verifys the given object is dict
    
    it it is, it loops recursvely to find out
    the deleted parameter if it exists
    in nested 

    if it is on main area, it will del and break the flow
    or it will loop until it finds out the deleted parameter
    '''
    for k in list(dict_item.keys()):
        if k == obj:
            print("\n parameter found: ", obj)
            del dict_item[k]
            print("\n deleted parameter: ", obj)
            break
        if isinstance(dict_item[k], dict):
            nest_loop(dict_item[k], obj) 
    return dict_item


def modify_json(data, values_to_remove):
    for values in values_to_remove:
        obj = nest_loop(data, values)
    return data

# reads the json file
with open('test_payload.json', 'r') as d:
        print("\n started..... \n\n reading json file.....")
        data = json.load(d)
        v = modify_json(data, values_to_remove)

# writes into json file
print("\n writing into json_data.json....")
with open('json_data.json', 'w') as outfile:
    json.dump(v, outfile, indent=4)
    print("\n completed....!!!!! \n")
