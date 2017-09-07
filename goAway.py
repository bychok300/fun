import vk_api
import sys
import json
import time
import getpass

print("Your login: ")
login = input()

password = getpass.getpass('Your password:')



def send_msg_if_it_exist(login, password):

	#init vk api
	vk_session = vk_api.VkApi(login,password)

	#try to authorize
	try :
		vk_session.auth()
	except vk_api.AuthError as error_msg:
		print(error_msg)
		sys.exit("Auth failed")

	#set opportunity to call vk api methods
	vk = vk_session.get_api()

	#set time to refresh
	print("Set time to refresh : ")
	refresh_time = input()

	print("Set answer message :")
	answer = input()

	#check messages
	while True:


		#time to refreshing
		time.sleep(int(refresh_time))
		#get unreaded message
		json_data = vk.messages.getDialogs(unread=1)

		no_msg = json_data['count']

		#if no message
		if no_msg == 0:
			print("No messages yet")
		#send answer to message
		else :
			message_from_user = json_data['items'][0]['message']['body']

			usr_id = json_data['items'][0]['message']['user_id']

			print(message_from_user, usr_id)

			send_msg = vk.messages.send(user_id=usr_id,message=answer)


send_msg_if_it_exist(login,password)
