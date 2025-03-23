# Create EKS Cluster
aws eks create-cluster --name job-tracker-cluster \
  --region ca-central-1 \
  --role-arn arn:aws:iam::732978450718:role/EKSRole \
  --resources-vpc-config subnetIds=subnet-0cfcff502578cb837,subnet-0cf60e155ec8c357b,securityGroupIds=sg-004515ef98a36b996 \
  --profile personal-account

# Create EKS Nodegroup
aws eks create-nodegroup --cluster-name job-tracker-cluster \
  --nodegroup-name eks-nodes \
  --scaling-config minSize=1,maxSize=3,desiredSize=2 \
  --subnets subnet-0cfcff502578cb837 subnet-0cf60e155ec8c357b \
  --instance-types t3.medium \
  --node-role arn:aws:iam::732978450718:role/EKSWorkerRole \
  --profile personal-account

# Update kubeconfig for kubectl
aws eks update-kubeconfig --region ca-central-1 --name job-tracker-cluster \
  --profile personal-account

aws eks update-kubeconfig --region ca-central-1 --name job-tracker-cluster --profile personal-account

helm list --all-namespaces  # List all Helm releases
helm uninstall <release-name> -n <namespace>  # Uninstall a specific release

helm uninstall job-tracker-frontend -n frontend
helm uninstall job-tracker-backend -n backend


kubectl delete namespace frontend backend
kubectl delete all --all -n frontend
kubectl delete all --all -n backend
kubectl delete all --all -A  # Delete everything in all namespaces

aws eks delete-cluster --name job-tracker-cluster --region ca-central-1 --profile personal-account

aws eks list-nodegroups --cluster-name job-tracker-cluster --profile personal-account
aws eks delete-nodegroup --cluster-name job-tracker-cluster --nodegroup-name eks-nodes --profile personal-account

