
import xml.etree.ElementTree as ET
from datetime import timedelta, date



def adjust_time(X: int, Y: int):
    '''
    The function is written in keep mind of the 
    given test xml file and structure. 

    if the xml changes in any case we need to change
    the code accordingly
    '''
    print('\n ****task started*****')
    print("\n loading the xml file....")
    tree = ET.parse('test_payload1.xml')
    
    print('\n getting the objects...')
    # getting the objects
    dep_obj = tree.findall(".//DEPART")
    return_obj = tree.findall(".//RETURN")

    print('\n calculating the dates from the current date')
    Depart = date.today() + timedelta(days=X)
    Return = date.today() + timedelta(days=Y)

    dep_obj[0].text = Depart.strftime('%Y%m%d')
    return_obj[0].text = Return.strftime('%Y%m%d')
    
    # writing to output 
    print("\n writing the output to output.xml")
    tree.write('output.xml')
    print("\n ****task completed*****")

adjust_time(4,14)