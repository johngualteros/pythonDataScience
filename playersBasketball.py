#import statistics
#players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
#print("standard deviation: {}".format(statistics.stdev(players)))

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

mean = sum(players)/len(players)
stdvar = (sum((v-mean)**2 for v in players)/len(players))**0.5

low, high = mean-stdvar,mean+stdvar

count = len([v for v in players if low < v < high])

print(count)