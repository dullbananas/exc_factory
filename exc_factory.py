def make_exception(name, attrs=None):
	if attrs == None:
		attrs = tuple()
	
	# Define members of the new class
	def init(self, message, **kwargs):
		# Call base constructor
		super(self.__class__, self).__init__(message)
		# Set custom attributes
		for attr_name in attrs:
			attr = kwargs.pop(attr_name, None)
			setattr(self, attr_name, attr)
	
	# Generate the class
	result = type(name, (Exception,), {
		'__init__': init,
	})
	
	return result
