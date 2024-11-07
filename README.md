### Instructions to Set Up and Access the Project
 
1. **Install Docker Desktop**
   - Visit the official installation guide [here](https://docs.docker.com/engine/install/).
2. **Install Docker Compose**
   - Follow the installation steps [here](https://docs.docker.com/compose/install/).
 
If you have already installed Docker and Docker compose, clean up your volumes before running the containers with the following command: docker-compose down -v
If you don't clean up your volumes, there is a possibility that the db's won't be created. 

3. **Download and Set Up the Project**
   - Download the ZIP folder containing the project files.
   - Unzip (extract) the folder.
 
4. **Run the Project with Docker Compose**
   - When everything is installed open a terminal.
   - Navigate to the folder where you saved the unzipped project.
   - Run the following command to start the project:
     ```bash
     docker-compose up --build -d
     ```
   - This command will start all containers for the project. You can view them running in the Docker Desktop app.
 
5. **Access the Database**
   - Open your web browser and go to `http://localhost:8080`.
   - On the login page, enter the following details:
     - **Server**: Choose `user_db`, `product_db`, `cart_order_db`, `sales_payment_db`, or `return_refund_db` (depending on the database you want to access).
     - **User**: `root`
     - **Password**: `root_password`
   - After logging in, select the database you want to explore from the dropdown menu on the left. You will now have live access to the database and its tables.
 
6. **Interacting with the Database via API**
   - Open a new terminal window to send requests to the API.
   - **Examples of API requests**:
     - **Show all customers**:
       ```powershell
       Invoke-RestMethod -Uri http://localhost:8000/customers -Method Get
       ```
     - **Create a new customer**:
       ```powershell
       $body = @{
           customer_id = 1
           email = "john.doe@example.com"
           password = "password123"
           first_name = "John"
           last_name = "Doe"
           phone_number = "1234567890"
           rewards = 100
           street_address = "123 Main St"
           city = "Anytown"
           state = "CA"
           zip_code = "12345"
       } | ConvertTo-Json
 
       Invoke-RestMethod -Uri http://localhost:8000/customers -Method Post -ContentType "application/json" -Body $body
       ```
     - **Delete a customer**:
       ```powershell
       Invoke-RestMethod -Uri http://localhost:8000/customers/1 -Method Delete
       ```
 
   - Refresh `http://localhost:8080` in your browser to see the changes in the database.
