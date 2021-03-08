# TODO 本地连接信息
LOCAL_HOST= '127.0.0.1'
LOCAL_PORT= 3306
LOCAL_USERNAME = 'root'
LOCAL_PASSWORD = '123456'

# TODO 写入库地址
USERNAME = 'xuwenjie'
PASSWORD = 'xwjxws123A@A@123'

UCO_MASTER_HOST = '10.2.4.66'
UCO_MASTER_PORT = 5019
YY_MASTER_HOST = '10.2.1.55'
YY_MASTER_PORT = 4008
EL_MASTER_HOST = '10.2.4.66'
EL_MASTER_PORT = 5012
ELC_MASTER_HOST = '10.2.4.66'
ELC_MASTER_PORT = 5009

# TODO 查询库地址
UCO_HOST = 'db20b4.uco.com'
UCO_PORT = 5400
YY_HOST = 'dbz1.uco.com'
YY_PORT = 3711
EL_HOST = 'db20b1.uco.com'
EL_PORT = 5100
ELC_HOST = 'db20b2.uco.com'
ELC_PORT = 5200
PRO_HOST = 'dbz1.uco.com'
PRO_PORT = 3701

DB_ENV = {
    'UCO':{
        'HOST':UCO_HOST,
        'PORT':UCO_PORT,
        'USERNAME':USERNAME,
        'PASSWORD':PASSWORD,
    },
    'YY':{
        'HOST': YY_HOST,
        'PORT': YY_PORT,
        'USERNAME': USERNAME,
        'PASSWORD': PASSWORD,
    },
    '3PL':{
        'HOST': PRO_HOST,
        'PORT': PRO_PORT,
        'USERNAME': USERNAME,
        'PASSWORD': PASSWORD,
    },
    'EL':{
        'HOST': EL_HOST,
        'PORT': EL_PORT,
        'USERNAME': USERNAME,
        'PASSWORD': PASSWORD,
    },
    'ELC':{
        'HOST': ELC_HOST,
        'PORT': ELC_PORT,
        'USERNAME': USERNAME,
        'PASSWORD': PASSWORD,
    },
}