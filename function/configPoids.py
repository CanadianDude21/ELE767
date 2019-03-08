import numpy as np
np.set_printoptions(threshold=1000000)

def sauvegardePoids(reseau,path):
	print("début de sauvegarde des poids")
	for i in range(reseau.config["nombreCoucheCachees"]+2):
		data = reseau.lay[i]
		# Write the array to disk
		with open(path+"/configPoidsLayer"+str(i)+".txt", 'w') as outfile:
		# I'm writing a header here just for the sake of readability
		# Any line starting with "#" will be ignored by numpy.loadtxt
			outfile.write('# Poids couche 1: {0}\n#Donnée 1\n'.format(data.shape))
			# Iterating through a ndimensional array produces slices along
			# the last axis. This is equivalent to data[i,:,:] in this case
			j = 2
			for data_slice in data:

			# The formatting string indicates that I'm writing out
			# the values in left-justified columns 7 characters in width
			# with 2 decimal places.  
				np.savetxt(outfile, data_slice, fmt='%-7.10f')

			# Writing out a break to indicate different slices...
				outfile.write('# Donnée {}\n'.format(j))
				j+=1
			#print("couche 1 done")
		outfile.close()

	# with open('config/configPoidsLayer2.txt', 'w') as outfile:
	# 	data = reseau.lay2
	# 	#print(reseau.lay2)
	# 	outfile.write('# Poids couche 2: {0}\n#Neurone entrée 1\n'.format(data.shape))
	# 	# Iterating through a ndimensional array produces slices along
	# 	# the last axis. This is equivalent to data[i,:,:] in this case
	# 	i = 2
	# 	for data_slice in data:

	# 	# The formatting string indicates that I'm writing out
	# 	# the values in left-justified columns 7 characters in width
	# 	# with 2 decimal places.  
	# 		np.savetxt(outfile, data_slice, fmt='%-7.10f')

	# 	# Writing out a break to indicate different slices...
	# 		outfile.write('# Neurone entrée {}\n'.format(i))
	# 		i+=1
	# 	#print("couche 2 done")
	# outfile.close()

	# with open('config/configPoidsLayer3.txt', 'w') as outfile:
	# 	data = reseau.lay3
	# 	#print(reseau.lay3)
	# 	outfile.write('# Poids couche 3: {0}\n#Neurone entrée 1\n'.format(data.shape))
	# 	# Iterating through a ndimensional array produces slices along
	# 	# the last axis. This is equivalent to data[i,:,:] in this case
	# 	i = 2
	# 	for data_slice in data:

	# 	# The formatting string indicates that I'm writing out
	# 	# the values in left-justified columns 7 characters in width
	# 	# with 2 decimal places.  
	# 		np.savetxt(outfile, data_slice, fmt='%-7.10f')

	# 	# Writing out a break to indicate different slices...
	# 		outfile.write('# Neurone entrée {}\n'.format(i))
	# 		i+=1
	# 	#print("couche 3 done")
	print("fin de sauvegarde des poids")

def chargerPoids(reseau,path):
	print("début de chargement des poids")
	# Read the array from disk
	for i in range(reseau.config["nombreCoucheCachees"]+2):
		new_data = np.loadtxt(path+"/configPoidsLayer"+str(i)+".txt")
		reseau.lay[i] = new_data.reshape(reseau.lay[i].shape)
	# new_data = np.loadtxt('config/configPoidsLayer1.txt')
	# reseau.lay1 = new_data.reshape(reseau.lay1.shape)
	# #print(reseau.lay1)
	# new_data = np.loadtxt('config/configPoidsLayer2.txt')
	# reseau.lay2 = new_data.reshape(reseau.lay2.shape)
	# #print(reseau.lay2)
	# new_data = np.loadtxt('config/configPoidsLayer3.txt')
	# reseau.lay3 = new_data.reshape(reseau.lay3.shape)
	# #print(reseau.lay3)
	print("fin de chargement des poids")