train: 
	docker build . -f docker/bot/coach.Dockerfile -t lappis/coach:latest

test-dialogue:
	docker-compose run --rm bot make e2e