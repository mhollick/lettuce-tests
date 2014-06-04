from lettuce import *
from subprocess import call
import boto
from boto.s3.key import Key
import boto.s3.connection
import os
import filecmp
import ConfigParser



@step('my configuration file is (\S+)')
def s3_config(step, s3_config):
    #world.s3_key = str(s3_key)
    config_file = './s3_fetch.ini'
    Config = ConfigParser.ConfigParser()
    Config.read(config_file)

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

aws_key_id = ConfigSectionMap('AWS')['aws_key_id']
aws_sec_key = ConfigSectionMap('AWS')['aws_sec_key']
s3_endpoint = ConfigSectionMap('S3')['s3_endpoint']
s3_bucket = ConfigSectionMap('S3')['s3_bucket']
s3_bucket_path_base = ConfigSectionMap('S3')['s3_bucket_path_base']
download_dest_base = ConfigSectionMap('TARGET')['download_dest_base']

'''
print '--------------------------------------------------------------------------------'
print '                                Configuration  '
print ' aws_key_id = ' + aws_key_id
print ' aws_sec_key = ' + aws_sec_key
print ' s3_endpoint = ' + s3_endpoint
print ' s3_bucket = ' + s3_bucket
print ' s3_bucket_path_base = ' + s3_bucket_path_base
print ' servers = ' + servers
print ' log_types = ' + log_types
print ' download_dest_base = ' + download_dest_base
print '--------------------------------------------------------------------------------'
'''


@step('my s3 key is (\S+)')
def s3_key(step, s3_key):
    world.s3_key = str(s3_key)

@step('my s3 secret is (\S+)')
def s3_secret(step, s3_secret):
    world.s3_secret = str(s3_secret)

@step('my s3 host is (\S+)')
def s3_host(step, s3_host):
    world.s3_host = str(s3_host)

@step('my s3 bucket is (\S+)')
def s3_bucket(step, s3_bucket):
    world.s3_bucket = str(s3_bucket)

@step('my s3 path is (\S+)')
def s3_path(step, s3_path):
    world.s3_path = str(s3_path)

@step('my test file is called (\S+)')
def test_file(step, test_file):
    world.test_file = str(test_file)

@step('my test file contains (\S+)')
def file_contents(step, file_contents):
    world.file_contents = str(file_contents)

@step('I upload my test file')

@step('I can download it and it is the same')

def create_test_file(test_file, file_contents)
    f = open(test_file, 'w')
    f.write(file_contents)
    f.close()

def upload_test_file(test_file, s3_key, s3_secret, s3_host, s3_bucket, s3_path)
    conn = boto.connect_s3(aws_access_key_id = s3_key, aws_secret_access_key = s3_secret, host = s3_host)
    bucket = conn.get_bucket(s3_bucket)
    full_key_name = os.path.join(s3_path, test_file)
    key = bucket.new_key(full_key_name)
    key.set_contents_from_filename(test_file)
    conn.close()

def download_test_file(test_file, s3_key, s3_secret, s3_host, s3_bucket, s3_path)
    conn = boto.connect_s3(aws_access_key_id = s3_key, aws_secret_access_key = s3_secret, host = s3_host)
    bucket = conn.get_bucket(s3_bucket)
    full_key_name = os.path.join(s3_path, test_file)
    key = bucket.get_key(full_key_name)
    key.get_contents_to_filename(test_file + '.s3')
    conn.close()

def compare_files(test_file)
    return filecmp.cmp(test_file, test_file + '.s3')

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1        
