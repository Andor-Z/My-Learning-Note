##4�������ļ��У�
* app:Flask����
    - app/models.py ���ݿ�ģ��
    - app/email.py �����ʼ�֧�ֺ���
* migrations: ���ݿ�Ǩ�ƽű�
* tests: ��Ԫ���Ա�д
* venv

* requirements.txt �г�������������
* config.py ��������
* manage.py �������������ĳ�������





### ϸС֪ʶ��

* ���û���������

Mac Linux ��
`$ export MAIL_USERNAME = <flaskm@example.com>`


Windows :
`(venv) > set MAIL_USERNAME = <flaskm@example.com>`


* ��ȡ����������
```
import os
os.environ.get('MAIL_USERNAME')
```

* ��������������汾  
`(venv) > pip freeze >requirements.txt`  

* ��װ������
`(venv) > pip intall -r requirements.txt`


### ������֢

* Python ���⻷���� ʹ��pip ��װ�°� ����`Fatal error in launcher: Unable to create process using`
    ����취��
            Windows������ʹ�ã�
        python -m pip install xxx���滻 install xxx��







* [python�� from . import ���������Ǹ���](https://www.zhihu.com/question/28688151)

* [4����ͼ�����еı�����](https://segmentfault.com/a/1190000002172627)