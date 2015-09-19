# yeah sorry
service-deploy:
	scp -i deploy -r service deploy@service1.newspapyr.co:/var/webapp/
	ssh -i deploy deploy@service1.newspapyr.co pkill -HUP gunicorn

service-ssh:
	ssh -i deploy deploy@service1.newspapyr.co
