import json

def print_con(abonent):
    print('Name '+list(abonent)[0]+"\n",'phones'+"\n")
    for i in abonent[list(abonent)[0]]['phones']:
        print(i+"\n")
    print('City '+abonent[list(abonent)[0]]['city']+"\n",'Mail '+abonent[list(abonent)[0]]['mail']+"\n",'Sex '+abonent[list(abonent)[0]]['sex']+"\n",'Birthday '+abonent[list(abonent)[0]]['birthday']+"\n",' ')

print('if you need help (Alt+13080) ')
open('information_sourse.json','a')
#ib={'Contact name':{'phones':['+7000000','+7888888'],'city':'MSK','mail':'mamont@vk.com','sex':'M','birthday':'01.01.111'}}
while True:
    command=input()
    if command=='↑':
        print('list-see all numbers','new-add number','search-search contact','del-dellit a contact ','red-change information in contact')
    elif command == 'list':
        with open('information_sourse.json','r') as read_ib:
            tmp=json.load(read_ib)
            for i in tmp:
                print_con(i)
    elif command=='new':
        try:
            with open('information_sourse.json','r') as read_ib:
                tmp=json.load(read_ib)
        except:
            print('empty')
        contact=input('Name ')
        try:
            if contact in tmp:
                print('this name is reserved')
            else:
                count=input('How many phones do contact have? ')
                phones=[0]*int(count)
                phones=list(map(lambda x: input('phone'),phones))
                city=input('City ')
                mail=input('mail ')
                sex=input('sex')
                birthday=input('birthday ')
                ib={contact:{'phones':phones,'city':city,'mail':mail,'sex':sex,'birthday':birthday}}
                try :
                    with open('information_sourse.json','r') as add_ib:
                        tmp=list(json.load(add_ib))
                        tmp.append(ib)
                    with open('information_sourse.json','w') as add_ib:
                        json.dump(tmp,add_ib)
                except :
                    with open('information_sourse.json','a') as add_ib:
                        json.dump(list(ib),add_ib)
                print('new conyact added')
        except:
            count=input('How many phones do contact have? ')
            phones=[0]*int(count)
            phones=list(map(lambda x: input('phone'),phones))
            city=input('City ')
            mail=input('mail ')
            sex=input('sex')
            birthday=input('birthday ')
            ib={contact:{'phones':phones,'city':city,'mail':mail,'sex':sex,'birthday':birthday}}
            try :
                with open('information_sourse.json','r') as add_ib:
                    tmp=list(json.load(add_ib))
                    tmp.append(ib)
                with open('information_sourse.json','w') as add_ib:
                    json.dump(tmp,add_ib)
            except :
                with open('information_sourse.json','a') as add_ib:
                    ib1=[]
                    ib1.append(ib)
                    json.dump(list(ib1),add_ib)
                    print('new conyact added')
    elif command=='search':
        request=input('contact ')
        try:
            with open('information_sourse.json','r') as read_ib:
                tmp=json.load(read_ib)
                for i in tmp:
                    if request in i:
                        print_con(i)
                    else:
                        print('no contact')
            print('done')
        except:
            print('empty')
    elif command=='del':
        request=input('contact ')
        try:
            with open('information_sourse.json','r') as read_ib:
                tmp=json.load(read_ib)
                for i in tmp:
                    if request in i:
                        print_con(i)
                        if input('Are you sure,that you want to dellit this contact? [y]es [n]o')=='y':
                            index_to_del=tmp.index(i)
            try:
                tmp.pop(index_to_del)
                with open('information_sourse.json','w') as add_ib:
                        json.dump(tmp,add_ib)
                print('done')
            except:
                None
        except:
            print('empty')   
    elif command=='red':
        request=input('contact ')
        try:
            with open('information_sourse.json','r') as read_ib:
                tmp=json.load(read_ib)
                for i in tmp:
                    if request in i:
                        print_con(i)
                        if input('Are you sure,that you want to change this contact? [y]es [n]o')=='y':
                            index_to_red=tmp.index(i)
                            if input('do you whant to change name? [y]es/[n]o')=='y':
                                name=input('new contact name ')
                            else:
                               name=request
                            phone_red_var=input('do you whant to change phones? [y]es/[n]o/[a]dd new')
                            if phone_red_var=='y':
                                phones=tmp[index_to_red][request]['phones']
                                for i in phones:
                                    print(i)
                                    if input('do you whant to change this phone? [y]es/[n]o')=='y':
                                        phones[phones.index(i)]=input('phone ')
                                    elif phone_red_var=='a':
                                        phones.append(input('phone '))
                            if input('do you whant to change city? [y]es/[n]o')=='y':
                                city=input('new city ')
                            else:
                                city=tmp[index_to_red][request]['city']
                            if input('do you whant to change mail? [y]es/[n]o')=='y':
                                mail=input('new mail ')
                            else:
                                mail=tmp[index_to_red][request]['mail']
                            if input('do you whant to change sex? [y]es/[n]o')=='y':
                                sex=input('new sex ')
                            else:
                                sex=tmp[index_to_red][request]['sex']
                            if input('do you whant to change birthday? [y]es/[n]o')=='y':
                                birthday=input('new birthday ')
                            else:
                                birthday=tmp[index_to_red][request]['birthday']
                            ib={name:{'phones':phones,'city':city,'mail':mail,'sex':sex,'birthday':birthday}}
                            print_con(ib)
                            tmp[index_to_red]=ib
                            with open('information_sourse.json','w') as red_ib:
                                json.dump(tmp,red_ib)
                                print('done')
        except:
            print('empty')
    
            
            

