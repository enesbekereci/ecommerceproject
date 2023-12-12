# Task - 66


## Concept

This is a small e-commerce project.
Customers add items to their carts, and pay for their goods.

The platform says if the item in customer's cart is not available, the rest of the cart will be delivered, free of charge. 
But the developers thought, if a hacker modifies the cart data, then (s)he can buy everything for free, always.
So they put a log line to catch the hacker. 

Also, the integration with the payment adapter is weak, it'll give error one out of 10 times.
The developers couldn't reproduce the issue, so a fix should be applied. 
Server returns HTTP 500 for such cases


## What to do

1- Please Dockerize the project. (An python docker image would do the trick)
2- Use Docker Compose to scale it up to run 5 instances of the process. (Create a `docker-compose.yml`)
3- Centralize the logging system with your preference. (Sentry + your favorite logging stack, create another `docker-compose.yml`)


## Initial Instructions

```
pip install -r requirements.txt
python run.py
```

You may want to create a virtualenv, insead of using the system Python


## Notes

1- You should provide not one but two `docker-compose.yml` files. One for this project, one for your logging system
2- Your single log system instance should show which instance had the payment error.
3- You should show how that hacker can put an illegal item and how we can see it in the logs. 
A python script that does that is appreciated.
4- You should provide the instructions (like we did) to run your code.


## Submit

1- Push that project into a remote repository using your favorite git account and provide the link
2- If you think you're unable to achieve some of these, please point that out.


## Timing

You have 2 days to complete this task.
