kubernetes_min_pod = KubernetesPodOperator(
    # The ID specified for the task.
    task_id="pod-ex-minimum",
    # Name of task you want to run, used to generate Pod ID.
    name="pod-ex-minimum",
    # Entrypoint of the container, if not specified the Docker container's
    # entrypoint is used. The cmds parameter is templated.
    cmds=["echo"],
    namespace='dbt-ns', 
    # k8s service account name created earlier
    service_account_name='dbt-composer-sa@mineral-anchor-361313.iam.gserviceaccount.com', 
    # Ensures that the right node-pool is used
    nodeSelector={'http://cloud.google.com/gke-nodepool': 'dbt-pool'}, 
    # Ensures that cache is always refreshed
    image_pull_policy='Always', 
    # Artifact image of dbt repo
    image='australia-southeast1-docker.pkg.dev/mineral-anchor-361313/my-dbt-repo/my-image', 
    # links to ENTRYPOINT in .sh file
)