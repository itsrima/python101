from sys import argv

script, user_id = argv


filename = user_id + '.txt'

print "This is a salary questionnaire & calculation for user %s" %user_id
print "Hello, user %s." %user_id
print "What is your yearly income?"

yearly_income = raw_input(">> ")

print "Now,would you like a monthly or weekly earnings report?"

report_type = raw_input(">> ")

target = open(filename, 'w')
target.write('yearly income: ' + yearly_income)
target.write("\n")
target.write('The user chose: ' + report_type)

if report_type == "monthly":
	print float(yearly_income) / 12
	
elif report_type == "weekly":
	print float(yearly_income) / 52

else:
	print "Stop wasting my time!"


print "Great! We've recorded your yearly income and report preference."
target.close()