To run the application:

Make sure you have Docker installed on your system.
Clone the repository containing the Django application.
Navigate to the repository directory in your terminal.
Build the Docker image using the following command:

docker build -t exam .

Run the Django development server using the following command:

docker run -p 8000:8000 exam


Access the Django admin interface at http://localhost:8000/admin/.
.

The following API endpoints are available:

/api/tasks/ - GET, POST: Retrieve a list of tasks or create a new task.
/api/categories/ - GET, POST: Retrieve a list of categories or create a new category.



To update or delete file you need to be permissioned as admin(login:admin, password:mypassowrd).

To create a new task:

curl -X POST -H "Content-Type: application/json" -d '{"title": "My Task", "description": "This is my task.", "completed": false, "category": 1}' http://localhost:8000/api/tasks/


To retrieve a list of tasks:

curl http://localhost:8000/api/tasks/

To retrieve a specific task:

curl http://localhost:8000/api/tasks/1/

To update a specific task:

curl -u username:password -X PUT -H "Content-Type: application/json" -d '{"title": "My Updated Task", "description": "This is my updated task.", "completed": true, "category": 1}' http://localhost:8000/api/tasks/1/

To delete a specific task:

curl -u username:password -X DELETE http://localhost:8000/api/tasks/1/

