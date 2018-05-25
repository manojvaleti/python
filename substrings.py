import re

originalstring = raw_input()

#replace requiredstring with the required substring we wanted to find in the original string

x = len(re.findall('(?=requiredstring)',originalstring))

#the number of times the required substring is found in our originalstring

print x

