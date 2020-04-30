data = 'from: IEMJEE 2016 <biswajoy.chatterjee@uem.edu.in>, date: 23 Jan 2017, 11:55'
find1 = data.find(':')
print(find1)

find2 = data.find('<', find1)
print(find2)

# slicing
domain  = data[find1+2 : find2-1]
print(domain)