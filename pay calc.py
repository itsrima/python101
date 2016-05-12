print "How much do you make in a year?"
pay_yearly = raw_input()
print "So you make %s per month and %s per week" % (
	float(pay_yearly) / 12., float(pay_yearly) / 52.)