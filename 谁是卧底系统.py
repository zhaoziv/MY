import random as r
vote_flag=True
logs=[]
bout=0
while True:
    choose=input('\n\t1.抽取身份\t2.投票工具\t3.查询日志\t4.退出系统\n选择功能以继续……\n[1~4]:')
    if choose=='1':
        vote_flag=False
        cnt=1
        bout+=1
        people_num=int(input('请输入玩家人数:'))
        if people_num<=2:
            print('人数必须大于2人!')
        else:
            words=[]
            words.clear()
            word=input('1.随机词语:')
            words.append(word)
            word=input('2.随机词语:')
            words.append(word)
            input()
            if words[0]==words[1]:
                print('词语重复!')
            else:
                good=words[r.randint(0,1)]
                if good==word:
                    undercover=words[0]
                else:
                    undercover=words[1]
                lst=[good for i in range(people_num)]
                lst_vote=[i for i in range(people_num)]
                lst_people=['平民' for i in range(people_num)]
                undercover_index=r.randint(0,people_num-1)
                lst.pop(undercover_index)
                lst_people.pop(undercover_index)
                lst.insert(undercover_index,undercover)
                lst_people.insert(undercover_index,'卧底')
                for i in lst:
                    print('\n'*30)
                    input('按下回车出现词语')
                    print('您是{}号,词语:{}'.format(cnt,i))
                    logs.append(['回合'+str(bout)+','+str(cnt)+'号词语:'+str(i)])
                    cnt+=1
                    input('返回')
                    print('\n'*30)
    elif choose=='2':
        if vote_flag:
            print('你尚未开始一场游戏!')
        else:
            vote_input=int(input('请输入投票数量最多的玩家序号:'))
            if vote_input-1 in lst_vote:
                print('该玩家的身份为:'+lst_people[vote_input-1])
                if lst_people[vote_input-1]=='卧底':
                    print('\n平民胜利')
                elif lst_people[vote_input-1]=='平民':
                    print('\n游戏继续')
            else:
                print('该玩家不存在!')
    elif choose=='3':
        for l in logs:
            print(l,end='\n')
    elif choose=='4':
        break
    else:
        print('输入有误!')