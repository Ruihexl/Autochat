def get_context(auth,chanel_id):

    headr = {
        "Authorization": auth,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    chanel_id = random.choice(chanel_list)
    url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(chanel_id)
    print(url)
    res = requests.get(url=url, headers=headr)

    result = json.loads(res.content)
    result_list = []
    for context in result:
        if ('<') not in context['content'] :
            if ('@') not in context['content'] :
                if ('http') not in context['content']:
                    if ('?') not in context['content']:
                        result_list.append(context['content'])

    return random.choice(result_list)


def chat(chanel_list,authorization):
      header = {
          "Authorization": authorization,
          "Content-Type": "application/json",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
      }
      for chanel_id in chanel_list:
          msg = {
              "content": get_context(authorization,chanel_id),
              "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
              "tts": False,
          }
          url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
          try:
              res = requests.post(url=url, headers=header, data=json.dumps(msg))
              print(res.content)
          except:
              pass
          continue
      time.sleep(random.randrange(10, 30))


if __name__ == "__main__":
    chanel_list = ["复制并黏贴群聊号"]  # 这里是群聊号（url最右边）
    authorization_list = "复制并黏贴auth认证数值" # 这里auth认证信息
    while True:
        try:
            chat(chanel_list,authorization_list)
            sleeptime = random.randrange(125, 245) #发送间隔时间为125到245之间的随机数(秒)
            time.sleep(sleeptime)
        except:
            break
