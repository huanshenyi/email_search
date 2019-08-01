import random
import smtplib
import logging
import time

import dns.resolver

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')
#
# logger = logging.getLogger()


def fetch_mx(host):
    # logger.info('メールサーバー探査中')
    answers = dns.resolver.query(host, 'MX')
    res = [str(rdata.exchange)[:-1] for rdata in answers]
    # logger.info('検査結果：%s' % res)
    return res


def verify_istrue(email):
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    final_res = {}
    name, host = email.split('@')
    host = random.choice(fetch_mx(host))
    # logger.info('サーバーへ接続中...：%s' % host)
    s = smtplib.SMTP(host, timeout=10)
    helo = s.docmd('HELO chacuo.net')
    # logger.debug(helo)
    send_from = s.docmd('MAIL FROM:<den@bell-face.com>')
    # logger.debug(send_from)
    send_from = s.docmd('RCPT TO:<%s>' % email)
    # logger.debug(send_from)
    if send_from[0] == 250 or send_from[0] == 451:
        final_res["date"] = nowTime
        final_res["name"] = email
        final_res["address"] = "存在します"
    elif send_from[0] == 550:
        final_res["date"] = nowTime
        final_res["name"] = email
        final_res["address"] = "存在しません"
    else:
        final_res["date"] = nowTime
        final_res["name"] = email
        final_res["address"] = "不明です"
        s.close()
        # return {"date": nowTime, "name": need_verify, "address": final_res[need_verify]}

    return final_res


if __name__ == '__main__':
    final_list = verify_istrue('306581901@qq.com')
    print(final_list)