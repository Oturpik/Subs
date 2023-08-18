Problem Statement: 
You've been assigned to create a simple microservices application using AWS containers. The application consists of two microservices: a front-end that displays inspirational quotes and a backend that provides quote data.

Guidelines/Goals:

1.	Containerize Microservices:
Create a Docker container for the front-end using a basic HTML page.
Create a Docker container for the back-end using a lightweight Python web server.
2.	Set Up ECS Cluster:
Create an Amazon ECS cluster to manage the microservices.
Define task definitions for each microservice, specifying the container images and ports.
3.	Deploy Microservices:
Launch the microservices as ECS services within the cluster.
Configure an Application Load Balancer to distribute traffic to the front-end
microservice.
4.	Test Communication:
Ensure that the front-end microservice can retrieve quotes from the back-end.
Test the complete application by accessing the load balancer's DNS name.


 Step 1: 
Containerize Microservices:
Front-end Microservice:
1. Create a directory for the front-end microservice.
2. Place the basic HTML page files (index.html, CSS, etc.) in the directory.
3. Create a `Dockerfile` in the same directory to build the front-end container:
4. Build the Docker container: use docker build -t frontend-microservice .

ecr.png

Back-end Microservice:
1. Create a directory for the back-end microservice.
2. Place the Python web server files in the directory.
3. Create a `Dockerfile` in the same directory to build the back-end container:
4. Build the Docker container: use docker build -t backend-microservice .

services.png

Step 2: Set Up ECS Cluster:
1. Log in to the AWS Management Console.
2. Navigate to the Amazon ECS dashboard.
3. Create a new ECS cluster.

microservices.png

Step 3: Deploy Microservices:
Define Task Definitions:
1. Create an ECS task definition for the front-end microservice:
   - Specify the container image for the front-end, use the frontend image.
   - Define the port mapping for the container (e.g., port 80).
2. Create another ECS task definition for the back-end microservice:
   - Specify the container image for the back-end.
   - Define the port mapping for the container (e.g., port 8000).

Launch ECS Services:
1. Create an ECS service for the front-end microservice using the task definition.
2. Create another ECS service for the back-end microservice using its task definition.

Step 4. Configure Load Balancer and Test Communication:
1. Create an Application Load Balancer (ALB) in the AWS Management Console.
2. Configure the ALB to distribute traffic to the front-end microservice's ECS service.
3. Test the communication between the front-end and back-end microservices:
   - confirm that the front-end microservice is configured to make API calls to the back-end microservice using the ALB's DNS name.
   - Test accessing the ALB's DNS name in a web browser to see if the front-end displays inspirational quotes retrieved from the back-end.
In the Frontend script ;

•	Index.html contains the basic structure of the webpage, including a title, a container for the quote, and a button to fetch a new quote.
•	Styles.css provides basic styling to format the appearance of the webpage.
•	Script.js adds interactivity to the webpage, fetching a quote from the backend microservice when the "get quote" button is clicked and updating the displayed quote.
•	The Dockerfile for the frontend service should be in the same directory.
To fetch data from the backend microservice, the front-end code will use HTTP requests to the appropriate endpoint on the backend microservice's API. The front-end code sends a GET request to the `/quote` endpoint of the backend microservice. The backend microservice processes the request and responds with a randomly chosen quote.
To update the front-end code to fetch quotes from the new backend microservice endpoint, 
1. Open the `index.html` file and find the following line of code to fetches quotes from the backend:
const response = await fetch('/quote');
2. Update the line to include the complete URL of the backend microservice. 
When users click the "Get Quote" button on the front-end webpage, the microservice should ideally retrieve quotes from the updated backend microservice that you deployed.
To set up the ECS Cluster
 From the AWS Management Console, search for "ECS" or find "Elastic Container Service".
Create a New ECS Cluster:
   - Click the "Create Cluster" button.
   - Configure the cluster settings, such as cluster name, EC2 instance type, and number of instances.
   - Optionally, you can configure the VPC, subnets, and security groups. This should be created alongside the instances.
   - Review the settings and create the cluster.

To Define Task Definitions:
1. Create Task Definitions for Microservices:
   - In the ECS Dashboard, click on the newly created cluster.
   - Click "Task Definitions" in the left sidebar.
   - Click "Create new Task Definition."
   - Choose the launch type compatibility as "EC2."
   - For each microservice (front-end and back-end):
     - Enter a name for the task definition.
     - Click "Add container" to define a container for the microservice:
       - Enter a container name.
       - Enter the image URI (e.g., the Amazon ECR repository URL used to upload the images).
       - Configure the essential container settings, such as CPU and memory limits, environment variables, and port mappings.
     - Click "Add."

Launch ECS Services:
Create ECS Services:
   - In the ECS Dashboard, click on the cluster.
   - Click the "Services" tab and then the "Create" button.
   - For each microservice (front-end and back-end):
     - Choose the previously created task definition.
     - Configure the service settings, such as desired count (number of instances) and launch type.
     - Choose the VPC, subnets, and security groups.
     - Optionally, configure load balancing and auto scaling settings.
     - Review and create the service.

Configure Load Balancer and Test Communication:
Create an Application Load Balancer (ALB):
   - In the AWS Management Console, search for "Load Balancers" or find it under the "Networking & Content Delivery" section.
   - Click "Create Load Balancer."
   - Choose "Application Load Balancer."
   - Configure the load balancer settings, including name, listeners, and availability zones.
   - Configure security settings (security groups) for the load balancer.
   - Configure routing if needed (target groups).
   Review and create the load balancer.

2. Update Security Groups and Target Groups:
   - In the load balancer configuration, make sure the security groups allow traffic from the VPC and subnets.
   - Make sure the target groups are correctly associated with the ECS services.

3. Test Communication:
   - Obtain the DNS name of the ALB from the AWS Management Console.
   - Access the DNS name in a web browser to test the application.
   - You should see the front-end displaying quotes fetched from the back-end microservice.
NOTE
The frontend service worked well but the backend service had issues. I will continue troubleshooting it.

frontlb.png