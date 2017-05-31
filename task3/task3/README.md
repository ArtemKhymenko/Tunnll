Task 3. Adaptive landing page with Django

To use this Django app you should:
 - copy this repo,
 - install python and django,
 - in directory with manage.py run "python manage.py runserver",
 - open http://127.0.0.1:8000/ in browser.

To run this Django app via Docker:
 - in directory with Dockerfile:
  - "sudo docker build -t task3 ." - this command build image using our Dockerfile
  - "sudo docker run -t task3" - this command run container based on just built image and starting Django server.
  Django app is available at http://0.0.0.0:8000 in browser
