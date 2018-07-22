#-*-coding:UTF-8-*-
import pymysql
import datetime
from config import MYSQL_CONFIG
from Log_Info.error_output import logError,logWarning

connection = pymysql.connect(host=MYSQL_CONFIG['host'], port=MYSQL_CONFIG['port'], user=MYSQL_CONFIG['user'], password=MYSQL_CONFIG['password'],
                             db=MYSQL_CONFIG['db'],charset=MYSQL_CONFIG['charset'], cursorclass=pymysql.cursors.DictCursor)





def to_sql_news(*args,secu_code,secu_name,code):
    '''
    插入新闻信息information_plate_news, information_plate_news_se
    '''
    try:
        connection.ping()
    except:
        connection.ping(True)
    cursor = connection.cursor()
    sql = "INSERT INTO information_plate_news (_id,db_source_id,status,category,title,abstract,content,author,source,publish," \
          "ipublish,createtime,icreatetime,s_url,dt_url,attitude,responsetime,editlock,updatetime,lastuser) VALUES " \
          "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_se = "INSERT INTO information_plate_news_se (info_id, db_source_id, type, secu_code, secu_name, code) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(args))
    # connection.commit()
    # type  1-股票 2-债券 3-基金 21-题材
    # print((args[0],args[1],1,secu_code,secu_name,code))
    cursor.execute(sql_se,(args[0],args[1],1,secu_code,secu_name,code))
    connection.commit()
    connection.close()


def get_codes_info(mk_id,sec_type):
    '''
    mk_id: list
    sec_type
    '''
    try:
        connection.ping()
    except:
        connection.ping(True)
    sql = 'SELECT `code`,dt_code,`name`,sec_type,market_id FROM t_stock_dict WHERE market_id in ({}) AND sec_type={}'.format(str(mk_id).replace('[','').replace(']',''),sec_type)
    cursor = connection.cursor()
    cursor.execute(sql)
    tot_info = cursor.fetchall()
    connection.close()
    return tot_info

def news_lastpublish(code):
    try:
        connection.ping()
    except:
        connection.ping(True)
    # 数据库个股最晚新闻信息
    sql = "SELECT  A.`code`,A.info_id,A.secu_code,A.secu_name,B.title,B.publish,B.createtime  FROM information_plate_news_se A JOIN information_plate_news B WHERE A.info_id = B._id AND A.`code` = '{}' ORDER BY  B.publish DESC".format(code)
    cursor = connection.cursor()
    cursor.execute(sql)
    last_info = cursor.fetchone()
    # print(last_info)
    init_time = datetime.datetime.strptime('2000-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
    connection.close()
    return last_info if last_info != None else {'publish':init_time,'_id':'0000000001'}

# print(news_lastpublish('0101600631'))

def news_id(info_id,db_source_id,secu_code,secu_name,dt_code):
    try:
        connection.ping()
    except:
        connection.ping(True)
    # db_source_id -98 同花顺   -97 东方财富
    sql = "SELECT * FROM information_plate_news_se WHERE info_id={} AND db_source_id = '-97'".format(info_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    info = cursor.fetchone()
    # print(info)
    if info != None:
        bs = 0
        sql_se = "INSERT INTO information_plate_news_se (info_id, db_source_id, type, secu_code, secu_name, code) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql_se,(info_id,db_source_id,1,secu_code,secu_name,dt_code))
        connection.commit()
    else:
        bs = 1
    connection.close()
    return bs


# print(news_lastpublish('0001000001xxx'))


def insert_stock_basics(*args):
    try:
        connection.ping()
    except:
        connection.ping(True)
    cursor = connection.cursor()
    sql = "INSERT INTO `stock_basics` ( `stock_code`, `report_date`, `mainbusiincome`, `mainbusiprofit`, " \
          "`totprofit`, `netprofit`, `totalassets`, `totalliab`, `totsharequi`, `basiceps`, `naps`, `opercashpershare`, " \
          "`peropecashpershare`, `operrevenue`, `invnetcashflow`, `finnetcflow`, `chgexchgchgs`, `cashnetr`, `cashequfinbal`,createtime) " \
          "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s);"
    try:
        cursor.execute(sql,(args))
        connection.commit()
    except pymysql.err.IntegrityError:
        pass
    except Exception as e:
        logError('{},{},{}'.format(args[0],args[1],str(e)))

    connection.close()



def get_stock_info():
    try:
        connection.ping()
    except:
        connection.ping(True)
    d = {}
    cursor = connection.cursor()
    # sql = "SELECT code,market FROM stock_dict "
    sql = "SELECT * FROM stock_dict A WHERE NOT EXISTS (SELECT * FROM stock_basics B WHERE B.stock_code = A.`code`)"
    cursor.execute(sql)
    info_list = cursor.fetchall()
    connection.close()
    return info_list


def insert_tot_stocks(*args):
    '''
    读取tushare 所有股票名及代码
    :param args:
    :return:
    '''
    try:
        connection.ping()
    except:
        connection.ping(True)
    cursor = connection.cursor()
    sql = "INSERT INTO stock_dict (name,code,market,createtime) VALUES (%s,%s,%s,%s)"
    try:
        cursor.execute(sql,(args))
        connection.commit()
    except pymysql.err.IntegrityError:
        pass
    except Exception as e:
        logError('{},{},{}'.format(args[0],args[1],str(e)))

    connection.close()

# insert_tot_stocks('读者传媒','603999','sh')

