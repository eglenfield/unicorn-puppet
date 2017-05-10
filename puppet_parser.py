import json
import os
import re

packages_array = []
user_array = []
volumes_array = []
test_user_array = []
test_volume_array = []
test_package_array = []
os_regex = ''
os_type = ''

def initialize(fn):
	data = open(os.path.join('inventory_files', fn), 'r')
	data = json.load(data)

	os_regex = re.compile('-(.+).json')
	os_type = os_regex.search(fn).group(1)
	return data, os_type

def package_parser(packages):
	for fn in os.listdir('inventory_files'):
		data, os_type = initialize(fn)
		package_count = 0
		for resource_data in data['resources']:
			if resource_data['resource'] == 'package':
				package_count += 1
				resource_data['package_key'] = package_count
				resource_data['os'] = os_type
				packages_array.append(resource_data)

		for instance in packages_array:
			package1 = packages()
			package1.os = instance['os']
			package1.provider = instance['provider']
			package1.resource = instance['resource']
			package1.title = instance['title']
			package1.version = instance['versions']
			package1.save()


def user_parser(users):
	for fn in os.listdir('inventory_files'):
		data, os_type = initialize(fn)
		user_count = 0
		for user_data in data['resources']:
			if user_data['resource'] == 'user':
				user_count += 1
				user_data['user_key'] = user_count
				user_data['os'] = os_type
				user_array.append(user_data)

		for instance in user_array:
			user1 = users()
			user1.resource = instance['resource']
			user1.shell = instance['shell']
			user1.title = instance['title']
			user1.uid = instance['uid']
			user1.comment = instance['comment']
			user1.home = instance['home']
			user1.gid = instance['gid']
			user1.groups = instance['groups']
			user1.os = instance['os']
			user1.save()


def volume_parser(volumes):
	for fn in os.listdir('inventory_files'):
		data, os_type = initialize(fn)
		for d in data['facts']['mountpoints']:
			volume_name = d
			data['facts']['mountpoints'][d]['volume_name'] = volume_name
			data['facts']['mountpoints'][d]['os'] = os_type
			volumes_array.append(data['facts']['mountpoints'][d])

		for instance in volumes_array:
			volume1 = volumes()
			volume1.volume_name = instance['volume_name']
			volume1.available = instance['available']
			volume1.available_bytes = instance['available_bytes']
			volume1.used = instance['used']
			volume1.capacity = instance['capacity']
			volume1.size = instance['size']
			volume1.options = instance['options']
			volume1.size_bytes = instance['size_bytes']
			volume1.used_bytes = instance['used_bytes']
			volume1.device = instance['device']
			volume1.filesystem = instance['filesystem']
			volume1.os = instance['os']
			volume1.save()

def test_package_parser(packages, data):
	for resource_data in data['resources']:
		if resource_data['resource'] == 'package':
			resource_data['os'] = os_type
			test_package_array.append(resource_data)

	for instance in test_package_array:
		package1 = packages()
		package1.os = instance['os']
		package1.provider = instance['provider']
		package1.resource = instance['resource']
		package1.title = instance['title']
		package1.version = instance['versions']
		package1.save()

def test_users_parser(users, data):
	for user_data in data['resources']:
		if user_data['resource'] == 'user':
			user_data['os'] = os_type
			test_user_array.append(user_data)

	for instance in test_user_array:
		user1 = users()
		user1.resource = instance['resource']
		user1.shell = instance['shell']
		user1.title = instance['title']
		user1.uid = instance['uid']
		user1.comment = instance['comment']
		user1.home = instance['home']
		user1.gid = instance['gid']
		user1.groups = instance['groups']
		user1.os = instance['os']
		user1.save()

def test_volumes_parser(volumes, data):
	for d in data['facts']['mountpoints']:
		volume_name = d
		data['facts']['mountpoints'][d]['volume_name'] = volume_name
		data['facts']['mountpoints'][d]['os'] = os_type
		test_volume_array.append(data['facts']['mountpoints'][d])

	for instance in test_volume_array:
		volume1 = volumes()
		volume1.volume_name = instance['volume_name']
		volume1.available = instance['available']
		volume1.available_bytes = instance['available_bytes']
		volume1.used = instance['used']
		volume1.capacity = instance['capacity']
		volume1.size = instance['size']
		volume1.options = instance['options']
		volume1.size_bytes = instance['size_bytes']
		volume1.used_bytes = instance['used_bytes']
		volume1.device = instance['device']
		volume1.filesystem = instance['filesystem']
		volume1.os = instance['os']
		volume1.save()
