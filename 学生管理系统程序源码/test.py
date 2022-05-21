#data="17140216;80.845,90.55,100.00"
#sid=data.split(sep=';')
#ssco=sid[1].split(sep=',')
#print('The each subject score of No. {0} is {1},{2},{3}.'.format(sid[0],ssco[0],ssco[1],ssco[2]))
#lst=str.split(sep=';')
#scores=lst[1].split(sep=',')
#print(lst[0],lst[1])
#print(scores[0],scores[1],scores[2])
#print('{0},{1},{2}'.format(lst[0],scores[0],scores[1]))
format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'java成绩', '总成绩'))
