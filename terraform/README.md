# Build Infrastructure on GCP
1. Intialize the modules and providers
```bash
terraform init
```
2. Plan the changes
```bash
terraform plan -out tf.plan
```
3. Apply the infrastructure
```bash
terraform apply tf.plan
```
4. Destroy the Infrastructure at the end
```bash
terraform destroy
```