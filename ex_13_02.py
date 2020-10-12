import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#
url = input('Enter - ')
position=input('Enter position:')
repeat= input('Enter number of repeat:')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')


for times in range(int(repeat)):

	#Getting the information of the correspondent url

	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')

	#We are indicated that the first name is 1, but in Python the array begins in 0,
	#so we have to take 1 unit from the index
	url = tags[int(position) - 1].get('href')
# print(link)

#Getting the content of the tag in the specified position. It should correspond to
#the answer we're looking for
print(tags[int(position) - 1])
result_name = tags[int(position) - 1].contents[0]
print(result_name)

# # links=list()
# # count=0
#
#
# # Retrieve all of the anchor tags
# tags = soup('a')
#
# for i in range(int(repeat)):
#     links=[]
#     for tag in tags:
#         links.append(tag.get('href', None))
# # print(links[int(position)-1])
#     html = urllib.request.urlopen(links[int(position)-1], context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     print("Retrieving",links[int(position)-1])
# print(links)
# print(links)
#     count=count+1
# print(namelist)
# print(namelist[count-1])


# import urllib
# from BeautifulSoup import *

# 2. Request raw URL input, count and position
# url = input('Enter URL to scrap: ')
# count = input('Enter count: ')
# count = int(count)
# position = input('Enter position: ')
# position = int(position)
#
# tag_list = list()
# # Repeats this count number of times
# for i in range(count):
#     print ("Retrieving:", url)
#     # 3. Read HTML with urllib's urlopen() method
#     html = urllib.request.urlopen(url, context=ctx).read()
#
#     # 4. Parse HTML with BeautifulSoup's BeautifulSoup() method
#     soup = BeautifulSoup(html, 'html.parser')
#
#     # 5. Retrieve list of anchor a tags
#     tags = soup('a')
#
#     # 6. Loop through to append tags to a list tag_list
#     for tag in tags:
#         tag_list.append(tag)
#
#     # 7. Get new url based on (position - 1) due to nature of counts request
#     url = tag_list[position - 1].get('href', None)
#     print(tag_list)
#
#     # 8. Delete the whole list for a new iteration through (3) to (7)
#     del tag_list[:]
#
# print ("Retrieving", url)
#SAMPLE DATA
# sample_url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# sample_repetitions = 4
# sample_resultPosition = 3
#
# #ACTUAL PROBLEM DATA
# problem_url = "http://py4e-data.dr-chuck.net/known_by_Evan.html"
# problem_repetitions = 7
# problem_resultPosition = 18
#
#
# #Choosing the type of execution we're trying
# type_of_execution = 'sample' #problem
# if type_of_execution == 'sample':
# 	(link, repetitions, resultPosition) = (sample_url, sample_repetitions, sample_resultPosition)
#
# elif type_of_execution == 'problem':
# 	(link, repetitions, resultPosition) = (problem_url, problem_repetitions, problem_resultPosition)


#Amount of iterations needed
# for times in range(repetitions):
#
# 	#Getting the information of the correspondent url
#
# 	html = urllib.request.urlopen(link, context=ctx).read()
# 	soup = BeautifulSoup(html, 'html.parser')
# 	tags = soup('a')
#
# 	#We are indicated that the first name is 1, but in Python the array begins in 0,
# 	#so we have to take 1 unit from the index
# 	link = tags[resultPosition - 1].get('href')
# # print(link)
#
# #Getting the content of the tag in the specified position. It should correspond to
# #the answer we're looking for
# print(tags[resultPosition - 1])
# result_name = tags[resultPosition - 1].contents[0]
# print(result_name)
