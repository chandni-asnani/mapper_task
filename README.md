# mapper_task


Steps to follow:
1. Install requirements from requirements.txt file.
2. Create database
3. Create .env file and provide database credentials as given in example below.<br>
	DB_NAME='mapper_task' <br>
	DB_USER='postgres'  <br>
	DB_HOST='127.0.0.1' <br>
	DB_PASSWORD='postgres' <br>
	DB_PORT='5432' <br>
4. To dump dataset.xlsx into dataset run datastore.py file.
5. To start server run command: uvicorn main:app --reload
6. To provide input hit url: http://127.0.0.1:8000/docs#
7. Click on Try it out option to give input and fetch result.

Sample Input: 

<img width="960" alt="sample_input" src="https://user-images.githubusercontent.com/70424574/153375693-2d1ec100-d0a1-456e-ba84-55b9e4c8eca9.png">

Sample Output:

<img width="957" alt="sample_output" src="https://user-images.githubusercontent.com/70424574/153375986-4c5ed8b1-ae96-4980-9949-beac99248397.png">
