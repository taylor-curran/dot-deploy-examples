from prefect import flow
from prefect.deployments import Deployment

@flow
def my_flow():
    print('hi')
    return 1

Deployment.build_from_flow(flow=my_flow, apply=True, name="my-dep")