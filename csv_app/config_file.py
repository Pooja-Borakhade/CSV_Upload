# from configparser import ConfigParser
# import configparser
# file = 'config.conf'

# config = configparser.ConfigParser()
# config.read(file)

# print(config.sections())        # To access data from that file 

# print(config['account'])
# print(config['account']['pin'])


# ###Updating  Config###
# config.add_section("bank")
# config.set('bank','name','happ')

# with open(file,'w') as configfile:
#     config.write(configfile)


import configparser
parser = configparser.ConfigParser()
parser.read('sampleconfig.ini')
for sect in parser.sections():
   print('Section:', sect)
   for k,v in parser.items(sect):
      print(' {} = {}'.format(k,v))
   print()


# import configparser
# parser = configparser.ConfigParser()
# parser.add_section('Manager')
# parser.set('Manager', 'Name', 'Ashok Kulkarni')
# parser.set('Manager', 'email', 'ashok@gmail.com')
# parser.set('Manager', 'password', 'secret')
# fp=open('test.ini','w')
# parser.write(fp)
# fp.close()