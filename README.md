Deployment:
1. Install Docker and Run Docker
2. Clone repo ``` git clone https://github.com/inbasu/Y_LAB ```
3. Go to directory with docker files
4. Build and run ``` docker-compose up --build``` or ```docker-compose up -d --build```

Tests:
![Снимок экрана от 2023-07-23 14-28-30](https://github.com/inbasu/Y_LAB/assets/13472561/368791fd-4f97-44e9-9877-3d1c012a7f64)
To run test : ``` docker-compose -f docker-compose.test.yml up  --build ```
After tests stop postgres CTRL + C and ``` docker rm postgres   ```