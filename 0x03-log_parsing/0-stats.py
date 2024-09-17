#!/usr/bin/python3
""" Log Parsing with re Module """
import re
import sys


def printFun(fileSize, statusDic):
    ''' Function to print output'''
    print("File Size =", fileSize)
    for key, value in statusDic.items():
        print(f'{key}: {value}')


def main():
    lineValidate = (
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)] '
            r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
            )
    lines = 0
    status = set(['200', '301', '400', '401', '403', '404', '405', '500'])
    statusDic = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
            }
    fileSize = 0
    try:
        while True:
            readLine = sys.stdin.readline()
            result = re.match(lineValidate, readLine)
            if result:
                if result.group(3) in status:
                    statusDic[result.group(3)] += 1
                fileSize += int(result.group(4))
            lines += 1
            if lines % 10 == 0:
                printFun(fileSize, statusDic)
    except KeyboardInterrupt:
        printFun(fileSize, statusDic)


if __name__ == '__main__':
    main()
