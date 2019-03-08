"""
@author: Leegeunhyeok
@date: 2019.03.08
"""

import base64

# 읽어올 파일, 저장할 파일
target_file = './sample.txt'
result_file = './result.txt'

# 읽어들인 라인 수
read_lines = 0
# 지정한 주기마다 진행상태 출력
term = 100

try:

    save_file = open(result_file, 'a')
    with open(target_file, 'r') as file_lines:

        # 모든 라인 읽어들이기
        for file_line in file_lines:

            try:
                # Base64로 인코딩 후 파일 저장
                b64_encoded = base64.b64encode(file_line)
                save_file.write(b64_encoded + '\n')

            except Exception as e:
                print 'Write file error, %s'

            # 지정한 주기에 도달할 때 마다 진행상태 출력
            read_lines += 1
            if read_lines % term == 0:
                print '%s lines done' % read_lines

except IOError as ioe:
    print ioe

except Exception as e:
    print e

finally:
    print 'Exit'
    try:
        save_file.close()

    except:
        pass
