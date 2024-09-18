# DemoFlaskApp

Application Details
There are 3 services. First one is a product catalog service and is of type Load Balancer and has a path /productdetails. This will be used by the end user to get the product details
Then there is second service called Flask Service which is of type ClusterIP and has a path /getproductdetails. This service stores data into 3 rd service Redis and retrieves details from it.

FF+ CE Scenarios
We have created a FF product_details on Harness. This is a classic scenario where if a FF is off then the response is 404 Feature not found and if the FF is on then we provide the Product details
In the second scenario, we have used POD API Modify Body fault to corrupt and mock the response of Flask Service for path /getproductdetails to provide as Test. In our product catalog application we have handled the validation and error handling  where if the response does not contain P as keyword for product. We respond to the user as a Bad Request, Corrupted response. An HTTP probe is created to validate the error handling scenarios.

In the second scenario, we have dropped the network packets between Product Catalog and Flask app to verify if the application hangs or if the application uses async communication (This is somethign that we can explain in depth to the customer)
