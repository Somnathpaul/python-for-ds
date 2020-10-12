################### syntax ###################
'''
di = {i:i*2 for i in range(1,50) if i%2==0}
print(di)

'''

'''
lst = ['python', 'c++', 'php', 'java']
di = {i:i for i in lst}
print(di)
'''

'''
########## altering dictionary key value pair
dic = {1:"amazon", 2:"flipkart", 3:"baidu", 4:"google", 5:"tancent"}
di = {v:k for (k,v) in dic.items()}
print(di)
'''


################## example ##################
# converting two list into a dictionary 
print("Top 12 websites with highest visited : ")
company=['google.com', 'youtube.com', 'tmall.com', 'baidu.com', 'qq.com', 'facebook.com', 'sohu.com', 'taobao.com', '360.cn', 'jd.com', 'yahoo.com','amazon.com']
company_number = [i+1 for i in range(0,len(company))]
#print(company_number)
di_coma = dict(zip(company_number, company))
print(di_coma)