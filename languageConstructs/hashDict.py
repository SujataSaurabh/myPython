#	SuGo, 15 August 2018
#	Implement dictionaries

dict = {'India': ['Delhi', 'Bangalore'], 
	'US':{'Washington D.C', 'Washington'}, 
	'Germany':{'Niedersachsen', 'Baden-Wurttemberg'}	
}
print(dict['India'], "\n")
print("Keys \t", dict.keys(), "\n")
print("Values \t", dict.values(), "\n")
print("Items \t", dict.items(), "\n")
print("Using get() function [dict.get('US')]\n")
print(dict.get('US'))
