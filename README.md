# Serverless Demo PyData 2019

Rapid demo of Chalice framework to emphasize the ease of CI/CD for Serverless development.


```
curl -X GET https://pwh6wk0hff.execute-api.us-east-2.amazonaws.com/api/
```

```
curl -X POST https://pwh6wk0hff.execute-api.us-east-2.amazonaws.com/api/shout/kyle -H "Content-Type: application/json" -d '{"hello": "world"}'
```

```
curl -X POST https://pwh6wk0hff.execute-api.us-east-2.amazonaws.com/api/shout/kyle -H "Content-Type: application/json" -d 'Listen to Data Skeptic'
```
