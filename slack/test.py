import slack_sdk

token = "xoxb-4713072259427-4719125015396-Sy66CcpUeHg3Ddf5A0phb8ue"

client = slack_sdk.WebClient(token=token)

client.chat_postMessage(channel="#tokbottest", text="hellow world!!")
