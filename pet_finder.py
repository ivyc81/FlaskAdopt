import requests
from secrets import API_KEY

def find_random_pet():
    '''function call pet finder restful api to get a random pet'''
    response = requests.get('http://api.petfinder.com/pet.getRandom',
    params ={'key':API_KEY,'output':'basic','format':'json'})  
    response_dic = response.json()
    pet_name = response_dic['petfinder']['pet']['name']['$t']
    pet_age = response_dic['petfinder']['pet']['age']['$t']
    try:
        pet_photo = response_dic['petfinder']['pet']['media']['photos']['photo'][3]['$t']
    except KeyError:
        pet_photo = ''
    return {'name':pet_name, 'age':pet_age, 'photo':pet_photo}