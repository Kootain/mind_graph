REMOTE_HOST=root@47.236.140.48  # 替换为实际的远程服务器用户名和地址
REMOTE_DEV_DIR=/root/coze_dev
BRANCH_NAME=kootain
DEV_PORT=5000

init:
	@if git rev-parse --verify $(BRANCH_NAME); then \
		echo "切换到分支 $(BRANCH_NAME)"; \
		git checkout $(BRANCH_NAME); \
	else \
		echo "创建分支 $(BRANCH_NAME)"; \
		git checkout -b $(BRANCH_NAME); \
		git push --set-upstream origin $(BRANCH_NAME); \
	fi
	$(MAKE) push
	ssh $(REMOTE_HOST) 'cd $(REMOTE_DEV_DIR) && git clone git@github.com:Kootain/mind_graph.git $(DEV_PORT) && cd $(DEV_PORT) && git checkout $(BRANCH_NAME) && sudo systemctl enable coze@$(DEV_PORT) && sudo systemctl start coze@$(DEV_PORT)'
	$(MAKE) log

clean:
	ssh $(REMOTE_HOST) 'sudo systemctl stop coze@$(DEV_PORT) && sudo systemctl disable coze@$(DEV_PORT) && sudo systemctl daemon-reload && rm -rf $(REMOTE_DEV_DIR)/$(DEV_PORT)'

dev:
	mkdir -p app/static/img
	python run.py

run:
	mkdir -p app/static/img
	pip install -r requirements.txt
	PORT=$(DEV_PORT) /usr/bin/python3 run.py

push:
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "存在未提交的更改，正在提交..."; \
		git add .; \
		git commit -m "Auto-commit: make commit-push"; \
		echo "正在推送到远程仓库..."; \
		git push; \
	else \
		echo "无未提交代码"; \
	fi

deploy:
	$(MAKE) push
	$(MAKE) remote-branch
	$(MAKE) log

remote-branch:
	@if [ -z "$(BRANCH_NAME)" ]; then \
		echo "Error: BRANCH_NAME is not set. Use 'make switch-branch BRANCH_NAME=your-branch' to set it."; \
		exit 1; \
	fi
	ssh $(REMOTE_HOST) 'cd $(REMOTE_DEV_DIR)/$(DEV_PORT) && git fetch && git checkout $(BRANCH_NAME) && git pull origin $(BRANCH_NAME)'


restart:
	ssh $(REMOTE_HOST) 'sudo systemctl restart coze@$(DEV_PORT)'

log:
	ssh $(REMOTE_HOST) 'sudo journalctl -u coze@$(DEV_PORT) -f'

status:
	ssh $(REMOTE_HOST) 'sudo systemctl status coze@$(DEV_PORT).service'