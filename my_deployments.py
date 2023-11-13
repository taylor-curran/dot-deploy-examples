from child_flows import child_flow_a, child_flow_b, child_flow_c, child_flow_d
from task_wrapped_deployments import task_wrapped_deployments
from ret_a import failing_flow
from prefect.deployments.runner import DeploymentImage
from prefect.runner.storage import GitRepository
from prefect.blocks.system import Secret


if __name__ == "__main__":
        child_flow_a.deploy(
            name="dep-child-a",
            tags=["child"],
            work_pool_name="my-k8s-pool",
            image="docker.io/taycurran/child-a:demo",
        )

        child_flow_b.deploy(
            name="dep-child-b",
            tags=["child"],
            work_pool_name="my-k8s-pool",
            image="docker.io/taycurran/child-b:demo",
        )

        child_flow_c.deploy(
            name="dep-child-c",
            tags=["child"],
            work_pool_name="my-k8s-pool",
            image="docker.io/taycurran/child-c:demo",
        )

        child_flow_d.deploy(
            name="dep-child-d",
            tags=["child"],
            work_pool_name="my-k8s-pool",
            image="docker.io/taycurran/child-d:demo",
        )

        # Parent Flow
        task_wrapped_deployments.deploy(
            name="task-wrapped-k8s",
            tags=["parent"],
            work_pool_name="my-k8s-pool",
            image="docker.io/taycurran/task-wrapped:demo",
        )


        failing_flow.deploy(
            name="failing-flow",
            tags=["parent", "len"],
            work_pool_name="my-k8s-pool",
            image="docker.io/taycurran/failing-flow:demo",
        )