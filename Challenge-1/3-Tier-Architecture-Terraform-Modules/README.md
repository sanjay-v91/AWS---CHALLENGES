# 3-tier-vpc Architecture

# As part of Resuability / Reproducibility I have used Terraform Modules

#Created  one public_subnet , one private_subnets , one database_subnets in each of the the Availability Zone. Like that i have deployed these subnets across 
3 AZ's (us-west-1a, us-west-1b, us-west-1c).
  private_subnets                  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets                   = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  database_subnets                 = ["10.0.21.0/24", "10.0.22.0/24", "10.0.23.0/24"]
  
#Created Security Groups
  
#Created Application Loadbalancer

#Created An autocaling group 

#Created MySQL Database

#Created above resources using the Terraform commands
1. Terraform init
2. Terraform plan
3. Terraform apply
