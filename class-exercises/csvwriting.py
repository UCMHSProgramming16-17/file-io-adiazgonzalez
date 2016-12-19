import csv
csvfile = open('examplefile.csv', 'w')

csvwriter = csv.writer(csvfile, delimiter=',')

csvwriter.writerow([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
csvwriter.writerow(['andrea', 'devan', 'shanli', 'thomas', 'sydney', 'nelson', 'tyler'])
csvwriter.writerow(['original', 'x2', 'x3', 'x4', 'x5'])
for x in range(500):
  csvwriter.writerow([x, x*2, x*3, x*4, x*5])

csvfile.close()

