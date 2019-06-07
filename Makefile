DESTROY=docker rmi white-matter-hyperintensities-
BUILD_L=docker build -f Dockerfile-
BUILD_R=-t white-matter-hyperintensities-
RUN=docker run -p 8888:8888 -d --name wmh --rm -v $(shell pwd):/app white-matter-hyperintensities-

destroy:
	${DESTROY}gpu
.PHONY: destroy

destroy-cpu:
	${DESTROY}cpu
.PHONY: destroy-cpu

build:
	${BUILD_L}gpu ${BUILD_R}gpu .
.PHONY: build

build-cpu:
	${BUILD_L}cpu ${BUILD_R}cpu .
.PHONY: build-cpu

run:
	${RUN}gpu
.PHONY: run

run-cpu:
	${RUN}cpu
.PHONY: run-cpu

shell:
	docker exec -it wmh bash
.PHONY: shell

stop:
	docker stop wmh
.PHONY: stop
