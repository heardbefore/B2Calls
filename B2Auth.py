import base64
import json
import urllib2
import os

def clear():
    os.system( 'clear' )

def lineBreak():
	print('\n')

id_and_key = '373f089f3db0:001090da7d0953c6b81890288fdd4f8ff36642b5d6'
basic_auth_string = 'Basic ' + base64.b64encode(id_and_key)
headers = { 'Authorization': basic_auth_string }

request = urllib2.Request(
    'https://api.backblazeb2.com/b2api/v1/b2_authorize_account',
    headers = headers
    )
response = urllib2.urlopen(request)
response_data = json.loads(response.read())
response.close()

print 'auth token:', response_data['authorizationToken']
print 'api url:', response_data['apiUrl']
print 'download url:', response_data['downloadUrl']
print 'minimum part size:', response_data['minimumPartSize']

api_url = response_data['apiUrl'] # Provided by b2_authorize_account
account_id = "373f089f3db0" # Obtained from your B2 account page
account_authorization_token = response_data['authorizationToken'] # Provided by b2_authorize_account
request2 = urllib2.Request(
	'%s/b2api/v1/b2_list_buckets' % api_url,
	json.dumps({ 'accountId' : account_id }),
	headers = { 'Authorization': account_authorization_token }
	)
response2 = urllib2.urlopen(request2)
response_data2 = json.loads(response2.read()) # Saves JSON data into python dictonary called response_data2
response2.close()

i = 0
# shows list of buckets in the account
for bucket in response_data2['buckets']:
	print str(i +1) + ' ' + bucket['bucketName']
	i += 1

buckNum = raw_input('Please Choose a Bucket: ')
x = 0
buckNum = int(buckNum) - 1
for bucket in response_data2['buckets']:
	if buckNum == x:
		bucket_id = response_data2['buckets'][x]['bucketId']
		break
	else:
		x += 1

clear() #clear the screen
print('You chose the bucket named: ' + response_data2['buckets'][x]['bucketName'])
#list files in chosen bucket
request = urllib2.Request(
	'%s/b2api/v1/b2_list_file_names' % api_url,
	json.dumps({ 'bucketId' : bucket_id }),
	headers = { 'Authorization': account_authorization_token }
	)
response = urllib2.urlopen(request)
response_data = json.loads(response.read())
response.close()

#Show the file list
i=0
for file in response_data['files']:
	print str(i +1) + ' ' + file['fileName']
	i += 1

lineBreak()

fileChoice = raw_input('Select which file to download: ') #get file selection
fileChoice = int(fileChoice) - 1 #convert choice to integer
lineBreak()




