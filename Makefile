# yeah sorry
service-deploy:
	scp -i deploy -r service deploy@service1.newspapyr.co:/var/webapp/
	ssh -i deploy deploy@service1.newspapyr.co pkill -HUP gunicorn

service-ssh:
	ssh -i deploy deploy@service1.newspapyr.co

web-deploy:
	scp -i deploy -r frontend deploy@web1.newspapyr.co:/var/webapp/
	ssh -i deploy deploy@web1.newspapyr.co pkill -HUP gunicorn

web-ssh:
	ssh -i deploy deploy@web1.newspapyr.co
