#coding: UTF-8

import slackweb

slack = slackweb.Slack(url="https://hooks.slack.com/services/********************")
attachments=[]
attachment={"pretext": "Incomingwebhooksを使用",
"color": "good",
"title": "高知工科大学",
"title_link": "https://www.kochi-tech.ac.jp",
"text": "高知工科大学ホームページのリンク",
}
attachments.append(attachment)
slack.notify(text="pythonでの投稿", username="hooksan", attachments=attachments)
