ARG project_id
ARG base_artifact
ARG base_image

FROM australia-southeast1-docker.pkg.dev/mineral-anchor-361313/base-dbt-docker/working-image
COPY . /app/
RUN echo "dbt via docker"

RUN chmod +x /app/dbt_run.sh
WORKDIR /app/
ENTRYPOINT ["/app/dbt_run.sh"]
