from prefect import flow
import time
from prefect.blocks.notifications import SlackWebhook

def my_hook(flow, flow_run, state):
    slack_webhook_block = SlackWebhook.load("my-slack-notifications")
    slack_webhook_block.notify("This is a failure hook!")

@flow(on_failure=[my_hook], retries=3)
def failing_flow():
    time.sleep(5)
    raise ValueError("oops!")

if __name__ == "__main__":
    failing_flow()