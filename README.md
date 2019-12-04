# Serverless Demo PyData 2019

Rapid demo of Chalice framework to emphasize the ease of CI/CD for Serverless development.


```
curl -X GET http://127.0.0.1:8080/
```

```
curl -X POST http://127.0.0.1:8080/shout/kyle -H "Content-Type: application/json" -d '{"hello": "world"}'
```

```
curl -X POST http://127.0.0.1:8080/shout/kyle -H "Content-Type: application/json" -d 'Listen to Data Skeptic'
```
