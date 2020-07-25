# Instructions

The goal of this exercise is to create a REST API using Java that calculates
the average of a given column in a CSV file. For instance, given
the CSV file data.csv in this repository:

```bash
curl -X POST -F 'data=@data.csv' -F 'column=number' http://localhost:8080
```

should return

```json
{
   "data": 42.0
}
```

You can use any method you would like to do this, as long as it
uses maven to build and uses Java. 

If you'd like to use Spring Boot, here is a shortcut to get that started:

https://start.spring.io/#!type=maven-project&language=java&platformVersion=2.3.2.RELEASE&packaging=jar&jvmVersion=1.8&groupId=healthcare.carta.interview&artifactId=rest-csv&name=rest-csv&description=REST%20API%20Exercise&packageName=healthcare.carta.interview.rest-csv&dependencies=hateoas,devtools
# Submission Instructions
Create a zip file or git repository with your answer and
send it along to us. 

# Evaluation
We will do the following to check that the code works:

```bash
unzip yourcode.zip
cd yourcode
mvn spring-boot:run  # or whatever run command you give us here to use

# In another terminal
curl -X POST -F 'data=@data.csv' -F 'column=number' http://localhost:8080
```

And will look to make sure that the answer is the average of our
"number" column in the CSV we'll use to evaluate.

Don't hesitate to reach out if there are any questions!
