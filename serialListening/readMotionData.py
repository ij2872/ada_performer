import pickle


# todo read data, analyze data, be the data
fileName = "motion.dat"
data = pickle.load(open(fileName, 'rb'))


print(data)

