# **Daily AWS Cost And Usage Bill**


AWS EventBridge is used to trigger a Lambda funtion which will fetch the daily cost usage using the Cost
Explorer API and then it will convert it into CSV file and then upload it into the S3 Bucket. The Bucket will
trigger another Lambda function which will send a mail with the attached file which was being uploaded, to
the recipients..

### **Cost of the Architecture**

Cost Explorer - 0.01$ per API Call

S3 Bucket – Negligible

Lambda Function – Negligible

SES Service – Negligible

----------------------------------------------------------------------------------------------------------------------------------


### **Architecture**





![structure](https://user-images.githubusercontent.com/55629302/198555151-a6365b64-97b3-47ab-9692-48bd42fecfde.jpg)



---------------------------------------------------------------------------------------------------------------------------------

# **Steps**

--- Create a **EventBridge** Cron job to trigger a Lambda Function daily as your specified time.

--- Create the **Lambda Funciton** to get the daily bill using Cost Explorer API

       Use the python code from LambdaFunctions/getDailyBill.py
       
       Add a Pandas Layer in the function
       
       And use Environtment Variable for the Bucket Name ( Key - BUCKET , Value - "Your Bucket Name" )

