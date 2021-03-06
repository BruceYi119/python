import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글처리
fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = sb.load_dataset('tips')
data = sb.load_dataset('anscombe')
# 불린추출
# print(data[data['day'] == 'Sat'])
g1 = data[data['dataset'] == 'I']
g2 = data[data['dataset'] == 'II']
g3 = data[data['dataset'] == 'III']
g4 = data[data['dataset'] == 'IV']

# plt.plot([1,2,3],[10,20,30])
# plt.title('선그래프')           # 그래프 제목
# plt.xlabel('X값')            # 축 제목
# plt.ylabel('Y값')
# plt.xticks([1,2,3])       # x축값
# plt.yticks([10,20,30])
# plt.xlim(-5,5)          # x축 값범위(min,max)
# plt.show()

# 그래프가 위치할 기본틀(도화지) 생성
fig = plt.figure()

# 그래프 넣을 격자(영역)설정
a1 = fig.add_subplot(2,2,1)   #2행 2열 1번째 그래프
a2 = fig.add_subplot(2,2,2)
a3 = fig.add_subplot(2,2,3)
a4 = fig.add_subplot(2,2,4)

# 3.그래프 추가
a1.plot(g1['x'],g1['y'],'o')
a2.plot(g2['x'],g2['y'],'ro')
a3.plot(g3['x'],g3['y'],'go')
a4.plot(g4['x'],g4['y'],'yo')

# 4.옵션
a1.set_title('1번그룹')
a2.set_title('2번그룹')
a3.set_title('3번그룹')
a4.set_title('4번그룹')
fig.suptitle('그래프test')
fig.tight_layout()
plt.show()

# tips = sb.load_dataset('tips')
# 산점도 : 변수 2개를 사용해서 만든 그래프
# plt.scatter(tips['total_bill'], tips['tip'])
# plt.title('산점도')
# plt.xlabel('식대')
# plt.ylabel('팁')
# plt.show()

############################################################################################################################################################################################################################

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# # 한글처리
# from matplotlib import font_manager,rc
# fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
# rc('font',family=fontname)
# # -----------------
# tips=sns.load_dataset('tips')
# # print(tips)
# # # 불린추출
# # print(tips['sex']=='Female')  #True, False
# # print(tips[tips['sex']=='Female'])
# # print(tips['total_bill'].mean())   #19.78594262295082
# # print(tips['total_bill']>tips['total_bill'].mean())
# # print(tips[tips['total_bill']>tips['total_bill'].mean()])
# # ans=sns.load_dataset("anscombe")
# # # print(ans)
# # # 4개의 그룹이 평균,분산,상관관계,회귀선이 동일
# # print(ans['dataset']=='I')
# # g1=ans[ans['dataset']=='I']
# # print(g1)
# # g2=ans[ans['dataset']=='II']
# # g3=ans[ans['dataset']=='III']
# # g4=ans[ans['dataset']=='IV']
# # print(g3)
# # plt.plot([1,2,3],[10,20,30])  #plt.plot(x좌표,y좌표)
# # plt.plot([1,2,3],[10,20,30],'o')
# # plt.plot([10,20,30,60],'o--')
# # plt.show()
# # plt.plot([1,2,3],[10,20,30])
# # plt.title('선그래프')    #그래프제목
# # plt.xlabel('x값')   #축제목
# # plt.ylabel('y값')
# # # plt.xticks([1,2,3])   #x축 값
# # # plt.yticks([10,20,30])
# # plt.xlim(-5,5)     #x축 값범위(min,max)
# # plt.show()
# # #1.그래프가 위치할 기본틀(도화지) 생성
# # fig=plt.figure()
# # # 2.그래프 넣을 격자(영역)설정
# # a1=fig.add_subplot(2,2,1)   #2행 2열 1번째 그래프
# # a2=fig.add_subplot(2,2,2)
# # a3=fig.add_subplot(2,2,3)
# # a4=fig.add_subplot(2,2,4)
# # # 3.그래프 추가
# # a1.plot(g1['x'],g1['y'],'o')
# # a2.plot(g2['x'],g2['y'],'ro')
# # a3.plot(g3['x'],g3['y'],'go')
# # a4.plot(g4['x'],g4['y'],'yo')
# # # 4.옵션
# # a1.set_title('1번그룹')
# # a2.set_title('2번그룹')
# # a3.set_title('3번그룹')
# # a4.set_title('4번그룹')
# # fig.suptitle('그래프test')
# # fig.tight_layout()
# # plt.show()
# # -------
# # fig=plt.figure()
# # # a1=fig.add_subplot(1,1,1)
# # a1=fig.add_subplot(111)
# # a1.plot([1,2,3],[10,20,30])
# # a1.set_title('그래프')
# # a1.set_xlabel('x값')
# # plt.show()
# # -----------
# print(tips)
# # plt.plot(tips['total_bill'],'o')
# # plt.ylabel('식대')
# # plt.show()
# # print('최소값',tips['total_bill'].min())
# # print('최대값',tips['total_bill'].max())
# # 히스토그램:변수 1개를 사용해서 만든 그래프, 일변량 그래프
# # plt.hist(tips['total_bill'])
# # plt.hist(tips['total_bill'],bins=5)  #bins x축구간
# # plt.title('식대의 히스토그램')
# # plt.show()
# # 산점도 :변수 2개를 사용해서 만든 그래프, 이변량 그래프
# # plt.scatter(tips['total_bill'],tips['tip'])
# # plt.title('산점도')
# # plt.xlabel('식대')
# # plt.ylabel('팁')
# # plt.show()
# # 사분위수
# # 여성들이 지급한 팁금액 출력
# # print(tips['sex']=='Female')
# # print('여성이 계산한 데이터\n',tips[tips['sex']=='Female'])
# # print('여성이 지급한 팁\n',tips[tips['sex']=='Female']['tip'])
# # plt.boxplot(tips[tips['sex']=='Female']['tip'])
# # plt.title('여성이 지급한 팁')
# # plt.show()
# # plt.boxplot(tips[tips['sex']=='Male']['tip'])
# # plt.title('남성이 지급한 팁')
# # plt.show()
# # plt.boxplot([tips[tips['sex']=='Female']['tip'],
# #              tips[tips['sex']=='Male']['tip']],
# #             labels=['여자','남자'])
# # plt.title('성별별 팁 금액 상자그림')
# # plt.xlabel('성별')
# # plt.show()
# # 산점도
# # def getSex(sex):
# #     if sex=='Female':
# #         return 0
# #     else:
# #         return 1
# # tips['sextonum']=tips['sex'].apply(getSex)
# # print(tips)
# # plt.scatter(tips['total_bill'],tips['tip'],
# #     s=tips['size']*15,alpha=0.5,c=tips['sextonum'])
# # plt.title('산점도')
# # plt.xlabel('식대')
# # plt.ylabel('팁')
# # plt.show()
# data=pd.read_csv('data/accident.csv')
# print(data)
# # 1.요일별 교통사고 사망자수(단, 사망자자수 3명이상인 데이터)
#
#
