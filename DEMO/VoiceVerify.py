#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from SDK.CCPRestSDK import REST

#���ʺ�
accountSid= '8a216da869dca6190169dd10cead00ae';

#���ʺ�Token
accountToken= 'e9dbe824b1144aa8aa4009b54a752146';

#Ӧ��Id
appId='8aaf070869dc0b880169e22fb0510359';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com';

#����˿� 
serverPort=8883;

#REST�汾��
softVersion='2013-12-26';

    # ������֤��
    # @param verifyCode  ��ѡ����   ��֤�����ݣ�Ϊ���ֺ�Ӣ����ĸ�������ִ�Сд������4-8λ
    # @param playTimes  ��ѡ����   ���Ŵ�����1��3��
    # @param to ��ѡ����    ���պ���
    # @param displayNum ��ѡ����    ��ʾ�����к���
    # @param respUrl ��ѡ����    ������֤��״̬֪ͨ�ص���ַ����ͨѶƽ̨�����Url��ַ���ͺ��н��֪ͨ
    # @param lang ��ѡ����    ��������
    # @param userData ��ѡ����    ������˽������

def voiceVerify(verifyCode,playTimes,to,displayNum,respUrl,lang,userData):
    #��ʼ��REST SDK
    rest = REST(serverIP,serverPort,softVersion)
    rest.setAccount(accountSid,accountToken)
    rest.setAppId(appId)
    
    result = rest.voiceVerify(verifyCode,playTimes,to,displayNum,respUrl,lang,userData)
    print(result)
    for k,v in result.iteritems(): 
        
        if k=='VoiceVerify' :
                for k,s in v.iteritems(): 
                    print ('%s:%s' % (k, s))
        else:
            print ('%s:%s' % (k, v))
   
   
voiceVerify(445566,2,18090531196,"","",'zh-en',"")