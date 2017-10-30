import redis
import json
import csv


def ip_to_score(ip_address):
    score = 0
    for v in ip_address.split('.'):
        score = score * 256 + int(v, 10)
    return score


def import_ips_to_redis(conn, filename):
    csv_file = csv.reader(open(filename, 'r'))
    for count, row in enumerate(csv_file):

        start_ip = row[0] if row else ''
        if 'i' in start_ip.lower():
            continue
        if '.' in start_ip:
            start_ip = ip_to_score(start_ip)
        elif start_ip.isdigit():
            start_ip = int(start_ip, 10)
        else:

            continue

        # 构建唯一城市ID。
        city_id = row[2] + '_' + str(count)
        # 将城市ID及其对应的IP地址分值添加到有序集合里面。
        conn.zadd('ip2cityid:', city_id, start_ip)


def import_cities_to_redis(conn, filename):
    for row in csv.reader(open(filename, 'rb')):
        if len(row) < 4 or not row[0].isdigit():
            continue
        row = [i.decode('latin-1') for i in row]

        city_id = row[0]
        country = row[1]
        region = row[2]
        city = row[3]
        # 将城市信息添加到Redis里面。
        conn.hset('cityid2city:', city_id,
            json.dumps([city, region, country]))


def find_city_by_ip(conn, ip_address):

    if isinstance(ip_address, str):                        #A
        ip_address = ip_to_score(ip_address)               #A

    # 查找唯一城市ID。
    city_id = conn.zrevrangebyscore(                       #B
        'ip2cityid:', ip_address, 0, start=0, num=1)       #B

    if not city_id:
        return None

    # 将唯一城市ID转换为普通城市ID。
    city_id = city_id[0].partition('_')[0]                 #C
    # 从散列里面取出城市信息。
    return json.loads(conn.hget('cityid2city:', city_id))  #D




if __name__ == '__main__':
    conn = redis.Redis()

    # import_ips_to_redis(conn, './GeoIPCountryWhois.csv')

    ip_address = ip_to_score('47.94.110.194')
    city_id = conn.zrevrangebyscore(                       #B
        'ip2cityid:', ip_address, 0, start=0, num=1)
    print(city_id)


