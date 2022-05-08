# 강제종료하기
ps -ef | grep 'python app.py' | awk '{print $2}' | xargs kill
