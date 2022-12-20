# Locust Tests Results

Playing with the locust settings I found that with a scaling of 1, the locust start showing errors with a Spawn Rate of 6 (22% failer/request), with a S.R of 7 the locust even didn't start, the model container turned off. 

Changing the scale to 5 times and Spawn Rate of 6 and 8, Locust didn't show any failure, meaning that the app were able to recieve more request/second than before. This setting started showing failures with a S.R of 10 wuth a rate of 27%.

## Test 1

```
├── Test 1
│   ├── # Locust Setting: Number of Users: 100 | Spawn Rate: 5 | Scaling: No
│   ├── # Hardware specs: Model: 3.84 GB | Redis: 3.84 | ml_api: 3.84 | Scaled: No
├── get "/"
│   ├── # requests: 21
│   ├── # fails: 0
│   ├── # fails/request: 0%
├── post "/predict"
│   ├── # requests: 31
│   ├── # fails: 0
│   ├── # fails/request: 0%
```

## Test 2

```
├── Test 2
│   ├── # Locust Setting: Number of Users: 100 | Spawn Rate: 6 | Scaling: No
│   ├── # Hardware specs: Model: 3.84 GB | Redis: 3.84 | ml_api: 3.84 | Scaled: No
├── get "/"
│   ├── # requests: 20
│   ├── # fails: 0
│   ├── # fails/request: 0%
├── post "/predict"
│   ├── # requests: 36
│   ├── # fails: 8
│   ├── # fails/request: 22%
```

## Test 3 - 

```
├── Test 3
│   ├── # Locust Setting: Number of Users: 100 | Spawn Rate: 6 | Scaling: 5 times
│   ├── # Hardware specs: Model: 3.84 GB | Redis: 3.84 | ml_api: 3.84 | Scaled: 5
├── get "/"
│   ├── # requests: 151
│   ├── # fails: 0
│   ├── fails/request: 0%
├── post "/predict"
│   ├── # requests: 260
│   ├── # fails: 0
│   ├── fails/request: 0%
```

## Test 4 

```
├── Test 4
│   ├── # Locust Setting: Number of Users: 100 | Spawn Rate: 8 | Scaling: 5 times
│   ├── # Hardware specs: Model: 3.84 GB | Redis: 3.84 | ml_api: 3.84 | Scaled: 5
├── get "/"
│   ├── # requests: 63
│   ├── # fails: 0
│   ├── fails/request: 0%
├── post "/predict"
│   ├── # requests: 129
│   ├── # fails: 8
│   ├── fails/request: 0%

```
## Test 5 
- 
- model container = 3.84 GB x 5 

├── Test 5
│   ├── # Locust Setting: Number of Users: 100 | Spawn Rate: 10 | Scaling: 5 times
│   ├── # Hardware specs: Model: 3.84 GB | Redis: 3.84 | ml_api: 3.84 | Scaled: 5
├── get "/"
│   ├── # requests: 19
│   ├── # fails: 0
│   ├── fails/request: 0%
├── post "/predict"
│   ├── # requests: 29
│   ├── # fails: 8
│   ├── fails/request: 27%
```