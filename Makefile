destroy:
	docker rmi white-matter-hyperintensities
.PHONY: destroy

build:
	docker build -t white-matter-hyperintensities .
.PHONY: build

run:
	docker run -p 8888:8888 -it --name wmh --rm -v $(shell pwd):/app -v ~/.ssh:/root/.ssh white-matter-hyperintensities bash
.PHONY: run
